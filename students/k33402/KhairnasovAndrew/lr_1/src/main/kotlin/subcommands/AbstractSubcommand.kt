package org.dazai.subcommands

import kotlinx.cli.ArgType
import kotlinx.cli.ExperimentalCli
import kotlinx.cli.Subcommand
import kotlinx.cli.default

@OptIn(ExperimentalCli::class)
abstract class AbstractSubcommand(name: String, actionDescription: String) : Subcommand(name, actionDescription) {
    protected val type by argument(ArgType.String)
    protected val host by option(ArgType.String, "host").default("localhost")
    protected val port by option(ArgType.Int, "port", "p").default(9000)
}