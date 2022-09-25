package org.dazai.dto

import kotlinx.serialization.Serializable

@Serializable
data class ChatMessage(
    val name: String,
    val messageBody: String
)
