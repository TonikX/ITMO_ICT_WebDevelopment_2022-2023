package org.dazai.client.math

import io.ktor.network.selector.SelectorManager
import io.ktor.network.sockets.Socket
import io.ktor.network.sockets.aSocket
import io.ktor.network.sockets.openReadChannel
import io.ktor.network.sockets.openWriteChannel
import io.ktor.utils.io.ByteWriteChannel
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.delay
import kotlinx.coroutines.launch
import kotlinx.coroutines.runBlocking
import kotlinx.coroutines.withContext
import org.slf4j.Logger
import java.nio.ByteBuffer
import kotlin.system.exitProcess

abstract class AbstractMathClient {
    abstract fun getLogger(): Logger

    protected abstract suspend fun inputAndSendData(sendChannel: ByteWriteChannel)

    protected abstract suspend fun convertResult(byteBuffer: ByteBuffer): String

    fun doConnection(host: String, port: Int) {
        runBlocking {
            val selectorManager = SelectorManager(Dispatchers.IO)
            val socket: Socket
            try {
                socket = aSocket(selectorManager).tcp().connect(host, port)
            } catch (e: Exception) {
                getLogger().error("Port is not opened")
                throw e
            }

            val receiveChannel = socket.openReadChannel()
            val sendChannel = socket.openWriteChannel(autoFlush = true)

            while (true) {
                try {
                    inputAndSendData(sendChannel)
                } catch (e: Exception) {
                    getLogger().warn("Server closed a connection")
                    withContext(Dispatchers.IO) {
                        socket.close()
                    }
                    withContext(Dispatchers.IO) {
                        selectorManager.close()
                    }
                    exitProcess(0)
                }
                delay(1_000L)
                val resultBuffer = ByteBuffer.allocate(1 shl 16)
                try {
                    receiveChannel.readAvailable(resultBuffer)
                } catch (e: Exception) {
                    getLogger().warn("Server closed a connection")
                    withContext(Dispatchers.IO) {
                        socket.close()
                    }
                    withContext(Dispatchers.IO) {
                        selectorManager.close()
                    }
                    exitProcess(0)
                }
                val message = convertResult(resultBuffer)
                println(message)
            }
        }
    }
}