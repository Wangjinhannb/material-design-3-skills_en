package org.example.md3catalog

import androidx.compose.foundation.BorderStroke
import androidx.compose.foundation.horizontalScroll
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.LazyRow
import androidx.compose.foundation.lazy.items
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.semantics.contentDescription
import androidx.compose.ui.semantics.semantics
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun CatalogApp() {
    var showDialog by remember { mutableStateOf(false) }
    var showSheet by remember { mutableStateOf(false) }
    MaterialTheme {
        Scaffold(topBar = { TopAppBar(title = { Text("MD3 Component Catalog") }) }) { padding ->
            LazyColumn(
                modifier = Modifier.fillMaxSize().padding(padding),
                contentPadding = PaddingValues(20.dp),
                verticalArrangement = Arrangement.spacedBy(14.dp)
            ) {
                item { Section("component-buttons", "Buttons") { Button(onClick = {}) { Text("Filled") }; FilledTonalButton(onClick = {}) { Text("Tonal") }; OutlinedButton(onClick = {}) { Text("Outlined") }; TextButton(onClick = {}) { Text("Text") } } }
                item { Section("component-floating-action-button", "Floating action button") { SmallFloatingActionButton(onClick = {}) { Text("+") }; FloatingActionButton(onClick = {}) { Text("+") }; LargeFloatingActionButton(onClick = {}) { Text("+") }; ExtendedFloatingActionButton(onClick = {}, text = { Text("New") }, icon = { Text("+") }) } }
                item { Section("component-icon-buttons", "Icon buttons") { IconButton(onClick = {}) { Text("☆") }; FilledIconButton(onClick = {}) { Text("★") }; FilledTonalIconButton(onClick = {}) { Text("⋯") }; OutlinedIconButton(onClick = {}) { Text("✎") } } }
                item { Section("component-segmented-buttons", "Segmented buttons") { var index by remember { mutableIntStateOf(0) }; Row { listOf("List","Grid","Compact").forEachIndexed { i,label -> FilterChip(selected=index==i,onClick={index=i},label={Text(label)},shape=RoundedCornerShape(if(i==0) 20.dp else if(i==2) 20.dp else 0.dp)) } } } }
                item { Section("component-badges", "Badges") { BadgedBox(badge={Badge{Text("12")}}){Text("Messages")}; Badge() } }
                item { Section("component-progress-indicators", "Progress indicators") { LinearProgressIndicator(progress={0.62f},modifier=Modifier.width(220.dp)); CircularProgressIndicator() } }
                item { Section("component-snackbars", "Snackbar") { Snackbar(action={TextButton(onClick={}){Text("Undo")}}){Text("Settings saved")} } }
                item { Section("component-tooltips", "Tooltips") { TooltipBox(positionProvider=TooltipDefaults.rememberPlainTooltipPositionProvider(),tooltip={PlainTooltip{Text("Help information")}},state=rememberTooltipState()){OutlinedButton(onClick={}){Text("Hover/Long press")}} } }
                item { Section("component-bottom-sheets", "Bottom sheet") { OutlinedButton(onClick={showSheet=true}){Text("Open sheet")} } }
                item { Section("component-cards", "Cards") { Card(Modifier.width(150.dp)){Box(Modifier.padding(16.dp)){Text("Filled")}}; OutlinedCard(Modifier.width(150.dp)){Box(Modifier.padding(16.dp)){Text("Outlined")}}; ElevatedCard(Modifier.width(150.dp)){Box(Modifier.padding(16.dp)){Text("Elevated")}} } }
                item { Section("component-carousel", "Carousel") { LazyRow(horizontalArrangement=Arrangement.spacedBy(10.dp),modifier=Modifier.widthIn(max=520.dp)){items((1..4).toList()){n->Card(Modifier.size(150.dp,96.dp)){Box(Modifier.fillMaxSize(),contentAlignment=Alignment.Center){Text("0$n")}}}} } }
                item { Section("component-dialogs", "Dialogs") { OutlinedButton(onClick={showDialog=true}){Text("Open dialog")} } }
                item { Section("component-divider", "Divider") { Column(Modifier.fillMaxWidth()){HorizontalDivider();Spacer(Modifier.height(16.dp));HorizontalDivider(Modifier.padding(start=48.dp))} } }
                item { Section("component-lists", "List") { Column(Modifier.fillMaxWidth()){ListItem(headlineContent={Text("Single-line list")});ListItem(headlineContent={Text("Two-line list")},supportingContent={Text("Supporting text")})} } }
                item { Section("component-side-sheets", "Side sheet") { Surface(Modifier.width(280.dp),shape=RoundedCornerShape(topStart=28.dp,bottomStart=28.dp),tonalElevation=2.dp){Column(Modifier.padding(20.dp)){Text("Side sheet",fontWeight=FontWeight.SemiBold);Text("Supporting information")}} } }
                item { Section("component-bottom-app-bar", "Bottom app bar") { BottomAppBar(actions={TextButton(onClick={}){Text("Menu")};TextButton(onClick={}){Text("Search")}},floatingActionButton={FloatingActionButton(onClick={}){Text("+")}}) } }
                item { Section("component-top-app-bar", "Top app bar") { TopAppBar(title={Text("Page title")},navigationIcon={TextButton(onClick={}){Text("←")}},actions={TextButton(onClick={}){Text("⋯")}}) } }
                item { Section("component-navigation-bar", "Navigation bar") { var sel by remember{mutableIntStateOf(0)};NavigationBar{listOf("Home","Saved","Settings").forEachIndexed{i,l->NavigationBarItem(selected=sel==i,onClick={sel=i},icon={Text(if(i==0)"⌂" else if(i==1)"☆" else "⚙")},label={Text(l)})}} } }
                item { Section("component-navigation-drawer", "Navigation drawer") { Column(Modifier.width(260.dp)){NavigationDrawerItem(label={Text("Inbox")},selected=true,onClick={});NavigationDrawerItem(label={Text("Drafts")},selected=false,onClick={});NavigationDrawerItem(label={Text("Archive")},selected=false,onClick={})} } }
                item { Section("component-navigation-rail", "Navigation rail") { NavigationRail{NavigationRailItem(selected=true,onClick={},icon={Text("⌂")},label={Text("Home")});NavigationRailItem(selected=false,onClick={},icon={Text("☆")},label={Text("Saved")})} } }
                item { Section("component-search", "Search") { OutlinedTextField(value="",onValueChange={},placeholder={Text("Search")},leadingIcon={Text("⌕")},shape=CircleShape,modifier=Modifier.widthIn(max=480.dp)) } }
                item { Section("component-tabs", "Tabs") { var tab by remember{mutableIntStateOf(0)};TabRow(selectedTabIndex=tab){listOf("Overview","Activity","Settings").forEachIndexed{i,l->Tab(selected=tab==i,onClick={tab=i},text={Text(l)})}} } }
                item { Section("component-checkbox", "Checkbox") { var a by remember{mutableStateOf(false)};var b by remember{mutableStateOf(true)};Row(verticalAlignment=Alignment.CenterVertically){Checkbox(a,{a=it});Text("Not selected")};Row(verticalAlignment=Alignment.CenterVertically){Checkbox(b,{b=it});Text("Selected")};TriStateCheckbox(state=androidx.compose.ui.state.ToggleableState.Indeterminate,onClick={}) } }
                item { Section("component-chips", "Chips") { AssistChip(onClick={},label={Text("Assist")});FilterChip(selected=true,onClick={},label={Text("Filter")});InputChip(selected=false,onClick={},label={Text("Input")});SuggestionChip(onClick={},label={Text("Suggestion")}) } }
                item { Section("component-date-pickers", "Date picker") { val state=rememberDatePickerState();DatePicker(state=state,modifier=Modifier.widthIn(max=420.dp)) } }
                item { Section("component-menus", "Menu") { var open by remember{mutableStateOf(false)};Box{OutlinedButton(onClick={open=true}){Text("Menu")};DropdownMenu(expanded=open,onDismissRequest={open=false}){DropdownMenuItem(text={Text("Copy")},onClick={open=false});DropdownMenuItem(text={Text("Move")},onClick={open=false});DropdownMenuItem(text={Text("Delete")},onClick={open=false})}} } }
                item { Section("component-radio-button", "Radio button") { var sel by remember{mutableIntStateOf(0)};Row{listOf("System","Light","Dark").forEachIndexed{i,l->Row(verticalAlignment=Alignment.CenterVertically){RadioButton(selected=sel==i,onClick={sel=i});Text(l)}}} } }
                item { Section("component-sliders", "Slider") { var v by remember{mutableFloatStateOf(.42f)};Slider(value=v,onValueChange={v=it});var r by remember{mutableStateOf(0.25f..0.75f)};RangeSlider(value=r,onValueChange={r=it}) } }
                item { Section("component-switch", "Switch") { var on by remember{mutableStateOf(true)};Switch(checked=on,onCheckedChange={on=it});Text(if(on)"Notifications on" else "Notifications off") } }
                item { Section("component-time-pickers", "Time picker") { TimePicker(state=rememberTimePickerState(initialHour=9,initialMinute=30),modifier=Modifier.widthIn(max=360.dp)) } }
                item { Section("component-text-fields", "Text fields") { OutlinedTextField(value="Text",onValueChange={},label={Text("Outlined")});TextField(value="Text",onValueChange={},label={Text("Filled")}) } }
            }
        }
        if (showDialog) AlertDialog(onDismissRequest={showDialog=false},title={Text("Confirm action")},text={Text("Basic Dialog example")},confirmButton={TextButton(onClick={showDialog=false}){Text("Confirm")}},dismissButton={TextButton(onClick={showDialog=false}){Text("Cancel")}})
        if (showSheet) ModalBottomSheet(onDismissRequest={showSheet=false}) { Column(Modifier.fillMaxWidth().padding(24.dp),verticalArrangement=Arrangement.spacedBy(16.dp)){Text("Bottom sheet",style=MaterialTheme.typography.titleLarge);Text("Supporting content and actions");Button(onClick={showSheet=false}){Text("Done")};Spacer(Modifier.height(24.dp))} }
    }
}

@Composable
private fun Section(id:String,title:String,content:@Composable ()->Unit){
    ElevatedCard(modifier=Modifier.fillMaxWidth().semantics{contentDescription=id}){
        Column(Modifier.fillMaxWidth().padding(20.dp),verticalArrangement=Arrangement.spacedBy(14.dp)){
            Text(title,style=MaterialTheme.typography.titleLarge)
            Text(id,style=MaterialTheme.typography.labelSmall,color=MaterialTheme.colorScheme.onSurfaceVariant)
            content()
        }
    }
}
