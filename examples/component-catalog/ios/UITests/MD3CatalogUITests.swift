import XCTest
final class MD3CatalogUITests: XCTestCase {
    func testLaunchAndAccessibility() throws {
        let app = XCUIApplication(); app.launch()
        XCTAssertTrue(app.navigationBars["MD3 Component Catalog"].exists)
        if #available(iOS 17.0, *) { try app.performAccessibilityAudit() }
        let screenshot = XCUIScreen.main.screenshot()
        let attachment = XCTAttachment(screenshot: screenshot)
        attachment.name = "md3-catalog"
        attachment.lifetime = .keepAlways
        add(attachment)
    }
}
