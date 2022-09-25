package org.dazai.server.http

import io.ktor.network.sockets.Socket
import io.ktor.utils.io.ByteReadChannel
import io.ktor.utils.io.ByteWriteChannel
import org.dazai.utils.http.HttpRequest
import org.dazai.utils.http.HttpResponse
import org.dazai.server.AbstractServer
import java.nio.ByteBuffer

abstract class AbstractHttpServer : AbstractServer() {
    abstract suspend fun getResponse(request: HttpRequest): HttpResponse

    override suspend fun handler(
        receiveChannel: ByteReadChannel,
        sendChannel: ByteWriteChannel,
        socket: Socket
    ) {
        val buffer = ByteBuffer.allocate(1 shl 16)
        receiveChannel.readAvailable(buffer)
        val request = HttpRequest.parse(buffer.array().decodeToString())
        sendChannel.writeFully(ByteBuffer.wrap(getResponse(request).buildString().encodeToByteArray()))
        socket.close()
    }
}