package org.dazai.server.http

import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.ObsoleteCoroutinesApi
import kotlinx.coroutines.channels.Channel
import kotlinx.coroutines.channels.SendChannel
import kotlinx.coroutines.channels.actor
import kotlinx.serialization.decodeFromString
import kotlinx.serialization.encodeToString
import kotlinx.serialization.json.Json
import org.dazai.dto.LessonBody
import org.dazai.utils.http.HttpRequest
import org.dazai.utils.http.HttpResponse
import org.slf4j.Logger
import org.slf4j.LoggerFactory

private sealed class LessonActorMsg {
    class GetLesson(val lessonName: String, val channel: SendChannel<List<Double>>) : LessonActorMsg()
    class AddLessonMark(val lessonName: String, val marks: List<Double>) : LessonActorMsg()
}

@OptIn(ObsoleteCoroutinesApi::class)
private fun CoroutineScope.getLessonActor() = actor<LessonActorMsg> {
    val lessons = mutableMapOf<String, MutableList<Double>>()
    for (msg in channel) {
        when (msg) {
            is LessonActorMsg.GetLesson -> msg.channel.send(lessons[msg.lessonName] ?: emptyList())
            is LessonActorMsg.AddLessonMark -> {
                lessons.putIfAbsent(msg.lessonName, mutableListOf())
                lessons[msg.lessonName]!!.addAll(msg.marks)
            }
        }
    }
}

private infix fun String.matches(regex: Regex) = regex matches this

class LessonHttpServer : AbstractHttpServer() {
    companion object {
        private val LOG = LoggerFactory.getLogger(LessonHttpServer::class.java)
    }

    private lateinit var lessonActor: SendChannel<LessonActorMsg>

    override fun postStart() {
        super.postStart()
        lessonActor = coroutineScope.getLessonActor()
    }

    override suspend fun getResponse(request: HttpRequest): HttpResponse {
        return try {
            mapRequest(request)
        } catch (e: Exception) {
            LOG.error(e.stackTraceToString())
            HttpResponse(500, emptyMap())
        }
    }

    private suspend fun mapRequest(request: HttpRequest): HttpResponse {
        val trimmed = request.url.trim('/')
        return if (trimmed == "lesson" && request.method == "POST") {
            addLesson(request)
        } else if (trimmed matches "lesson\\?lesson=\\w*".toRegex() && request.method == "GET") {
            getJsonResponse(request)
        } else if (trimmed matches "\\?lesson=\\w*".toRegex() && request.method == "GET") {
            getHtmlResponse(request)
        } else HttpResponse(
            404,
            mapOf(),
            """<p>NOT FOUND</p><img src="https://juststickers.in/wp-content/uploads/2016/12/404-error-not-found.png">"""
        )
    }

    private suspend fun getHtmlResponse(request: HttpRequest): HttpResponse {
        val channel = Channel<List<Double>>()
        val lessonName = request.url.split("=")[1]
        lessonActor.send(LessonActorMsg.GetLesson(lessonName, channel))

        return HttpResponse(
            200,
            emptyMap(),
            LessonHttpServer::class.java.getResource("/lessons.html")!!.readText()
                .format(lessonName, channel.receive().joinToString(", "))
        )
    }

    private suspend fun getJsonResponse(request: HttpRequest): HttpResponse {
        val channel = Channel<List<Double>>()
        val lessonName = request.url.split("=")[1]
        lessonActor.send(LessonActorMsg.GetLesson(lessonName, channel))

        return HttpResponse(200, emptyMap(), Json.encodeToString(LessonBody(lessonName, channel.receive())))
    }

    private suspend fun addLesson(request: HttpRequest): HttpResponse {
        if (request.body == null) {
            return HttpResponse(400, mapOf(), "Invalid data")
        }
        val body = try {
            Json.decodeFromString<LessonBody>(request.body)
        } catch (e: Exception) {
            LOG.error(e.stackTraceToString())
            return HttpResponse(400, mapOf(), "Invalid data")
        }

        lessonActor.send(LessonActorMsg.AddLessonMark(body.lessonName, body.marks))
        return HttpResponse(
            200,
            mapOf(),
            Json.encodeToString(listOf("ok"))
        )
    }

    override fun getLogger(): Logger = LOG
}