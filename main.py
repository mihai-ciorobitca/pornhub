import asyncio
from browser_manager import AsyncBrowserManager
from utils import get_username, get_verification_code
import time

async def sign_up(page, username, password):
    try:
        await page.goto("https://www.pornhub.com/")

        confirm_age_modal = page.locator('#modalWrapMTubes > div > div > button')
        if await confirm_age_modal.is_visible(timeout=5000):
            await confirm_age_modal.click()
        else:
            print("No age confirmation modal found.")

        cookie_btn = page.locator('#cookieBannerWrapper > button.cbSecondaryCTA.cbButton.gtm-event-cookie-banner')
        if await cookie_btn.is_visible(timeout=5000):
            await cookie_btn.click()
        else:
            print("No cookie banner found.")

        await page.reload(wait_until="load")

        header_btn = page.locator("#headerLoginLink.signIn")
        await header_btn.click()
        
        sign_up_btn = page.locator("#signUpBtn")
        await sign_up_btn.click()

        email_pass_btn = page.locator(".emailPassSignButton")
        await email_pass_btn.click()

        email_input = page.locator("#createEmail")
        await email_input.fill(username)

        password_input = page.locator("#originalPassword")
        await password_input.fill(password)

        sign_up_submit = page.locator("#js-signUpBtn")
        await sign_up_submit.click()

        await page.wait_for_url("**#email-verification-modal", wait_until="load")

        verification_inputs = page.locator(".verificationCodeWrapper .js_verificationCodeInput")
        verification_code = await get_verification_code(username.split("@")[0])
        for i, digit in enumerate(verification_code):
            await verification_inputs.nth(i).fill(digit)

        await page.wait_for_load_state("networkidle")

        dob_title = page.locator("text=Date of birth")
        try:
            await dob_title.wait_for(state="visible", timeout=5000)
            print("DOB modal detected")

            year_select = page.locator("#js_year")
            await year_select.select_option("1995")

            month_select = page.locator("#js_month")
            await month_select.select_option("1")

            day_select = page.locator("#js_day")
            await day_select.select_option("1")

            dob_checkbox = page.locator("label[for='dob_confirmation']")
            await dob_checkbox.click()

            signup_button = page.locator("#js-signUpBtn")
            await signup_button.click()

            await page.wait_for_load_state("networkidle")
        except:
            print("No DOB modal found.")

        await page.reload(wait_until="load")
        
        tos_btn = page.locator("#modalWrapMTubes div.tosNotificationContent button")

        if await tos_btn.is_visible(timeout=5000):
            await tos_btn.click()
        else:
            print("No TOS modal found.")

        await page.reload(wait_until="load")

        header_btn = page.locator("#profileMenuWrapper > div")
        await header_btn.click()

        return username
    except Exception as e:
        print(f"Error during sign-up: {e}")
        return None

async def sign_in(page, username, password):
        
    await page.goto("https://www.pornhub.com/")

    confirm_age_modal = page.locator('#modalWrapMTubes > div > div > button')
    if await confirm_age_modal.is_visible(timeout=5000):
        await confirm_age_modal.click()
    else:
        print("No age confirmation modal found.")

    cookie_btn = page.locator('#cookieBannerWrapper > button.cbSecondaryCTA.cbButton.gtm-event-cookie-banner')
    if await cookie_btn.is_visible(timeout=5000):
        await cookie_btn.click()
    else:
        print("No cookie banner found.")

    await page.reload(wait_until="load")

    header_btn = page.locator("#headerLoginLink.signIn")
    await header_btn.click()
    
    sign_in_btn = page.locator("#headerLoginLink.topMenuButtons")
    await sign_in_btn.click()

    email_pass_btn = page.locator(".emailPassSignButton")
    await email_pass_btn.click()

    email_input = page.locator("#usernameModal")
    await email_input.fill(username)

    password_input = page.locator("#passwordModal")
    await password_input.fill(password)

    sign_up_submit = page.locator("#signinSubmit")
    await sign_up_submit.click()

    await page.wait_for_load_state("networkidle")

    dob_title = page.locator("text=Date of birth")
    try:
        await dob_title.wait_for(state="visible", timeout=5000)
        print("DOB modal detected")

        year_select = page.locator("#js_year")
        await year_select.select_option("1995")

        month_select = page.locator("#js_month")
        await month_select.select_option("1")

        day_select = page.locator("#js_day")
        await day_select.select_option("1")

        dob_checkbox = page.locator("label[for='dob_confirmation']")
        await dob_checkbox.click()

        signup_button = page.locator("#js-signUpBtn")
        await signup_button.click()

        await page.wait_for_load_state("networkidle")
    except:
        print("No DOB modal found.")

    await page.reload(wait_until="load")
    
    tos_btn = page.locator("#modalWrapMTubes div.tosNotificationContent button")

    if await tos_btn.is_visible(timeout=5000):
        await tos_btn.click()
    else:
        print("No TOS modal found.")

    await page.reload(wait_until="load")

    header_btn = page.locator("#profileMenuWrapper > div")
    await header_btn.click()

# TODO 

async def test_links(username, password):
    async with AsyncBrowserManager(headless=False) as page:
        await sign_in(page, username, password)

        network_link = page.get_by_role("link", name="SpiceVids")
        await network_link.click()

async def test_buttons():
    """
    play, pause, next, mute, autoplay, fullscreen 
    """
    pass

async def main():
    username = await get_username() 
    password = "SecretPassword123!"
    async with AsyncBrowserManager(headless=False) as page:
        username = await sign_up(page, username, password)
        if not username:
            print("Sign-up failed, skipping further actions.")
            username = f"None_{int(time.time())}"
            time.sleep(5)
        print(f"Account created: {username} | {password}")

        screenshot_path = f"screenshots/{username}_screenshot.png"
        await page.screenshot(path=screenshot_path)
        print(f"Screenshot saved to {screenshot_path}")

    
    # async with AsyncBrowserManager(headless=False) as page:
    #     await sign_in(page, username, password)
    #     print(f"Signed in: {username} | {password}")

    #     screenshot_path = f"screenshots/{username}_screenshot.png"
    #     await page.screenshot(path=screenshot_path)
    #     print(f"Screenshot saved to {screenshot_path}")


async def runner():
    for _ in range(1000):
        await main()

if __name__ == "__main__":
    asyncio.run(runner())
