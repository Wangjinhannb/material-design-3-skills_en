package org.example.md3catalog

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent

class CatalogActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent { CatalogApp() }
    }
}
