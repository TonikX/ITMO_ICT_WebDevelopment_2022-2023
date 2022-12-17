package org.dazai.server

import io.ktor.network.selector.SelectorManager
import io.ktor.network.sockets.Socket
import io.ktor.network.sockets.aSocket
import io.ktor.network.sockets.openReadChannel
import io.ktor.network.sockets.openWriteChannel
import io.ktor.utils.io.ByteReadChannel
import io.ktor.utils.io.ByteWriteChannel
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import kotlinx.coroutines.runBlocking
import org.slf4j.Logger

abstract class AbstractServer {
    protected lateinit var coroutineScope: CoroutineScope

    protected abstract fun getLogger(): Logger

    protected abstract suspend fun handler(
        receiveChannel: ByteReadChannel,
        sendChannel: ByteWriteChannel,
        socket: Socket
    )

    protected open fun postStart() {}

    fun startPooling(host: String, port: Int) {
        runBlocking {
            coroutineScope = this
            postStart()
            val selectorManager = SelectorManager(Dispatchers.IO)
            val serverSocket = try {
                aSocket(selectorManager).tcp().bind(host, port)
            } catch (e: Exception) {
                getLogger().error("Port already in use")
                throw e
            }
            getLogger().info("Server is listening at ${serverSocket.localAddress}")
            while (true) {
                val socket = serverSocket.accept()
                getLogger().info("Accepted $socket")
                launch(Dispatchers.IO) {
                    val receiveChannel = socket.openReadChannel()
                    val sendChannel = socket.openWriteChannel(autoFlush = true)
                    try {
                        handler(receiveChannel, sendChannel, socket)
                    } catch (e: Exception) {
                        getLogger().error(e.stackTraceToString())
                    }
                }
            }
        }
    }
}