package org.dazai.server

import io.ktor.network.sockets.Socket
import io.ktor.network.sockets.isClosed
import io.ktor.utils.io.ByteReadChannel
import io.ktor.utils.io.ByteWriteChannel
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import kotlinx.serialization.ExperimentalSerializationApi
import kotlinx.serialization.decodeFromByteArray
import kotlinx.serialization.encodeToByteArray
import kotlinx.serialization.protobuf.ProtoBuf
import org.dazai.dto.ChatMessage
import org.slf4j.Logger
import org.slf4j.LoggerFactory
import java.lang.NullPointerException
import java.nio.ByteBuffer

class ChatServer : AbstractServer() {
    private data class Client(
        val conId: Long,
        val name: String,
        private val writeChannel: ByteWriteChannel
    ) {
        @OptIn(ExperimentalSerializationApi::class)
        suspend fun sendMessage(message: ChatMessage) {
            val byteBuffer = ByteBuffer.wrap(ProtoBuf.encodeToByteArray(message))
            writeChannel.writeFully(byteBuffer)
        }
    }

    companion object {
        private val LOG = LoggerFactory.getLogger(ChatServer::class.java)
    }

    private val clients = mutableListOf<Client>()
    private var connCounter = 0L

    @OptIn(ExperimentalSerializationApi::class)
    private suspend fun startReader(receiveChannel: ByteReadChannel, socket: Socket, currClient: Client) {
        while (!socket.isClosed) {
            val byteBuffer = ByteBuffer.allocate(1 shl 16)
            receiveChannel.readAvailable(byteBuffer)
            val message = try {
                ProtoBuf.decodeFromByteArray<ChatMessage>(
                    byteBuffer.array()
                        .filter { it != 0.toByte() }
                        .toByteArray()
                )
            } catch (e: Exception) {
                if (byteBuffer.array().none { it != 0.toByte() }) {
                    LOG.error("Client with id ${currClient.conId} (${currClient.name}) disconnected")
                    clients.removeIf { it.conId == currClient.conId }
                    socket.close()
                    return
                }
                LOG.error("Message in wrong format")
                LOG.error(e.stackTraceToString())
                continue
            }
            LOG.info("Client with ${currClient.conId} (${currClient.name}) sent ${message.messageBody}")
            clients.filter { it.conId != currClient.conId }
                .forEach { client ->
                    try {
                        client.sendMessage(message)
                    } catch (e: Exception) {
                        LOG.error("Client with name ${client.name} is unavailable")
                        clients.removeIf { it.conId == client.conId }
                        return
                    }
                }
        }
    }

    override fun getLogger(): Logger = LOG

    @OptIn(ExperimentalSerializationApi::class)
    override suspend fun handler(
        receiveChannel: ByteReadChannel,
        sendChannel: ByteWriteChannel,
        socket: Socket
    ) {
        val buffer = ByteBuffer.allocate(1 shl 16)
        receiveChannel.readAvailable(buffer)
        if (buffer.array().none { it != 0.toByte() }) {
            LOG.error("Client unavailable")
            throw NullPointerException("name must be not null")
        }
        val name = ProtoBuf.decodeFromByteArray<String>(buffer.array())
        connCounter ++
        val currClient = Client(connCounter, name, sendChannel)
        clients.add(currClient)
        coroutineScope.launch(Dispatchers.IO) {
            startReader(receiveChannel, socket, currClient)
        }
    }
}