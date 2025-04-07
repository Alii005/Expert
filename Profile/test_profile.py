import time
import pytest
from Login.test_baseclass import BaseClass
from Login.test_login import Login_page
from Profile.test_profiledata import profile_data

class Test_profile(BaseClass):
    def test_profile(self, getData):
        self.driver.implicitly_wait(10)
        log = self.getLogger()
        login = Login_page(self.driver)
        login.signin_button()
        login.put_Number().send_keys(getData["Number"])
        time.sleep(1)
        log.info("Number entered successfully")
        login.next_button()
        login.put_pass().send_keys(getData["Password"])
        login.login_button()
        log.info("Login Successfully")
        time.sleep(2)
        login.profile_button()
        time.sleep(1)
        log.info("profile button")
        login.manageProfile_btn()
        # log.info("Manage profile button")
        # image_path = "C:\\Users\\Selteq\\Downloads\\Frame 79 (1).jpg"
        # file_input = login.uploadProfileImg()
        # file_input.send_keys(image_path)
        # time.sleep(4)
        login.click_firstname()
        login.enter_firstname().send_keys(getData["Firstname"])
        login.savebtn_FN()
        login.click_lastname()
        login.enter_lastname().send_keys(getData["Lastname"])
        login.savebtn_LN()
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        login.gender_btn()
        login.gender_selection()
        login.gender_savebtn()
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        login.click_DOB()
        login.select_DOB()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        login.DOB_saveBtn()
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        login.homebutton()
        time.sleep(3)



        #assert login.login_button()

    @pytest.fixture(params=profile_data.test_profiledata)
    def getData(self, request):
        return request.param
