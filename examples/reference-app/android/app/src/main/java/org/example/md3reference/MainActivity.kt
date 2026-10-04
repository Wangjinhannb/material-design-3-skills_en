package org.example.md3reference
import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.testTag
import androidx.compose.ui.unit.dp
class MainActivity:ComponentActivity(){override fun onCreate(savedInstanceState:Bundle?){super.onCreate(savedInstanceState);setContent{ReferenceApp()}}}
@Composable fun ReferenceApp(){var name by remember{mutableStateOf("Material User")};var notifications by remember{mutableStateOf(true)};var saved by remember{mutableStateOf(false)};MaterialTheme{Scaffold(topBar={TopAppBar(title={Text("MD3 Reference")})}){p->LazyColumn(Modifier.fillMaxSize().padding(p),contentPadding=PaddingValues(20.dp),verticalArrangement=Arrangement.spacedBy(16.dp)){item{Text("Classic Material Design 3",style=MaterialTheme.typography.headlineMedium);Text("Cross-platform reference app",style=MaterialTheme.typography.titleLarge);Button(onClick={}){Text("Primary action")}};item{Text("Overview",Modifier.testTag("reference-overview"),style=MaterialTheme.typography.titleLarge);Row(horizontalArrangement=Arrangement.spacedBy(10.dp)){Card(Modifier.weight(1f)){Text("Token",Modifier.padding(16.dp))};Card(Modifier.weight(1f)){Text("Adaptive",Modifier.padding(16.dp))};Card(Modifier.weight(1f)){Text("State",Modifier.padding(16.dp))}}};item{Text("List",Modifier.testTag("reference-list"),style=MaterialTheme.typography.titleLarge);ListItem(headlineContent={Text("Item A")},supportingContent={Text("Supporting information")});ListItem(headlineContent={Text("Item B")},supportingContent={Text("Supporting information")})};item{Text("Form",Modifier.testTag("reference-form"),style=MaterialTheme.typography.titleLarge);OutlinedTextField(value=name,onValueChange={name=it},label={Text("Display name")});Row{Switch(checked=notifications,onCheckedChange={notifications=it});Text("Enable notifications",Modifier.padding(10.dp))};Button(onClick={saved=true}){Text("Save")};if(saved)Text("Settings saved",color=MaterialTheme.colorScheme.primary)};item{Text("Settings",Modifier.testTag("reference-settings"),style=MaterialTheme.typography.titleLarge);Text("Theme follows the system; content stays readable and operable as the window changes.")}}}}}
