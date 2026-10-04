import SwiftUI
import UIKit

private func adaptiveColor(
    light: (Double, Double, Double),
    dark: (Double, Double, Double)
) -> Color {
    Color(uiColor: UIColor { traits in
        let value = traits.userInterfaceStyle == .dark ? dark : light
        return UIColor(red: value.0, green: value.1, blue: value.2, alpha: 1)
    })
}

private let primary = adaptiveColor(
    light: (103.0 / 255.0, 80.0 / 255.0, 164.0 / 255.0),
    dark: (208.0 / 255.0, 188.0 / 255.0, 1.0)
)
private let primaryContainer = adaptiveColor(
    light: (234.0 / 255.0, 221.0 / 255.0, 1.0),
    dark: (79.0 / 255.0, 55.0 / 255.0, 139.0 / 255.0)
)
private let secondaryContainer = adaptiveColor(
    light: (232.0 / 255.0, 222.0 / 255.0, 248.0 / 255.0),
    dark: (74.0 / 255.0, 68.0 / 255.0, 88.0 / 255.0)
)
private let surfaceContainer = adaptiveColor(
    light: (243.0 / 255.0, 237.0 / 255.0, 247.0 / 255.0),
    dark: (33.0 / 255.0, 31.0 / 255.0, 38.0 / 255.0)
)
private let outline = adaptiveColor(
    light: (121.0 / 255.0, 116.0 / 255.0, 126.0 / 255.0),
    dark: (147.0 / 255.0, 143.0 / 255.0, 153.0 / 255.0)
)
private let onSurfaceVariant = adaptiveColor(
    light: (73.0 / 255.0, 69.0 / 255.0, 79.0 / 255.0),
    dark: (202.0 / 255.0, 196.0 / 255.0, 208.0 / 255.0)
)
private let onSecondaryContainer = adaptiveColor(
    light: (29.0 / 255.0, 25.0 / 255.0, 43.0 / 255.0),
    dark: (232.0 / 255.0, 222.0 / 255.0, 248.0 / 255.0)
)
private let error = adaptiveColor(
    light: (179.0 / 255.0, 38.0 / 255.0, 30.0 / 255.0),
    dark: (242.0 / 255.0, 184.0 / 255.0, 181.0 / 255.0)
)
private let inverseSurface = adaptiveColor(
    light: (50.0 / 255.0, 47.0 / 255.0, 53.0 / 255.0),
    dark: (230.0 / 255.0, 224.0 / 255.0, 233.0 / 255.0)
)
private let inverseOnSurface = adaptiveColor(
    light: (245.0 / 255.0, 239.0 / 255.0, 247.0 / 255.0),
    dark: (50.0 / 255.0, 47.0 / 255.0, 53.0 / 255.0)
)

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
            .navigationTitle("Component Catalog")
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
        section("component-buttons", "Buttons") { HorizontalRow { M3Button("Filled", filled: true); M3Button("Tonal", tonal: true); M3Button("Outlined", outlined: true); M3Button("Text") } }
        section("component-floating-action-button", "Floating action button") { HorizontalRow { CircleButton("+"); CircleButton("+"); CircleButton("+"); M3Button("＋ New", tonal: true) } }
        section("component-icon-buttons", "Icon buttons") { HorizontalRow { CircleButton("☆"); CircleButton("★",filled:true); CircleButton("⋯",tonal:true); CircleButton("✎",outlined:true) } }
        section("component-segmented-buttons", "Segmented buttons") { M3SegmentedControl(labels: ["List", "Grid", "Compact"], selection: $selectedSegment) }
        section("component-badges", "Badges") { HStack { Text("Messages").overlay(alignment:.topTrailing){Circle().fill(error).frame(width:8,height:8).offset(x:7,y:-5)}; Text("12").font(.body.weight(.semibold)).padding(.horizontal,8).padding(.vertical,4).background(error).foregroundStyle(.white).clipShape(Capsule()) } }
        section("component-progress-indicators", "Progress indicators") {
            VStack(alignment: .leading) {
                ProgressView(value: 0.62) { Text("Progress") }.tint(primary)
                ProgressView("Loading").tint(primary)
            }
        }
        section("component-snackbars", "Snackbar") {
            HStack {
                Text("Settings saved")
                Spacer()
                Button("Undo") {}
            }
            .padding()
            .background(inverseSurface)
            .foregroundStyle(inverseOnSurface)
            .clipShape(RoundedRectangle(cornerRadius: 4))
        }
        section("component-tooltips", "Tooltips") {
            Text("Long press or hover uses the platform help affordance")
                .font(.callout)
                .padding(10)
                .background(inverseSurface)
                .foregroundStyle(inverseOnSurface)
                .clipShape(RoundedRectangle(cornerRadius: 4))
        }
        section("component-bottom-sheets", "Bottom sheet") { M3Button("Open sheet", outlined:true, action:{showSheet=true}) }
        section("component-cards", "Cards") { HorizontalRow { M3Card("Filled");M3Card("Outlined",outlined:true);M3Card("Elevated",elevated:true) } }
        section("component-carousel", "Carousel") { ScrollView(.horizontal){HStack{ForEach(1...4,id:\.self){n in Text(String(format:"%02d",n)).font(.title2).frame(width:150,height:96).background(primaryContainer).clipShape(RoundedRectangle(cornerRadius:20))}}}.scrollIndicators(.hidden) }
        section("component-dialogs", "Dialogs") { M3Button("Open dialog",outlined:true,action:{showDialog=true}) }
        section("component-divider", "Divider") { VStack{Divider();Divider().padding(.leading,48)} }
        section("component-lists", "List") { VStack(spacing:0){ListRow("Single-line list");ListRow("Two-line list",subtitle:"Supporting text")} }
    }

    @ViewBuilder private var navigationSections: some View {
        section("component-side-sheets", "Side sheet") { HStack { Spacer(); VStack(alignment:.leading){Text("Side sheet").font(.headline);Text("Supporting information")}.padding().frame(width:260,alignment:.leading).background(surfaceContainer).clipShape(UnevenRoundedRectangle(topLeadingRadius:28,bottomLeadingRadius:28)) } }
        section("component-bottom-app-bar", "Bottom app bar") { HorizontalRow { CircleButton("☰");CircleButton("⌕");Spacer(minLength:24);CircleButton("+",tonal:true) }.padding(8).background(surfaceContainer).clipShape(RoundedRectangle(cornerRadius:18)) }
        section("component-top-app-bar", "Top app bar") { HorizontalRow { CircleButton("←");Text("Page title").font(.headline);Spacer(minLength:24);CircleButton("⋯") }.padding(8).background(surfaceContainer).clipShape(RoundedRectangle(cornerRadius:18)) }
        section("component-navigation-bar", "Navigation bar") { HorizontalRow { NavItem("⌂","Home",selected:true);NavItem("☆","Saved");NavItem("⚙","Settings") }.padding(8).background(surfaceContainer).clipShape(RoundedRectangle(cornerRadius:18)) }
        section("component-navigation-drawer", "Navigation drawer") { VStack(alignment:.leading){DrawerItem("Inbox",selected:true);DrawerItem("Drafts");DrawerItem("Archive")}.frame(maxWidth:260,alignment:.leading) }
        section("component-navigation-rail", "Navigation rail") { HorizontalRow { NavItem("⌂","Home",selected:true);NavItem("☆","Saved");NavItem("⚙","Settings") }.padding(8).background(surfaceContainer).clipShape(RoundedRectangle(cornerRadius:18)) }
        section("component-search", "Search") {
            HStack {
                Image(systemName: "magnifyingglass").accessibilityHidden(true)
                TextField("Search", text: $search)
            }
            .padding(.horizontal, 18)
            .frame(minHeight: 56)
            .background(surfaceContainer)
            .clipShape(Capsule())
        }
        section("component-tabs", "Tabs") { M3SegmentedControl(labels: ["Overview", "Activity", "Settings"], selection: $selectedTab) }
        section("component-checkbox", "Checkbox") { Toggle("Selected",isOn:$checked).toggleStyle(.checkboxLike) }
    }

    @ViewBuilder private var inputSections: some View {
        section("component-chips", "Chips") { HorizontalRow { Chip("Assist");Chip("Filter",selected:true);Chip("Input ×");Chip("Suggestion") } }
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
                            .frame(minHeight: 44)
                        }
                    }
                }
        section("component-sliders", "Slider") {
            Slider(value: $slider, in: 0...1) {
                Text("Value")
            }
            .tint(primary)
        }
        section("component-switch", "Switch") { Toggle("Notifications",isOn:$checked).tint(primary) }
        section("component-time-pickers", "Time picker") { DatePicker("Time",selection:$date,displayedComponents:.hourAndMinute).datePickerStyle(.compact) }
        section("component-text-fields", "Text fields") { VStack { TextField("Filled",text:$field).padding(14).background(surfaceContainer).clipShape(RoundedRectangle(cornerRadius:4));TextField("Outlined",text:$field).padding(14).overlay(RoundedRectangle(cornerRadius:4).stroke(outline)) } }
    }

    @ViewBuilder private func section<Content:View>(_ id:String,_ title:String,@ViewBuilder content:()->Content)->some View {
        VStack(alignment:.leading,spacing:14){Text(title).font(.title3.weight(.semibold));content()}
            .padding(20).frame(maxWidth:.infinity,alignment:.leading).background(surfaceContainer).clipShape(RoundedRectangle(cornerRadius:20)).accessibilityIdentifier(id)
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
            .tint(primary)
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
            .frame(minHeight: 48)
            .background(filled ? primary : tonal ? secondaryContainer : Color.clear)
            .foregroundStyle(filled ? Color.white : tonal ? onSecondaryContainer : primary)
            .clipShape(Capsule())
            .overlay(Capsule().stroke(outlined ? outline : .clear))
            .opacity(configuration.isPressed ? 0.84 : 1)
    }
}

private struct M3OutlineButtonStyle: ButtonStyle {
    func makeBody(configuration: Configuration) -> some View {
        configuration.label
            .padding(.horizontal, 20)
            .frame(minHeight: 48)
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
        .tint(primary)
        .background(filled ? primary : tonal ? secondaryContainer : .clear)
        .foregroundStyle(filled ? .white : tonal ? onSecondaryContainer : primary)
        .clipShape(Circle())
        .overlay(Circle().stroke(outlined ? outline : .clear))
        .accessibilityLabel(accessibilityName)
    }

    private var accessibilityName: String {
        switch label {
        case "+": return "Add"
        case "☆": return "Favorite"
        case "★": return "Favorite selected"
        case "⋯": return "More options"
        case "✎": return "Edit"
        case "☰": return "Menu"
        case "⌕": return "Search"
        case "←": return "Back"
        default: return label
        }
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
        .frame(width: 145, alignment: .leading)
        .frame(minHeight: 100, alignment: .leading)
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
                    Text(subtitle).font(.caption).foregroundStyle(onSurfaceVariant)
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
            .padding(.vertical, 8)
            .frame(minHeight: 32)
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

private struct HorizontalRow<Content: View>: View {
    @ViewBuilder let content: () -> Content

    var body: some View {
        ScrollView(.horizontal) {
            HStack(spacing: 10) {
                content()
            }
        }
        .scrollIndicators(.hidden)
    }
}

private struct M3SegmentedControl: View {
    let labels: [String]
    @Binding var selection: Int

    var body: some View {
        HorizontalRow {
            ForEach(Array(labels.enumerated()), id: \.offset) { index, label in
                Button {
                    selection = index
                } label: {
                    Text(label)
                        .font(.body.weight(.medium))
                        .padding(.horizontal, 16)
                        .frame(minHeight: 48)
                        .fixedSize(horizontal: true, vertical: false)
                }
                .foregroundStyle(selection == index ? onSecondaryContainer : primary)
                .background(selection == index ? secondaryContainer : Color.clear)
                .clipShape(Capsule())
                .overlay(Capsule().stroke(selection == index ? Color.clear : outline))
                .accessibilityAddTraits(selection == index ? .isSelected : [])
            }
        }
    }
}
