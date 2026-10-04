import SwiftUI

private let primary = Color(red: 0.404, green: 0.314, blue: 0.643)
private let primaryContainer = Color(red: 0.918, green: 0.867, blue: 1.0)
private let secondaryContainer = Color(red: 0.910, green: 0.875, blue: 0.941)
private let surfaceContainer = Color(red: 0.949, green: 0.929, blue: 0.953)
private let outline = Color(red: 0.475, green: 0.455, blue: 0.494)
private let onSurfaceVariant = Color(red: 0.286, green: 0.271, blue: 0.310)

struct CatalogView: View {
    @State private var showDialog = false
    @State private var showSheet = false
    @State private var selectedSegment = 0
    @State private var selectedTab = 0
    @State private var checked = true
    @State private var selectedRadio = 0
    @State private var slider = 0.42
    @State private var search = ""
    @State private var field = "Text"
    @State private var date = Date()


    var body: some View {
        NavigationStack {
            ScrollView {
                LazyVStack(spacing: 14) {
                    primarySections
                    navigationSections
                    inputSections
                }
                .padding(20)
            }
            .navigationTitle("MD3 Component Catalog")
            .navigationBarTitleDisplayMode(.inline)
        }
        .alert("Confirm action", isPresented: $showDialog) {
            Button("Cancel", role: .cancel) {}
            Button("Confirm") {}
        } message: {
            Text("Basic Dialog example")
        }
        .sheet(isPresented: $showSheet) {
            VStack(alignment: .leading, spacing: 16) {
                Capsule().fill(outline).frame(width: 32, height: 4).frame(maxWidth: .infinity)
                Text("Bottom sheet").font(.title2)
                Text("Supporting content and actions")
                M3Button("Done", filled: true, action: { showSheet = false })
                Spacer()
            }
            .padding(24)
            .presentationDetents([.medium])
        }
    }

    @ViewBuilder private var primarySections: some View {
        section("component-buttons", "Buttons") { HStack { M3Button("Filled", filled: true); M3Button("Tonal", tonal: true); M3Button("Outlined", outlined: true); M3Button("Text") } }
        section("component-floating-action-button", "Floating action button") { HStack { CircleButton("+"); CircleButton("+"); CircleButton("+"); M3Button("＋ New", tonal: true) } }
        section("component-icon-buttons", "Icon buttons") { HStack { CircleButton("☆"); CircleButton("★",filled:true); CircleButton("⋯",tonal:true); CircleButton("✎",outlined:true) } }
        section("component-segmented-buttons", "Segmented buttons") { Picker("view", selection:$selectedSegment) { Text("List").tag(0);Text("Grid").tag(1);Text("Compact").tag(2) }.pickerStyle(.segmented) }
        section("component-badges", "Badges") { HStack { Text("Messages").overlay(alignment:.topTrailing){Circle().fill(.red).frame(width:8,height:8).offset(x:7,y:-5)}; Text("12").font(.caption2.bold()).padding(.horizontal,7).frame(height:24).background(.red).foregroundStyle(.white).clipShape(Capsule()) } }
        section("component-progress-indicators", "Progress indicators") { VStack(alignment:.leading){ProgressView(value:0.62).tint(primary);ProgressView().tint(primary)} }
        section("component-snackbars", "Snackbar") { HStack { Text("Settings saved"); Spacer(); Button("Undo"){} }.padding().background(Color.primary.opacity(0.9)).foregroundStyle(Color(.systemBackground)).clipShape(RoundedRectangle(cornerRadius:4)) }
        section("component-tooltips", "Tooltips") { Text("Long press or hover uses the platform help affordance").font(.callout).padding(10).background(Color.primary.opacity(0.9)).foregroundStyle(Color(.systemBackground)).clipShape(RoundedRectangle(cornerRadius:4)) }
        section("component-bottom-sheets", "Bottom sheet") { M3Button("Open sheet", outlined:true, action:{showSheet=true}) }
        section("component-cards", "Cards") { HStack { M3Card("Filled");M3Card("Outlined",outlined:true);M3Card("Elevated",elevated:true) } }
        section("component-carousel", "Carousel") { ScrollView(.horizontal){HStack{ForEach(1...4,id:\.self){n in Text(String(format:"%02d",n)).font(.title2).frame(width:150,height:96).background(primaryContainer).clipShape(RoundedRectangle(cornerRadius:20))}}}.scrollIndicators(.hidden) }
        section("component-dialogs", "Dialogs") { M3Button("Open dialog",outlined:true,action:{showDialog=true}) }
        section("component-divider", "Divider") { VStack{Divider();Divider().padding(.leading,48)} }
        section("component-lists", "List") { VStack(spacing:0){ListRow("Single-line list");ListRow("Two-line list",subtitle:"Supporting text")} }
    }

    @ViewBuilder private var navigationSections: some View {
        section("component-side-sheets", "Side sheet") { HStack { Spacer(); VStack(alignment:.leading){Text("Side sheet").font(.headline);Text("Supporting information")}.padding().frame(width:260,alignment:.leading).background(surfaceContainer).clipShape(UnevenRoundedRectangle(topLeadingRadius:28,bottomLeadingRadius:28)) } }
        section("component-bottom-app-bar", "Bottom app bar") { HStack { CircleButton("☰");CircleButton("⌕");Spacer();CircleButton("+",tonal:true) }.padding(8).background(surfaceContainer).clipShape(RoundedRectangle(cornerRadius:18)) }
        section("component-top-app-bar", "Top app bar") { HStack { CircleButton("←");Text("Page title").font(.headline);Spacer();CircleButton("⋯") }.padding(8).background(surfaceContainer).clipShape(RoundedRectangle(cornerRadius:18)) }
        section("component-navigation-bar", "Navigation bar") { HStack { NavItem("⌂","Home",selected:true);NavItem("☆","Saved");NavItem("⚙","Settings") }.padding(8).background(surfaceContainer).clipShape(RoundedRectangle(cornerRadius:18)) }
        section("component-navigation-drawer", "Navigation drawer") { VStack(alignment:.leading){DrawerItem("Inbox",selected:true);DrawerItem("Drafts");DrawerItem("Archive")}.frame(maxWidth:260,alignment:.leading) }
        section("component-navigation-rail", "Navigation rail") { HStack { NavItem("⌂","Home",selected:true);NavItem("☆","Saved");NavItem("⚙","Settings") }.padding(8).background(surfaceContainer).clipShape(RoundedRectangle(cornerRadius:18)) }
        section("component-search", "Search") { HStack{Image(systemName:"magnifyingglass");TextField("Search",text:$search)}.padding(.horizontal,18).frame(height:56).background(surfaceContainer).clipShape(Capsule()) }
        section("component-tabs", "Tabs") { Picker("Tag",selection:$selectedTab){Text("Overview").tag(0);Text("Activity").tag(1);Text("Settings").tag(2)}.pickerStyle(.segmented) }
        section("component-checkbox", "Checkbox") { Toggle("Selected",isOn:$checked).toggleStyle(.checkboxLike) }
    }

    @ViewBuilder private var inputSections: some View {
        section("component-chips", "Chips") { HStack { Chip("Assist");Chip("Filter",selected:true);Chip("Input ×");Chip("Suggestion") } }
        section("component-date-pickers", "Date picker") { DatePicker("Date",selection:$date,displayedComponents:.date).datePickerStyle(.compact) }
        section("component-menus", "Menu") { Menu("Menu") { Button("Copy"){};Button("Move"){};Button("Delete",role:.destructive){} }.buttonStyle(M3OutlineButtonStyle()) }
        section("component-radio-button", "Radio button") {
                    HStack {
                        ForEach(Array(["System", "Light", "Dark"].enumerated()), id: \.offset) { index, label in
                            Button { selectedRadio = index } label: {
                                HStack {
                                    Image(systemName: selectedRadio == index ? "circle.inset.filled" : "circle")
                                    Text(label)
                                }
                            }
                            .foregroundStyle(primary)
                        }
                    }
                }
        section("component-sliders", "Slider") { Slider(value:$slider).tint(primary) }
        section("component-switch", "Switch") { Toggle("Notifications",isOn:$checked).tint(primary) }
        section("component-time-pickers", "Time picker") { DatePicker("Time",selection:$date,displayedComponents:.hourAndMinute).datePickerStyle(.compact) }
        section("component-text-fields", "Text fields") { VStack { TextField("Filled",text:$field).padding(14).background(surfaceContainer).clipShape(RoundedRectangle(cornerRadius:4));TextField("Outlined",text:$field).padding(14).overlay(RoundedRectangle(cornerRadius:4).stroke(outline)) } }
    }

    @ViewBuilder private func section<Content:View>(_ id:String,_ title:String,@ViewBuilder content:()->Content)->some View {
        VStack(alignment:.leading,spacing:14){Text(title).font(.title3.weight(.semibold));Text(id).font(.caption).foregroundStyle(onSurfaceVariant);content()}
            .padding(20).frame(maxWidth:.infinity,alignment:.leading).background(surfaceContainer.opacity(0.7)).clipShape(RoundedRectangle(cornerRadius:20)).accessibilityIdentifier(id)
    }
}

private struct M3Button: View {
    let text: String
    var filled = false
    var tonal = false
    var outlined = false
    var action: () -> Void = {}

    init(_ text: String, filled: Bool = false, tonal: Bool = false, outlined: Bool = false, action: @escaping () -> Void = {}) {
        self.text = text
        self.filled = filled
        self.tonal = tonal
        self.outlined = outlined
        self.action = action
    }

    var body: some View {
        Button(text, action: action)
            .buttonStyle(M3ButtonStyle(filled: filled, tonal: tonal, outlined: outlined))
    }
}

private struct M3ButtonStyle: ButtonStyle {
    let filled: Bool
    let tonal: Bool
    let outlined: Bool

    func makeBody(configuration: Configuration) -> some View {
        configuration.label
            .font(.body.weight(.medium))
            .padding(.horizontal, 20)
            .frame(minHeight: 40)
            .background(filled ? primary : tonal ? secondaryContainer : Color.clear)
            .foregroundStyle(filled ? Color.white : primary)
            .clipShape(Capsule())
            .overlay(Capsule().stroke(outlined ? outline : .clear))
            .opacity(configuration.isPressed ? 0.84 : 1)
    }
}

private struct M3OutlineButtonStyle: ButtonStyle {
    func makeBody(configuration: Configuration) -> some View {
        configuration.label
            .padding(.horizontal, 20)
            .frame(minHeight: 40)
            .foregroundStyle(primary)
            .overlay(Capsule().stroke(outline))
    }
}

private struct CircleButton: View {
    let label: String
    var filled = false
    var tonal = false
    var outlined = false

    init(_ label: String, filled: Bool = false, tonal: Bool = false, outlined: Bool = false) {
        self.label = label
        self.filled = filled
        self.tonal = tonal
        self.outlined = outlined
    }

    var body: some View {
        Button(action: {}) {
            Text(label)
                .frame(width: 48, height: 48)
                .contentShape(Rectangle())
        }
        .background(filled ? primary : tonal ? secondaryContainer : .clear)
        .foregroundStyle(filled ? .white : primary)
        .clipShape(Circle())
        .overlay(Circle().stroke(outlined ? outline : .clear))
    }
}

private struct M3Card: View {
    let title: String
    var outlined = false
    var elevated = false

    init(_ title: String, outlined: Bool = false, elevated: Bool = false) {
        self.title = title
        self.outlined = outlined
        self.elevated = elevated
    }

    var body: some View {
        VStack(alignment: .leading) {
            Text(title).font(.headline)
            Text("Related content")
        }
        .padding()
        .frame(width: 145, height: 100, alignment: .leading)
        .background(outlined ? Color.clear : surfaceContainer)
        .clipShape(RoundedRectangle(cornerRadius: 12))
        .overlay(RoundedRectangle(cornerRadius: 12).stroke(outlined ? outline : .clear))
        .shadow(color: .black.opacity(elevated ? 0.15 : 0), radius: 3, y: 1)
    }
}

private struct ListRow: View {
    let title: String
    var subtitle: String?

    init(_ title: String, subtitle: String? = nil) {
        self.title = title
        self.subtitle = subtitle
    }

    var body: some View {
        HStack {
            Circle()
                .fill(secondaryContainer)
                .frame(width: 40, height: 40)
                .overlay(Text(String(title.prefix(1))))
            VStack(alignment: .leading) {
                Text(title)
                if let subtitle {
                    Text(subtitle).font(.caption).foregroundStyle(.secondary)
                }
            }
            Spacer()
        }
        .padding(.vertical, 8)
    }
}

private struct NavItem: View {
    let icon: String
    let title: String
    var selected = false

    init(_ icon: String, _ title: String, selected: Bool = false) {
        self.icon = icon
        self.title = title
        self.selected = selected
    }

    var body: some View {
        VStack(spacing: 4) {
            Text(icon)
                .padding(.horizontal, 14)
                .padding(.vertical, 4)
                .background(selected ? secondaryContainer : .clear)
                .clipShape(Capsule())
            Text(title).font(.caption)
        }
    }
}

private struct DrawerItem: View {
    let title: String
    var selected = false

    init(_ title: String, selected: Bool = false) {
        self.title = title
        self.selected = selected
    }

    var body: some View {
        Text(title)
            .padding(.horizontal, 16)
            .frame(maxWidth: .infinity, minHeight: 48, alignment: .leading)
            .background(selected ? secondaryContainer : .clear)
            .clipShape(Capsule())
    }
}

private struct Chip: View {
    let title: String
    var selected = false

    init(_ title: String, selected: Bool = false) {
        self.title = title
        self.selected = selected
    }

    var body: some View {
        Text(title)
            .font(.callout)
            .padding(.horizontal, 12)
            .frame(height: 32)
            .background(selected ? secondaryContainer : .clear)
            .overlay(RoundedRectangle(cornerRadius: 8).stroke(selected ? .clear : outline))
    }
}

private struct CheckboxToggleStyle: ToggleStyle {
    func makeBody(configuration: Configuration) -> some View {
        Button { configuration.isOn.toggle() } label: {
            HStack {
                Image(systemName: configuration.isOn ? "checkmark.square.fill" : "square")
                    .foregroundStyle(primary)
                configuration.label
            }
        }
    }
}

private extension ToggleStyle where Self == CheckboxToggleStyle {
    static var checkboxLike: CheckboxToggleStyle { CheckboxToggleStyle() }
}
