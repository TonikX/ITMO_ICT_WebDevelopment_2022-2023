package org.dazai.server.math

import io.ktor.utils.io.ByteWriteChannel
import kotlinx.serialization.ExperimentalSerializationApi
import kotlinx.serialization.decodeFromByteArray
import kotlinx.serialization.encodeToByteArray
import kotlinx.serialization.protobuf.ProtoBuf
import org.slf4j.Logger
import org.slf4j.LoggerFactory
import java.nio.ByteBuffer

class SquareEquationServer : AbstractMathServer() {
    companion object {
        private val LOG = LoggerFactory.getLogger(SquareEquationServer::class.java)
    }

    override fun getLogger(): Logger = LOG

    @OptIn(ExperimentalSerializationApi::class)
    override suspend fun consumer(
        byteBuffer: ByteBuffer,
        sendChannel: ByteWriteChannel
    ) {
        val args: List<Double>
        try {
            args = ProtoBuf.decodeFromByteArray(byteBuffer.array())
        } catch (e: Exception) {
            LOG.error("Data is not valid")
            sendEmptyList(sendChannel)
            return
        }

        if (args.size > 3) {
            val message = "Invalidate data: too many args passed"
            LOG.error(message)
            sendEmptyList(sendChannel)
            return
        }

        val d = args[1] * args[1] - 4 * args[0] * args[2]
        if (d < 0) {
            val message = "Value is complex"
            LOG.error(message)
            sendEmptyList(sendChannel)
            return
        }
        val result1 = (-args[1] + kotlin.math.sqrt(d)) / (2 * args[0])
        val result2 = (-args[1] - kotlin.math.sqrt(d)) / (2 * args[0])
        LOG.info("Results is $result1 and $result2")

        val responseBuffer = ByteBuffer.wrap(ProtoBuf.encodeToByteArray(listOf(result1, result2)))
        sendChannel.writeFully(responseBuffer)
    }

    @OptIn(ExperimentalSerializationApi::class)
    suspend fun sendEmptyList(sendChannel: ByteWriteChannel) {
        val responseBuffer = ByteBuffer.wrap(ProtoBuf.encodeToByteArray(listOf<Double>()))
        sendChannel.writeFully(responseBuffer)
    }
}