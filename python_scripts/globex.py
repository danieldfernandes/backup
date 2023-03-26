from selenium import webdriver # pip3 install selenium
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time, getpass, unittest, pyautogui # pip3 install pyautogui 
from selenium.webdriver.common.by import By
from config import *
from auxiliar import *

class TestGlobex(unittest.TestCase):

    # def test_success_trx_Keybank(self):

    #     # switch to banks iframe on lightbox
    #     iframe = browser.find_element("id", "paywithmybank-iframe-widget-container")
    #     browser.switch_to.frame(iframe)
        
    #     # select the bank under test on lightbox
    #     next = WebDriverWait(browser, 15).until(EC.element_to_be_clickable(("id", "widgetSearchField"))).send_keys( "Keybank" )
    #     next = WebDriverWait(browser, 15).until(EC.element_to_be_clickable(("id", "fic-307070267"))).click()
        
    #     browser.switch_to.default_content()
    #     iframe = WebDriverWait(browser, 15).until(EC.element_to_be_clickable(("id", "paywithmybank-iframe")))
    #     browser.switch_to.frame(iframe)

    #     next = WebDriverWait(browser, 20).until(EC.element_to_be_clickable(("id", "slider-button"))).click()
        
    #     iframe = WebDriverWait(browser, 10).until(EC.element_to_be_clickable(("id", "lbx-iframeAuthenticate")))
    #     browser.switch_to.frame(iframe)
        
    #     next = WebDriverWait(browser, 60).until(EC.element_to_be_clickable(("id", "lbx-formAuthenticate-authFields-labeluserid"))).send_keys( input("Keybank username: ") )
    #     next = WebDriverWait(browser, 60).until(EC.element_to_be_clickable(("id", "lbx-formAuthenticate-authFields-inputpassword"))).send_keys( getpass.getpass("Keybank password: ") )

    #     next = WebDriverWait(browser, 15).until(EC.presence_of_element_located(("id", "lbx-formLogin-submit"))).click()
        
    #     time.sleep(15)

    # def test_invalid_login_Keybank(self):

    #     # switch to banks iframe on lightbox
    #     iframe = browser.find_element("id", "paywithmybank-iframe-widget-container")
    #     browser.switch_to.frame(iframe)
        
    #     # select the bank under test on lightbox
    #     next = WebDriverWait(browser, 5).until(EC.element_to_be_clickable(("id", "widgetSearchField"))).send_keys( "Keybank" )
    #     next = WebDriverWait(browser, 5).until(EC.element_to_be_clickable(("id", "fic-307070267"))).click()
        
    #     browser.switch_to.default_content()
    #     iframe = WebDriverWait(browser, 15).until(EC.element_to_be_clickable(("id", "paywithmybank-iframe")))
    #     browser.switch_to.frame(iframe)

    #     next = WebDriverWait(browser, 15).until(EC.element_to_be_clickable(("id", "slider-button"))).click()
        
    #     iframe = WebDriverWait(browser, 10).until(EC.element_to_be_clickable(("id", "lbx-iframeAuthenticate")))
    #     browser.switch_to.frame(iframe)

    #     next = WebDriverWait(browser, 60).until(EC.element_to_be_clickable(("id", "lbx-formAuthenticate-authFields-labeluserid"))).send_keys( input("Keybank username: ") )
    #     next = WebDriverWait(browser, 60).until(EC.element_to_be_clickable(("id", "lbx-formAuthenticate-authFields-inputpassword"))).send_keys( getpass.getpass("Keybank password: ") )

    #     next = WebDriverWait(browser, 8).until(EC.presence_of_element_located(("id", "lbx-formLogin-submit"))).click()
        
    #     time.sleep(15)

    # blocked by DI window
    def test_FI_DirectIntegration(self):

        iframe = browser.find_element("id", "paywithmybank-iframe-widget-container")
        browser.switch_to.frame(iframe)
        
        next = WebDriverWait(browser, 5).until(EC.presence_of_element_located(("id", "widgetSearchField"))).send_keys('Chase')
        next = WebDriverWait(browser, 5).until(EC.presence_of_element_located(("id", "fic-102001017"))).click()
        
        browser.switch_to.default_content()

        iframe = WebDriverWait(browser, 15).until(EC.presence_of_element_located(("id", "paywithmybank-iframe")))
        iframe = browser.find_element("xpath", "//*[@id=\"paywithmybank-iframe\"]")
        browser.switch_to.frame(iframe)
        
        next = WebDriverWait(browser, 15).until(EC.presence_of_element_located(("id", "lbx-formAuthenticate"))).click()
        time.sleep(60)

    @classmethod
    def setUpClass(cls):
        browser.get(globex)
        time.sleep(6)

    @classmethod
    def tearDownClass(cls):
        #browser.close() # Closes the current window
        browser.quit() # All windows related to driver instance will quit

    #def setUp(self):
    #def tearDown(self):

if __name__ == '__main__':
    unittest.main()