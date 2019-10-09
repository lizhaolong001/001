from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class SavedContactPage(BaseAction):
    # 保存后的大标题
    contact_title_feature = By.ID, "com.android.contacts:id/large_title"

    # 获取大标题的名称
    def get_contact_title_text(self):
        return self.find_element(self.contact_title_feature).text