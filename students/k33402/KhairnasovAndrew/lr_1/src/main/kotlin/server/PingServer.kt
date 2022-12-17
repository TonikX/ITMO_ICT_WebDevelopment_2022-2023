package org.dazai.server

import io.ktor.network.sockets.Socket
import io.ktor.utils.io.ByteReadChannel
import io.ktor.utils.io.ByteWriteChannel
import io.ktor.utils.io.writeStringUtf8
import org.slf4j.Logger
import org.slf4j.LoggerFactory

class PingServer : AbstractServer() {
    companion object {
        private val LOG = LoggerFactory.getLogger(PingServer::class.java)
    }

    override fun getLogger(): Logger = LOG

    override suspend fun handler(
        receiveChannel: ByteReadChannel,
        sendChannel: ByteWriteChannel,
        socket: Socket
    ) {
        try {
            while (true) {
                val message = receiveChannel.readUTF8Line(256)
                if (message != null) {
                    LOG.info("From client received message: $message")
                    sendChannel.writeStringUtf8("Hello, client!\n")
                }
            }
        } catch (e: Throwable) {
            socket.close()
        }
    }
}