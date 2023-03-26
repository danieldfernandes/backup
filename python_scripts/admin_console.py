from selenium import webdriver # pip3 install selenium
import time, getpass, unittest, pyautogui # pip3 install pyautogui 
from config import *
from aux import *

class TestAdminConsole(unittest.TestCase):

    def test_search_Trustly_on_google(self):
        #"//*[@id=\"sortabletable\"]/tbody/tr[1]/td[36]/a[2]"
        #"//*[@id=\"sortabletable\"]/tbody/tr[2]/td[36]/a[2]"
        #elem = chrome_browser.find_element(By.NAME, "q").send_keys("Trustly")
        time.sleep(1)
        #pyautogui.press('esc')
        #elem = browser.find_element(By.NAME, "btnK").click()
        #self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")

    @classmethod
    def setUpClass(cls):
        browser.get(admin_console)
        # >>> login on admin console
        if(env == "local"):
            browser.find_element("id","username").send_keys('admin')
            browser.find_element("id","password").send_keys('superadmin')
        else:
            browser.find_element("id","username").send_keys('daniel.fernandes')
            #browser.find_element("id","password").send_keys(input("Password: "))
            browser.find_element("id","password").send_keys(getpass.getpass('Password to log into Admin Console: '))
        browser.find_element("id","btn-login").click()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        #browser.close() # Closes the current window
        browser.quit() # All windows related to driver instance will quit

    #def setUp(self):
    #def tearDown(self):

if __name__ == '__main__':
    unittest.main()