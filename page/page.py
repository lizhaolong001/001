from page.diyilianxiren import DiYiLianXiRenPage
from page.jiaru import JiaRuPage
from page.saved_contact_page import SavedContactPage


class Page:
    def __init__(self, driver):
        self.driver = driver

    @property
    def da_yi_lian_xi(self):
        return DiYiLianXiRenPage(self.driver)

    @property
    def jia_ru(self):
        return JiaRuPage(self.driver)

    @property
    def saved_contact(self):
        return SavedContactPage(self.driver)