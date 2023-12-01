from playwright.sync_api import Page, Playwright, sync_playwright, expect


def test_enquire_hightest_price(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True, slow_mo=50)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://shop.mercedes-benz.com/en-au/shop/vehicle/srp/demo")
    page.get_by_role("button", name="Agree to all")

    page.get_by_label("* Your state").select_option("New South Wales")
    page.locator("[data-test-id=\"modal-popup__location\"]").get_by_label("", exact=True).fill("2007")

    page.locator("label").filter(has_text="Private").locator("div").click()
    page.locator("[data-test-id=\"state-selected-modal__close\"]").click()

    page.locator("button").filter(has_text="Pre-Owned").click()

    page.locator("xpath=//p[normalize-space()='Colour']").click()

    page.get_by_text("Colour 0").click()

    page.get_by_text("Black NonMetallic").click()

    expect(page.locator("[data-test-id=\"srp\"]")).to_contain_text("Mercedes-AMG GLC 43")

    # Sorting Price (descending)
    page.get_by_label("Sorting").select_option("price-desc-ucos")

    page.locator("h3").filter(has_text="Mercedes-AMG GLC").click()

    # Save car Model Year to a variable
    model_year = page.locator("[data-test-id=\"dcp-vehicle-details-list-item-1\"]").text_content()

    # Assert model year
    expect(page.locator("[data-test-id=\"dcp-vehicle-details-list-item-2\"]")).to_contain_text("2018")

    # Save car VIN to a variable
    vin_number = page.locator("[data-test-id=\"dcp-vehicle-details-list-item-10\"]").text_content()

    # Assert vin number
    expect(page.locator("[data-test-id=\"dcp-vehicle-details-list-item-10\"]")).to_contain_text("WDC2539642F296449")
    filename = 'car_info.txt'

    save_car_info_to_file(model_year, vin_number, filename)

    page.locator("xpath=//button[normalize-space()='Enquire Now']").click()
    page.get_by_label("First Name").click()
    page.get_by_label("First Name").fill("Homer")
    page.get_by_label("Last Name").fill("Simpson")
    page.get_by_label("E-Mail").fill("hsimpson@mail.com")
    page.locator("[data-test-id=\"rfq-contact__phone\"]").get_by_label("Phone").fill("0441234567")
    page.get_by_label("Postal Code").click()
    page.get_by_label("Postal Code").fill("2007")
    page.get_by_label("Comments (optional)").click()
    page.get_by_label("Comments (optional)").fill("Morning")
    page.locator("label").filter(has_text="I have read and understood").locator("wb-icon").click()
    page.locator("label").filter(has_text="Email").locator("wb-icon").click()
    page.locator("[data-test-id=\"dcp-rfq-contact-button-container__button-next\"]").click()
    expect(page.locator("h4")).to_contain_text("Contact data")
    expect(page.locator("[data-test-id=\"dcp-rfq-confirmation-section__label-first-last-name\"]")).to_contain_text(
        "Homer Simpson")
    expect(page.locator("[data-test-id=\"dcp-rfq-confirmation-section__label-email\"]")).to_contain_text(
        "hsimpson@mail.com")
    expect(page.locator("[data-test-id=\"dcp-rfq-confirmation-section__label-phone\"]")).to_contain_text("0441234567")
    page.locator("[data-test-id=\"dcp-rfq-confirmation-button-container__button\"]").click()
    page.get_by_text("Thank you for your enquiry in").click()

    # Validate message error
    expect(page.locator("[data-test-id=\"pdp\"]")).to_contain_text(
        "Thank you for your enquiry in your selected Mercedes-Benz! Your Mercedes-Benz retailer will get in touch with you within the next two hours. (Operating Hours 8am-8pm)")
    page.locator("[data-test-id=\"dcp-rfq-success-button-container__button\"]").click()

    context.close()
    browser.close()


def save_car_info_to_file(model_year, vin_number, filename):
    with open(filename, 'w') as file:
        file.write(str(model_year) + '\n')
        file.write(str(vin_number) + '\n')


filename = 'car_info.txt'
