package org.dazai.subcommands

import org.dazai.client.ChatClient
import org.dazai.client.PingClient
import org.dazai.client.math.SquareEquationClient

class ClientSubcommand : AbstractSubcommand("client", "") {
    override fun execute() {
        when (type) {
            in setOf("PingClient", "first", "simple") -> PingClient().doConnection(host, port)
            in setOf("SquareEquationClient") -> SquareEquationClient().doConnection(host, port)
            in setOf("ChatClient") -> ChatClient().doConnection(host, port)
        }
    }
}