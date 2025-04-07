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
        time.sleep(1)
        log.info("Number entered successfully")
        if not login.nextBtn_clickable():
            self.driver.refresh()
            time.sleep(1)
        login.next_button()
        login.put_pass().send_keys(getData["Password"])
        assert login.is_button_clickable()
        login.login_button()
        time.sleep(4)
        log.info("Login Successfully")
        time.sleep(2)

    @pytest.fixture(params=login_data.test_logindata)
    def getData(self, request):
        return request.param
