package org.dazai.utils.http

import java.lang.StringBuilder

data class HttpRequest(
    val method: String,
    val url: String,
    val headers: Map<String, String>,
    val body: String? = null
) {
    companion object {
        fun parse(s: String): HttpRequest {
            val rows = s.split("\n").map { it.trim('\r') }
            val builder = HttpRequestBuilder()
            builder.setMethod(rows.first().split(" ")[0])
            builder.setUrl(rows.first().split(" ")[1])

            val emptyRow = rows.indexOf("")
            builder.headers.putAll(
                rows.subList(1, if (emptyRow != -1) emptyRow else rows.size).map { row ->
                    val (name, value) = row.split(":").map { it.trim() }
                    Pair(name, value)
                }
            )

            if (emptyRow != -1) {
                builder.setBody(rows.subList(emptyRow, rows.size).joinToString("\n").trim('\u0000'))
            }

            return builder.build()
        }
    }

    fun buildString(): String {
        val sb = StringBuilder()
        sb.append("$method $url HTTP/1.0\n")

        headers.forEach { (name, value) ->
            sb.append("$name: $value\n")
        }

        sb.append("\n")

        if (body != null) {
            sb.append(body)
        }

        return sb.toString()
    }

    class HttpRequestBuilder(
        var method: String? = null,
        var url: String? = null,
        var headers: MutableMap<String, String> = mutableMapOf(),
        var body: String? = null
    ) {
        fun setMethod(s: String?): HttpRequestBuilder {
            method = s
            return this
        }

        fun setUrl(s: String?): HttpRequestBuilder {
            url = s
            return this
        }

        fun setHeaders(h: Map<String, String>): HttpRequestBuilder {
            headers = h.toMutableMap()
            return this
        }

        fun setBody(s: String?): HttpRequestBuilder {
            body = s
            return this
        }

        fun addHeader(name: String, value: String) {
            headers[name] = value
        }

        fun delHeader(name: String) {
            headers.remove(name)
        }

        fun build() = HttpRequest(
            method!!,
            url!!,
            headers,
            body
        )
    }
}