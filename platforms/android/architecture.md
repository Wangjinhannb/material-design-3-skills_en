# Architecture

Kotlin, Jetpack Compose, and `androidx.compose.material3`.

Compose Material 3 is the primary official implementation reference. Current packages also expose Expressive APIs, so repository code stays within the Classic baseline.

Platform code consumes generated tokens or an equivalent shared theme entry point. Business logic stays outside the visual mapping layer.
