package org.dazai.client

import io.ktor.utils.io.ByteReadChannel
import io.ktor.utils.io.ByteWriteChannel
import io.ktor.utils.io.writeStringUtf8
import org.slf4j.Logger
import org.slf4j.LoggerFactory
import kotlin.system.exitProcess

class PingClient : AbstractAsyncClient() {
    companion object {
        private val LOG = LoggerFactory.getLogger(PingClient::class.java)
    }

    override fun getLogger(): Logger = LOG

    override suspend fun startSender(sendChannel: ByteWriteChannel) {
        val myMessage = "Hello, server\n"
        sendChannel.writeStringUtf8(myMessage)
    }

    override suspend fun startReader(receiveChannel: ByteReadChannel) {
        while (true) {
            val message = receiveChannel.readUTF8Line(256)
            if (message != null) {
                LOG.info(message)
            } else {
                onServerClose()
                exitProcess(0)
            }
        }
    }
}