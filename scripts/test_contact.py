import time
import pytest
from base.base_analyze import analyze_file
from base.base_driver import init_driver
from page.page import Page


class TestContact:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(5)
        self.driver.quit()

    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    @pytest.mark.parametrize("args", analyze_file("reg_data.yaml", "test_contact"))
    def test_contact(self, args):
        name = args["name"]
        phone = args["phone"]

        # 点击主页，新建联系人
        self.page.da_yi_lian_xi.add_tian_jia()
        # 输入名字
        self.page.jia_ru.input_name(name)
        # 输入电话
        self.page.jia_ru.input_phone(phone)
        # 点击返回
        self.page.jia_ru.press_back()
        # 断言：判断输入名字和保存名字是否一致
        assert name == self.page.saved_contact.get_contact_title_text()