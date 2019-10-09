from selenium.webdriver.common.by import By
import allure
from base.base_action import BaseAction



class DiYiLianXiRenPage(BaseAction):

    tianjia = By.ID, "com.android.contacts:id/floating_action_button"

    @allure.step(title='点击添')
    def add_tian_jia(self):
        self.click(self.tianjia)
