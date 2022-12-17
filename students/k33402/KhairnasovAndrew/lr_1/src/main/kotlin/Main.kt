package org.dazai

import kotlinx.cli.ArgParser
import kotlinx.cli.ExperimentalCli
import org.dazai.subcommands.ClientSubcommand
import org.dazai.subcommands.ServerSubcommand
import org.slf4j.LoggerFactory.getLogger

@OptIn(ExperimentalCli::class)
fun main(args: Array<String>) {
    val logger = getLogger("main")
    logger.debug("Starting with args: ${args.joinToString(" ")}")

    val parser = ArgParser("Simple socket server/client app", strictSubcommandOptionsOrder = true)

    parser.subcommands(ServerSubcommand(), ClientSubcommand())
    parser.parse(args)
}