from browser.actions import navigate_to, click_element, type_text, get_text
from utils.logger import log_info, log_error
from playwright.sync_api import Page

def example_task(page: Page):
    try:
        try:
            navigate_to(page, "http://automationpractice.pl/index.php")
            page.wait_for_selector("a.login", timeout=10000)  
            log_info("🏠 Opened homepage.")
        except Exception as e:
            log_error(f"Failed to open homepage or locate login link: {e}")
            return  

        try:
            click_element(page, "a.login")
            page.wait_for_selector("#SubmitLogin", timeout=10000)
            log_info("🔐 Navigating to login page...")
        except Exception as e:
            log_error(f"Failed to navigate to login page: {e}")
            return

        email = "vasil.milchev.business@gmail.con"
        password = "v6Gz$C4I$UlV$!lsbzxs"

        try:
            type_text(page, "#email", email)
            type_text(page, "#passwd", password)
            click_element(page, "#SubmitLogin")
            page.wait_for_selector("input[name='search_query']", timeout=10000)  
            log_info(f"✅ Logged in successfully as {email}")
        except Exception as e:
            log_error(f"Login failed: {e}")
            return

        search_query = "woman dress"
        try:
            type_text(page, "input[name='search_query']", search_query)
            click_element(page, "button[name='submit_search']")
            page.wait_for_selector(".product_list .product-name", timeout=10000)
            log_info(f"🔍 Searched for '{search_query}'")
        except Exception as e:
            log_error(f"Search failed: {e}")
            return

        try:
            page.select_option("#selectProductSort", value="price:asc")
            page.wait_for_selector(".product_list .product-name", timeout=10000)  

            selected_option = page.query_selector("#selectProductSort option[selected]")
            sort_text = selected_option.inner_text()
            log_info(f"🔢 Applied sort: {sort_text}")

        except Exception as e:
            log_error(f"Sorting failed: {e}")
            sort_text = "Unknown"  



        product_name_selector = ".product_list .product-name"
        product_price_selector = ".product_list .right-block .price.product-price"
        try:
            product_name = get_text(page, product_name_selector)
            product_price = get_text(page, product_price_selector)
            product_link = page.query_selector(product_name_selector).get_attribute("href")

            if product_name and product_price and product_link:
                log_info(
                    f"1. Required Core: The Robot Driver:\n"
                    f"🔍 Search result from '{search_query}':\n"
                    f"🧾 Applied filter/sort: {sort_text}\n"
                    f"📘 Found product: '{product_name}'\n"
                    f"💲 Price: {product_price}\n"
                    f"🌐 Link: {product_link}"
                )
            else:
                log_error("⚠️ Failed to extract product info.")
        except Exception as e:
            log_error(f"Failed to extract product info: {e}")

    except Exception as e:
        log_error(f"❌ Task failed unexpectedly: {e}")
