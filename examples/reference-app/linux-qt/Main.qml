import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {
    id: root
    width: 820
    height: 700
    visible: true
    title: "MD3 Reference"

    ScrollView {
        anchors.fill: parent
        ColumnLayout {
            width: Math.min(root.width - 48, 900)
            anchors.horizontalCenter: parent.horizontalCenter
            spacing: 16

            Label { text: "Classic Material Design 3"; color: "#6750A4" }
            Label { text: "Cross-platform reference app"; font.pixelSize: 32 }
            Button { text: "Primary action"; objectName: "primary-action" }
            GroupBox {
                objectName: "reference-overview"
                title: "Overview"
                Layout.fillWidth: true
                RowLayout { Label { text: "Token" } Label { text: "Adaptive" } Label { text: "State" } }
            }
            GroupBox {
                objectName: "reference-list"
                title: "List"
                Layout.fillWidth: true
                ColumnLayout { Label { text: "Item A · Supporting information" } Label { text: "Item B · Supporting information" } }
            }
            GroupBox {
                objectName: "reference-form"
                title: "Form"
                Layout.fillWidth: true
                ColumnLayout {
                    TextField { placeholderText: "Display name"; text: "Material User"; objectName: "display-name" }
                    Switch { text: "Enable notifications"; checked: true; objectName: "notifications" }
                    Button { text: "Save"; objectName: "save-settings" }
                }
            }
            GroupBox {
                objectName: "reference-settings"
                title: "Settings"
                Layout.fillWidth: true
                Label { text: "Theme follows the system; content stays readable and operable as the window changes."; wrapMode: Text.WordWrap }
            }
        }
    }
}
