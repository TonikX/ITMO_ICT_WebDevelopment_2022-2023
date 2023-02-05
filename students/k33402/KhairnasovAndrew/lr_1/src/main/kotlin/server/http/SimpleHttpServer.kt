package org.dazai.server.http

import org.dazai.utils.http.HttpRequest
import org.dazai.utils.http.HttpResponse
import org.slf4j.Logger
import org.slf4j.LoggerFactory
import java.io.File
import java.time.LocalDateTime

class SimpleHttpServer : AbstractHttpServer() {
    companion object {
        private val LOG = LoggerFactory.getLogger(SimpleHttpServer::class.java)
    }

    override suspend fun getResponse(request: HttpRequest): HttpResponse {
        return HttpResponse(
            200,
            mapOf("date" to LocalDateTime.now().toString()),
            File("index.html").readText()
        )
    }

    override fun getLogger(): Logger = LOG
}