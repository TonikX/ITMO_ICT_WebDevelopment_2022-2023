package org.dazai.utils.http

import java.lang.StringBuilder

data class HttpResponse(
    val status: Int,
    val headers: Map<String, String>,
    val body: String? = null
) {
    companion object {
        fun parse(s: String): HttpResponse {
            val builder = HttpResponseBuilder()
            val rows = s.split("\n").map { it.trim('\r') }

            builder.setStatus(rows.first().split(" ")[1].toInt())

            val emptyRow = rows.indexOf("")
            builder.headers.putAll(
                rows.subList(1, if (emptyRow != -1) emptyRow + 1 else rows.size).map { row ->
                    val (name, value) = row.split(":").map { it.trim() }
                    Pair(name, value)
                }
            )

            if (emptyRow != -1) {
                builder.setBody(rows.subList(emptyRow, rows.size).joinToString("\n"))
            }

            return builder.build()
        }
    }

    fun buildString(): String {
        val sb = StringBuilder()
        sb.append("HTTP/1.0 $status Desc\n")

        headers.forEach { (name, value) ->
            sb.append("$name: $value\n")
        }

        sb.append("\n")

        if (body != null) {
            sb.append(body)
        }

        return sb.toString()
    }

    class HttpResponseBuilder(
        var status: Int? = null,
        var headers: MutableMap<String, String> = mutableMapOf(),
        var body: String? = null
    ) {
        fun setStatus(i: Int?): HttpResponseBuilder {
            status = i
            return this
        }

        fun setHeaders(h: Map<String, String>): HttpResponseBuilder {
            headers = h.toMutableMap()
            return this
        }

        fun setBody(s: String?): HttpResponseBuilder {
            body = s
            return this
        }

        fun addHeader(name: String, value: String) {
            headers[name] = value
        }

        fun delHeader(name: String) {
            headers.remove(name)
        }

        fun build() = HttpResponse(
            status!!,
            headers,
            body
        )
    }
}