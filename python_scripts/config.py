from selenium import webdriver # pip3 install selenium
import random

# set your environment here. Options: "local", "uat" or "int"
env = "uat" 
match env.lower():
    case "uat":
        admin_console = "https://uat.paywithmybank.com/admin-console"
        globex = "https://uat.paywithmybank.com/merchant-demo/globex"
    case "int":
        admin_console = "https://int.paywithmybank.com/admin-console"
        globex = "https://int.paywithmybank.com/merchant-demo/globex"
    case default:
        admin_console = "http://localhost:9002/admin-console"
        globex = "http://localhost:7000/merchant-demo/globex"

# set a random browser to run tests (Chrome, Firefox, Safari)
browser_option = random.randint(1, 3)
if(browser_option == 1):
    print("Chrome")
    browser = webdriver.Chrome(executable_path=r'~/WebDrivers/chromedriver')
elif(browser_option == 2):
    print("Firefox")
    browser = webdriver.Firefox(executable_path=r'~/WebDrivers/geckodriver')
elif(browser_option == 3):
    print("Safari")
    browser = webdriver.Safari()

#pyautogui.position()
#print(pyautogui.KEYBOARD_KEYS)
#['\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~', 'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace', 'browserback', 'browserfavorites', 'browserforward', 'browserhome', 'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear', 'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete', 'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10', 'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20', 'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja', 'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail', 'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack', 'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6', 'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn', 'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn', 'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator', 'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab', 'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen', 'command', 'option', 'optionleft', 'optionright']