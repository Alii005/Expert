import time
import pytest

from Editbooking.test_editbookingdata import Edit_booking
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
        log.info("Login Successfully")
        time.sleep(2)
        # login.searchbtn(self).send_keys(getData["Service"])

        # --- Edit Booking Flow ---
        edit = Edit_booking(self.driver)
        edit.open_profile_dropdown()
        edit.go_to_my_orders()
        edit.click_booking()
        edit.click_edit_appointment()
        edit.click_date_card("Mon", "28")
        edit.click_time_slot("09:30-09:45")
        edit.click_save_continue()


@pytest.fixture(params=login_data.test_logindata)
def getData(request):
    return request.param
