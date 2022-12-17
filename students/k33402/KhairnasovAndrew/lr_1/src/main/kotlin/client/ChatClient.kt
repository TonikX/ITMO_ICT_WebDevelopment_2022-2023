package org.dazai.client

import io.ktor.network.sockets.isClosed
import io.ktor.utils.io.ByteReadChannel
import io.ktor.utils.io.ByteWriteChannel
import kotlinx.serialization.ExperimentalSerializationApi
import kotlinx.serialization.decodeFromByteArray
import kotlinx.serialization.encodeToByteArray
import kotlinx.serialization.protobuf.ProtoBuf
import org.dazai.dto.ChatMessage
import org.slf4j.Logger
import org.slf4j.LoggerFactory
import java.nio.ByteBuffer

class ChatClient : AbstractAsyncClient() {
    companion object {
        private val LOG = LoggerFactory.getLogger(ChatClient::class.java)
    }

    override fun getLogger(): Logger = LOG

    @OptIn(ExperimentalSerializationApi::class)
    override suspend fun startSender(sendChannel: ByteWriteChannel) {
        print("Input username: ")
        val name = readLine()!!
        sendChannel.writeFully(ByteBuffer.wrap(ProtoBuf.encodeToByteArray(name)))

        while (!socket!!.isClosed) {
            print("Input message: ")
            val messageBody = readLine()!!

            val byteBuffer = ByteBuffer.wrap(ProtoBuf.encodeToByteArray(ChatMessage(name, messageBody)))
            try {
                sendChannel.writeFully(byteBuffer)
            } catch (e: Exception) {
                onServerClose()
            }
        }
    }

    @OptIn(ExperimentalSerializationApi::class)
    override suspend fun startReader(receiveChannel: ByteReadChannel) {
        while (!socket!!.isClosed) {
            val byteBuffer = ByteBuffer.allocate(1 shl 16)
            receiveChannel.readAvailable(byteBuffer)
            val message = try {
                ProtoBuf.decodeFromByteArray<ChatMessage>(
                    byteBuffer.array()
                        .filter { it != 0.toByte() }
                        .toByteArray()
                )
            } catch (e: Exception) {
                LOG.error("Message in wrong format")
                LOG.error(e.stackTraceToString())
                onServerClose()
                return
            }

            LOG.info("${message.name}: ${message.messageBody}")
        }
    }
}