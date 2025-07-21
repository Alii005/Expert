import time
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, TimeoutException, \
    NoAlertPresentException
from Login.test_loginData import login_data


class Edit_booking:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.actions = ActionChains(self.driver)

    def open_profile_dropdown(self):
        try:
            dropdown_button = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//p[contains(@class, 'text_user_profile')]"))
            )
            dropdown_button.click()
            print("Opened user profile dropdown.")
        except Exception as e:
            print(f"Failed to open profile dropdown: {e}")

    def go_to_my_orders(self):
        try:
            my_orders = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//p[text()='My Orders']"))
            )
            my_orders.click()
            print("Navigated to 'My Orders'.")
        except Exception as e:
            print(f"Failed to click 'My Orders': {e}")

    def click_booking(self):
        try:
            first_booking = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "(//p[@class='m-0 p-0 main_waxflow_text'])[1]"))
            )
            first_booking.click()
            print("Clicked on the first booking card.")
        except Exception as e:
            print(f"Failed to click the first booking card: {e}")

    def click_edit_appointment(self):
        try:
            edit_button = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//p[text()='Edit Appointment']"))
            )
            edit_button.click()
            print("Clicked 'Edit Appointment'.")
        except Exception as e:
            print(f"Failed to click 'Edit Appointment': {e}")

    def click_date_card(self, target_day: str, target_date: str):
        try:
            date_cards = self.driver.find_elements(By.CLASS_NAME, "item_card_pc")
            for card in date_cards:
                try:
                    day_text = card.find_element(By.TAG_NAME, "p").text
                    date_text = card.find_elements(By.TAG_NAME, "p")[1].text
                    if day_text == target_day and date_text == target_date:
                        card.click()
                        print(f"Selected date: {day_text} {date_text}")
                        return
                except (NoSuchElementException, IndexError):
                    continue
            print(f"No matching date found for: {target_day} {target_date}")
        except NoSuchElementException:
            print("Date cards not found.")

    def click_time_slot(self, target_time: str) -> bool:
        try:
            time_slot_elements = self.driver.find_elements(By.XPATH, f"//p[contains(normalize-space(), '{target_time}')]")
            for element in time_slot_elements:
                if element.text.strip() == target_time:
                    element.click()
                    print(f"Selected time slot: {target_time}")
                    return True
            print(f"Time slot not found: {target_time}")
            return False
        except (NoSuchElementException, ElementClickInterceptedException) as e:
            print(f"Error while selecting time slot '{target_time}': {e}")
            return False

    def click_save_continue(self):
        # self.driver.execute_script("window.scrollBy(0, 1000);")
        try:
            # Wait for and click the 'Save & Continue' button
            save_button = self.wait.until(
                EC.element_to_be_clickable((By.XPATH,"//button[contains(@class, 'button_width_slots') and contains(normalize-space(), 'Save & Continue')]")))
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", save_button)
            time.sleep(1)
            save_button.click()
            print("Clicked 'Save & Continue'.")

            WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            print(f"Alert says: {alert.text}")
            alert.accept()
            print("Clicked OK on alert.")

        except NoAlertPresentException:
            print("No alert found after clicking Save & Continue.")
        except Exception as e:
            print(f"Error occurred: {e}")

