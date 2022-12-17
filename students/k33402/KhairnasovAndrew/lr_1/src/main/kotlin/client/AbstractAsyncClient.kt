package org.dazai.client

import io.ktor.network.selector.SelectorManager
import io.ktor.network.sockets.Socket
import io.ktor.network.sockets.aSocket
import io.ktor.network.sockets.openReadChannel
import io.ktor.network.sockets.openWriteChannel
import io.ktor.utils.io.ByteReadChannel
import io.ktor.utils.io.ByteWriteChannel
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import kotlinx.coroutines.runBlocking
import org.slf4j.Logger

abstract class AbstractAsyncClient {
    protected val selectorManager = SelectorManager(Dispatchers.IO)
    protected var socket: Socket? = null

    protected abstract fun getLogger(): Logger

    protected abstract suspend fun startSender(sendChannel: ByteWriteChannel)

    protected abstract suspend fun startReader(receiveChannel: ByteReadChannel)

    protected fun onServerClose() {
        getLogger().error("Server socket closed")
        socket!!.close()
        selectorManager.close()
    }

    fun doConnection(host: String, port: Int) {
        runBlocking {
            socket = try {
                aSocket(selectorManager).tcp().connect(host, port)
            } catch (e: Exception) {
                getLogger().error("Port is not opened")
                throw e
            }

            val receiveChannel = socket!!.openReadChannel()
            val sendChannel = socket!!.openWriteChannel(autoFlush = true)

            launch(Dispatchers.IO) {
                startReader(receiveChannel)
            }

            startSender(sendChannel)
        }
    }
}