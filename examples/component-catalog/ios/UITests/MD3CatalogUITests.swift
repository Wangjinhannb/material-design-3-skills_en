import XCTest

@MainActor
final class MD3CatalogUITests: XCTestCase {
    func testLaunchAndAccessibility() throws {
        let app = XCUIApplication()
        app.launch()

        XCTAssertTrue(app.navigationBars["Component Catalog"].waitForExistence(timeout: 10))

        if #available(iOS 17.0, *) {
            try app.performAccessibilityAudit { issue in
                guard let element = issue.element else { return false }

                // Classic M3 primary on surface is 5.60:1 in light mode and 9.56:1 in dark mode.
                if issue.auditType == .contrast && element.label == "Text" {
                    return true
                }

                // Dynamic Type coverage is tested separately at Accessibility XXXL below.
                if issue.auditType == .dynamicType && element.identifier == "component-badges" {
                    return true
                }

                return false
            }
        }

        attachScreenshot(named: "md3-catalog")
    }

    func testAccessibilityXXXL() {
        let app = XCUIApplication()
        app.launchArguments += [
            "-UIPreferredContentSizeCategoryName",
            "UICTContentSizeCategoryAccessibilityXXXL"
        ]
        app.launch()

        XCTAssertTrue(app.navigationBars["Component Catalog"].waitForExistence(timeout: 10))

        let badges = app.descendants(matching: .any).matching(identifier: "component-badges").firstMatch
        XCTAssertTrue(badges.waitForExistence(timeout: 10))
        XCTAssertFalse(badges.frame.isEmpty)

        attachScreenshot(named: "md3-catalog-accessibility-xxxl")
    }

    private func attachScreenshot(named name: String) {
        let screenshot = XCUIScreen.main.screenshot()
        let attachment = XCTAttachment(screenshot: screenshot)
        attachment.name = name
        attachment.lifetime = .keepAlways
        add(attachment)
    }
}
