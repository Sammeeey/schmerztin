import datetime
import telegram_send

from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://home.cgm-life.de/portal/#/appointment/?institution=013003348
    page.goto("https://home.cgm-life.de/portal/#/appointment/?institution=013003348")

    # Click button:has-text("Bitte wählen Sie eine Terminart") >> nth=0
    page.locator("button:has-text(\"Bitte wählen Sie eine Terminart\")").first.click()

    # Click text=Termine für Neupatienten Dr. Pioch >> nth=0
    page.locator("text=Termine für Neupatienten Dr. Pioch").first.click()


    # find first highlighted day number
    # selector: .dayhighlight
    most_recent_day = int(page.locator('.dayhighlight').first.inner_text())

    # find month of first highlighted day number
    # selector: .switch.ng-binding
    if page.locator('.switch.ng-binding:has-text("Juni")'):
        next_possible_appointment = datetime.date(2022,6,most_recent_day)
    if page.locator('.switch.ng-binding:has-text("Juli")'):
        next_possible_appointment = datetime.date(2022,7,most_recent_day)
    if page.locator('.switch.ng-binding:has-text("August")'):
        next_possible_appointment = datetime.date(2022,8,most_recent_day)
    if page.locator('.switch.ng-binding:has-text("September")'):
        next_possible_appointment = datetime.date(2022,9,most_recent_day)
    print(next_possible_appointment)

    # hardcoded earlier appointment (to test correct functionality of telegram bot)
    next_possible_appointment = datetime.date(2022,9,1)

    # create Python date equivalent for current appointment
    current_appointment = datetime.date(2022,9,2)


    # send appointment via telegram, if newer than comparison value
    if next_possible_appointment < current_appointment:
        telegram_send.send(messages=[f"Earlier appointment available at {next_possible_appointment}"])

    # ---------------------
    # page.pause()
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
