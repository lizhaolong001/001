from selenium.webdriver.common.by import By
import allure
from base.base_action import BaseAction


class JiaRuPage(BaseAction):
    name_text = By.XPATH, "//*[@text ='姓名']"
    phone_text = By.XPATH, "//*[@text ='电话']"

    @allure.step(title='输入名字')
    def input_name(self, text):
        allure.attach("名字:", text)
        self.input(self.name_text, text)

    @allure.step(title='输入电话')
    def input_phone(self, text):
        self.input(self.phone_text, text)
        allure.attach("截图：", self.driver.get_screenshot_as_png(), allure.attach_type.PNG)