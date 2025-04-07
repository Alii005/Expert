import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common import actions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Login_page:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.actions= ActionChains(self.driver)

    button = (By.XPATH, "//button[text()='Signup/ Login']")

    putNumber = (By.XPATH, "//input[@class='form-control ']")

    nextBtn = (By.XPATH, "//button[@type='submit']")

    putpass = (By.XPATH, "//input[@placeholder='Enter Password']")

    loginbutton = (By.XPATH, "//button[text()='Login']")

    profileBtn = (By.XPATH,"//p[@class='m-0 pt-1 text_user_profile']")

    manageprofile = (By.XPATH, "//p[text()='  Manage Profile']")

    profileImg = (By.XPATH, "//img[@class='img-fluid button_style']")

    firstName = (By.XPATH,"//div[text()='First Name']")

    enterFirstname = (By.XPATH, "//input[@placeholder='JOHN']")

    firstnameBtn = (By.XPATH, "//button[@class='btn btn-danger button_size_fixed universal_button_color px-4']")

    lastName = (By.XPATH, "//div[text()='Last Name']")

    enterLastname = (By.XPATH, "//input[@type='text']")

    lastnameBtn = (By.XPATH, "//button[contains(text(),'Save Changes')]")

    gender = (By.XPATH, "//div[text()='Gender']")

    genderSelection = (By.ID, "man")

    genderBtn = (By.XPATH, "//button[text()='Save Changes']")

    DOB = (By.XPATH, "//div[text()='Date of Birth']")

    Month = (By.XPATH, "//span[text()='January 2024']")

    chosenMonth = (By.XPATH, "//span[text()='May 2024']")

    clndr_next = (By.XPATH, "//button[@class='react-calendar__navigation__arrow react-calendar__navigation__next-button']")

    date = (By.XPATH, "//abbr[text()='20']")

    DOBsave = (By.XPATH, "//button[text()='Save Changes']")

    homebtn = (By.XPATH, "//img[@class='img-fluid width_ll']")


    def signin_button(self):
        return self.driver.find_element(*Login_page.button).click()

    def put_Number(self):
        return self.driver.find_element(*Login_page.putNumber)

    def next_button(self):
        return self.driver.find_element(*Login_page.nextBtn).click()

    def nextBtn_clickable(self):
        try:
            button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
            return button.is_enabled()
        except Exception as e:
            raise Exception("Next button is not clickable")

    def put_pass(self):
        return self.driver.find_element(*Login_page.putpass)

    def login_button(self):
        return self.driver.find_element(*Login_page.loginbutton).click()

    def is_button_clickable(self):
        try:
            button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Login']")))
            return button.is_enabled()
        except Exception as e:
            raise Exception("Login button is not clickable")

    def profile_button(self):
        return self.driver.find_element(*Login_page.profileBtn).click()

    def manageProfile_btn(self):
        return self.driver.find_element(*Login_page.manageprofile).click()

    def uploadProfileImg(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//img[@class='img-fluid button_style']")))
        return self.driver.find_element(*Login_page.profileImg)

    def click_firstname(self):
        return self.driver.find_element(*Login_page.firstName).click()

    def enter_firstname(self):
        element = self.driver.find_element(*Login_page.enterFirstname)
        self.actions.double_click(element).perform()
        return self.driver.find_element(*Login_page.enterFirstname)

    def savebtn_FN(self):
        return self.driver.find_element(*Login_page.firstnameBtn).click()

    def click_lastname(self):
        return self.driver.find_element(*Login_page.lastName).click()

    def enter_lastname(self):
        element = self.driver.find_element(*Login_page.enterLastname)
        self.actions.double_click(element).perform()
        return self.driver.find_element(*Login_page.enterLastname)

    def savebtn_LN(self):
        return self.driver.find_element(*Login_page.lastnameBtn).click()

    def gender_btn(self):
        # self.driver.execute_script("window.scrollTo(0, 1000);")
        return self.driver.find_element(*Login_page.gender).click()

    def gender_selection(self):
        return self.driver.find_element(*Login_page.genderSelection).click()

    def gender_savebtn(self):
        return self.driver.find_element(*Login_page.genderBtn).click()

    def click_DOB(self):
        return self.driver.find_element(*Login_page.DOB).click()

    def select_DOB(self):
        # while self.Month == self.chosenMonth:
        #     next = self.driver.find_element(*Login_page.clndr_next)
        #     next.click()
        #     #if self.Month == self.chosenMonth:
        self.driver.find_element(By.XPATH, "//span[text()='January 2024']").click()
        self.driver.find_element(By.XPATH, "//span[text()='2024']").click()
        next = self.driver.find_element(By.XPATH, "//button[@class='react-calendar__navigation__arrow react-calendar__navigation__prev-button']")
        next.click()
        next.click()
        next.click()
        self.driver.find_element(By.XPATH, "//button[text()='1991']").click()
        self.driver.find_element(By.XPATH, "//abbr[text()='May']").click()

        return self.driver.find_element(*Login_page.date).click()

    def DOB_saveBtn(self):
        return self.driver.find_element(*Login_page.DOBsave).click()

    def homebutton(self):
        return self.driver.find_element(*Login_page.homebtn).click()


















