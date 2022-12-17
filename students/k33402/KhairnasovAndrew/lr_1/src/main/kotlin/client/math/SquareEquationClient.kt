package org.dazai.client.math

import io.ktor.utils.io.ByteWriteChannel
import kotlinx.serialization.ExperimentalSerializationApi
import kotlinx.serialization.decodeFromByteArray
import kotlinx.serialization.encodeToByteArray
import kotlinx.serialization.protobuf.ProtoBuf
import org.slf4j.Logger
import org.slf4j.LoggerFactory
import java.nio.ByteBuffer

class SquareEquationClient : AbstractMathClient() {
    companion object {
        private val LOG = LoggerFactory.getLogger(SquareEquationClient::class.java)
    }

    override fun getLogger(): Logger = LOG

    @OptIn(ExperimentalSerializationApi::class)
    override suspend fun inputAndSendData(sendChannel: ByteWriteChannel) {
        print("Input coefficients for equation: ")
        val coefList = try {
            readLine()!!.split(" ").map { it.toDouble() }
        } catch (e: Exception) {
            LOG.error("Invalid input data")
            return
        }

        val sendBuffer = ByteBuffer.wrap(ProtoBuf.encodeToByteArray(coefList))
        sendChannel.writeFully(sendBuffer)
    }

    @OptIn(ExperimentalSerializationApi::class)
    override suspend fun convertResult(byteBuffer: ByteBuffer): String {
        return ProtoBuf.decodeFromByteArray<List<Double>>(byteBuffer.array())
            .joinToString(" ")
    }
}