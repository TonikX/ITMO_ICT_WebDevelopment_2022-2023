package org.dazai.server.math

import io.ktor.network.sockets.Socket
import io.ktor.utils.io.ByteReadChannel
import io.ktor.utils.io.ByteWriteChannel
import org.dazai.server.AbstractServer
import java.nio.ByteBuffer

abstract class AbstractMathServer : AbstractServer() {
    protected abstract suspend fun consumer(byteBuffer: ByteBuffer, sendChannel: ByteWriteChannel)

    override suspend fun handler(
        receiveChannel: ByteReadChannel,
        sendChannel: ByteWriteChannel,
        socket: Socket
    ) {
        try {
            while (true) {
                val byteBuffer = ByteBuffer.allocate(1 shl 16)
                receiveChannel.readAvailable(byteBuffer)
                consumer(byteBuffer, sendChannel)
            }
        } catch (e: Throwable) {
            socket.close()
        }
    }
}