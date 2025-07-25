import time
import pytest
from Login.test_baseclass import BaseClass
from Login.test_login import Login_page
from Login.test_loginData import login_data


class Test_login(BaseClass):
    def test_login(self, getData):
        self.driver.implicitly_wait(10)
        log = self.getLogger()
        login = Login_page(self.driver)
        login.signin_button()
        login.put_Number().send_keys(getData["Number"])
        time.sleep(2)
        log.info("Number entered successfully")
        if not login.nextBtn_clickable():
            self.driver.refresh()
            time.sleep(1)
        login.next_button()
        login.put_pass().send_keys(getData["Password"])
        assert login.is_button_clickable()
        time.sleep(2)
        login.login_button()
        time.sleep(1)
        log.info("Login Successfully")
        time.sleep(2)
        login.searchbtn(self).send_keys(getData["Service"])
        time.sleep(2)
        login.searched_Service()
        time.sleep(4)
        login.attribute_click()
        time.sleep(2)
        login.bookNow_btn()
        login.business_selection()
        login.dateandtime()
        login.click_slotnext()
        login.pay_now()
        time.sleep(15)


    @pytest.fixture(params=login_data.test_logindata)
    def getData(self, request):
        return request.param
