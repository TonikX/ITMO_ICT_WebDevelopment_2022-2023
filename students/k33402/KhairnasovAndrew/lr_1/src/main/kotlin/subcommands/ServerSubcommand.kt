package org.dazai.subcommands

import org.dazai.server.ChatServer
import org.dazai.server.PingServer
import org.dazai.server.http.LessonHttpServer
import org.dazai.server.http.SimpleHttpServer
import org.dazai.server.math.SquareEquationServer

class ServerSubcommand : AbstractSubcommand("server", "") {
    override fun execute() {
        when (type) {
            in setOf("PingServer", "first", "simple") -> PingServer().startPooling(host, port)
            in setOf("SquareEquationServer") -> SquareEquationServer().startPooling(host, port)
            in setOf("ChatServer") -> ChatServer().startPooling(host, port)
            in setOf("SimpleHttpServer") -> SimpleHttpServer().startPooling(host, port)
            in setOf("LessonHttpServer") -> LessonHttpServer().startPooling(host, port)
        }
    }
}