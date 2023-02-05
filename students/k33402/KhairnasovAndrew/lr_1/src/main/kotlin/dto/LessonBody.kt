package org.dazai.dto

import kotlinx.serialization.Serializable

@Serializable
data class LessonBody(
    val lessonName: String,
    val marks: List<Double>
)
