import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {
    id: root
    width: 1100
    height: 900
    visible: true
    title: "MD3 Component Catalog"

    ScrollView {
        anchors.fill: parent
        ColumnLayout {
            width: Math.min(root.width - 48, 1080)
            anchors.horizontalCenter: parent.horizontalCenter
            spacing: 14

            Label { text: "Classic Material Design 3"; color: "#6750A4" }
            Label { text: "31-component catalog"; font.pixelSize: 32 }

            GroupBox { Layout.fillWidth: true; title: "Buttons · component-buttons"; RowLayout { Button { text: "Filled" } Button { text: "Outlined"; flat: true } } }
            GroupBox { Layout.fillWidth: true; title: "Floating action button · component-floating-action-button"; Button { text: "+" } }
            GroupBox { Layout.fillWidth: true; title: "Icon buttons · component-icon-buttons"; RowLayout { RoundButton { text: "★" } RoundButton { text: "⋮" } } }
            GroupBox { Layout.fillWidth: true; title: "Segmented buttons · component-segmented-buttons"; RowLayout { Button { text: "Day"; checkable: true; checked: true } Button { text: "Week"; checkable: true } Button { text: "Month"; checkable: true } } }
            GroupBox { Layout.fillWidth: true; title: "Badges · component-badges"; RowLayout { Label { text: "●"; color: "#b3261e" } Label { text: "12"; color: "white"; padding: 6; background: Rectangle { color: "#b3261e"; radius: 12 } } } }
            GroupBox { Layout.fillWidth: true; title: "Progress indicators · component-progress-indicators"; ColumnLayout { ProgressBar { value: .65 } BusyIndicator { running: true } } }
            GroupBox { Layout.fillWidth: true; title: "Snackbar · component-snackbars"; Label { text: "Settings saved"; padding: 12; color: "white"; background: Rectangle { color: "#322f35"; radius: 4 } } }
            GroupBox { Layout.fillWidth: true; title: "Tooltip · component-tooltips"; Button { text: "Hover"; ToolTip.visible: hovered; ToolTip.text: "Description" } }
            GroupBox { Layout.fillWidth: true; title: "Bottom sheet · component-bottom-sheets"; Frame { Label { text: "Bottom sheet" } } }
            GroupBox { Layout.fillWidth: true; title: "Cards · component-cards"; Frame { Label { text: "Card content" } } }
            GroupBox { Layout.fillWidth: true; title: "Carousel · component-carousel"; RowLayout { Repeater { model: 3; Frame { Label { text: "Item " + (index + 1) } } } } }
            GroupBox { Layout.fillWidth: true; title: "Dialogs · component-dialogs"; Button { text: "Open dialog"; onClicked: dialog.open() } }
            GroupBox { Layout.fillWidth: true; title: "Divider · component-divider"; Rectangle { Layout.fillWidth: true; height: 1; color: "#79747e" } }
            GroupBox { Layout.fillWidth: true; title: "Lists · component-lists"; ColumnLayout { Label { text: "Item A" } Label { text: "Item B" } } }
            GroupBox { Layout.fillWidth: true; title: "Side sheet · component-side-sheets"; Frame { Label { text: "Supporting information" } } }
            GroupBox { Layout.fillWidth: true; title: "Bottom app bar · component-bottom-app-bar"; RowLayout { ToolButton { text: "⌂" } ToolButton { text: "☆" } } }
            GroupBox { Layout.fillWidth: true; title: "Top app bar · component-top-app-bar"; ToolBar { RowLayout { Label { text: "Title" } Item { Layout.fillWidth: true } ToolButton { text: "⋮" } } } }
            GroupBox { Layout.fillWidth: true; title: "Navigation bar · component-navigation-bar"; RowLayout { Button { text: "Home"; flat: true } Button { text: "Saved"; flat: true } } }
            GroupBox { Layout.fillWidth: true; title: "Navigation drawer · component-navigation-drawer"; ColumnLayout { Label { text: "Home" } Label { text: "Settings" } } }
            GroupBox { Layout.fillWidth: true; title: "Navigation rail · component-navigation-rail"; ColumnLayout { ToolButton { text: "⌂" } ToolButton { text: "☆" } } }
            GroupBox { Layout.fillWidth: true; title: "Search · component-search"; TextField { placeholderText: "Search" } }
            GroupBox { Layout.fillWidth: true; title: "Tabs · component-tabs"; TabBar { TabButton { text: "Overview" } TabButton { text: "Details" } } }
            GroupBox { Layout.fillWidth: true; title: "Checkbox · component-checkbox"; CheckBox { text: "Checkbox item"; checked: true } }
            GroupBox { Layout.fillWidth: true; title: "Chips · component-chips"; RowLayout { Button { text: "Filter"; checkable: true } Button { text: "Tag"; flat: true } } }
            GroupBox { Layout.fillWidth: true; title: "Date picker · component-date-pickers"; Label { text: "2026-10-03" } }
            GroupBox { Layout.fillWidth: true; title: "Menus · component-menus"; Button { text: "Menu"; onClicked: menu.open(); Menu { id: menu; MenuItem { text: "Edit" } MenuItem { text: "Delete" } } } }
            GroupBox { Layout.fillWidth: true; title: "Radio button · component-radio-button"; RadioButton { text: "Radio option"; checked: true } }
            GroupBox { Layout.fillWidth: true; title: "Sliders · component-sliders"; Slider { value: .45 } }
            GroupBox { Layout.fillWidth: true; title: "Switch · component-switch"; Switch { text: "Notifications"; checked: true } }
            GroupBox { Layout.fillWidth: true; title: "Text fields · component-text-fields"; TextField { placeholderText: "Display name" } }
            GroupBox { Layout.fillWidth: true; title: "Time picker · component-time-pickers"; Label { text: "12:30" } }
        }
    }

    Component.onCompleted: { if (Qt.application.arguments.indexOf("--smoke") >= 0) Qt.callLater(Qt.quit) }

    Dialog {
        id: dialog
        title: "Confirm action"
        standardButtons: Dialog.Ok | Dialog.Cancel
        Label { text: "Dialog content" }
    }
}
