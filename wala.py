from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

list_branches = ['1. Ulum Tahghighat', '2. Tehran Shomal', '3. Tehran Markaz', '4. Tehran Jonub', '5. Tehran Gharb',
                 '6. Tehran Shargh', '7. Khorasgan', '8. Yadgar Emam', '9. Varamin', '10. Eslamshahr',
                 '11. Shahr Ghods', '12. Malard',
                 '13. Safardasht'
                 ]

for item in list_branches:
    print(item)

branch = input('\nEnter your branch: ')
username = input('Enter your username: ')
password = input('Enter your password: ')
message = "سلام استاد"


if branch == 'Tehran Shomal':


    # http://iau-tnb.daan.ir/
    browser = webdriver.Chrome()
    browser.get('http://iau-tnb.daan.ir/login-identification-form')
    browser.find_element_by_name("identification_number").send_keys(username)
    browser.find_element_by_name("password").send_keys(password)
    button = browser.find_element_by_tag_name('button')
    button.click()

    browser.get('http://iau-tnb.daan.ir/session-list#session-list')
    vurud = browser.find_element_by_xpath('//*[@id="session-list"]/div[2]/div[3]/table/tbody/tr/td[3]/a[2]')
    vurud.click()

    time.sleep(15)
    browser.find_element_by_css_selector('#message-input').send_keys(message)
    browser.find_element_by_css_selector('#message-input').send_keys(Keys.ENTER)

elif branch == 'Tehran Markaz':

    # http://iauctb.daan.ir/
    browser = webdriver.Chrome()
    browser.get('http://iauctb.daan.ir/login-identification-form')
    browser.find_element_by_name("identification_number").send_keys(username)
    browser.find_element_by_name("password").send_keys(password)
    button = browser.find_element_by_tag_name('button')
    button.click()

    browser.get('http://iauctb.daan.ir/session-list#session-list')
    vurud = browser.find_element_by_xpath('//*[@id="session-list"]/div[2]/div[3]/table/tbody/tr/td[3]/a[2]')
    vurud.click()

    time.sleep(15)
    browser.find_element_by_css_selector('#message-input').send_keys(message)
    browser.find_element_by_css_selector('#message-input').send_keys(Keys.ENTER)

elif branch == 'Tehran Jonub':

    # http://azad.daan.ir/
    browser = webdriver.Chrome()
    browser.get('http://azad.daan.ir/login-identification-form')
    browser.find_element_by_name("identification_number").send_keys(username)
    browser.find_element_by_name("password").send_keys(password)
    button = browser.find_element_by_tag_name('button')
    button.click()

    browser.get('http://azad.daan.ir/session-list#session-list')
    vurud = browser.find_element_by_xpath('//*[@id="session-list"]/div[2]/div[3]/table/tbody/tr/td[3]/a[2]')
    vurud.click()

    time.sleep(15)
    browser.find_element_by_css_selector('#message-input').send_keys(message)
    browser.find_element_by_css_selector('#message-input').send_keys(Keys.ENTER)

elif branch == 'Tehran Gharb':

    # http://wtiau.daan.ir/
    browser = webdriver.Chrome()
    browser.get('http://wtiau.daan.ir/login-identification-form')
    browser.find_element_by_name("identification_number").send_keys(username)
    browser.find_element_by_name("password").send_keys(password)
    button = browser.find_element_by_tag_name('button')
    button.click()

    browser.get('http://wtiau.daan.ir/session-list#session-list')
    vurud = browser.find_element_by_xpath('//*[@id="session-list"]/div[2]/div[3]/table/tbody/tr/td[3]/a[2]')
    vurud.click()

    time.sleep(15)
    browser.find_element_by_css_selector('#message-input').send_keys(message)
    browser.find_element_by_css_selector('#message-input').send_keys(Keys.ENTER)

elif branch == 'Tehran Shargh':

    # http://iauet.daan.ir/
    browser = webdriver.Chrome()
    browser.get('http://iauet.daan.ir/login-identification-form')
    browser.find_element_by_name("identification_number").send_keys(username)
    browser.find_element_by_name("password").send_keys(password)
    button = browser.find_element_by_tag_name('button')
    button.click()

    browser.get('http://iauet.daan.ir/session-list#session-list')
    vurud = browser.find_element_by_xpath('//*[@id="session-list"]/div[2]/div[3]/table/tbody/tr/td[3]/a[2]')
    vurud.click()

    time.sleep(15)
    browser.find_element_by_css_selector('#message-input').send_keys(message)
    browser.find_element_by_css_selector('#message-input').send_keys(Keys.ENTER)

elif branch == 'Ulum Tahghighat':

    # http://srbiau.daan.ir/
    browser = webdriver.Chrome()
    browser.get('http://srbiau.daan.ir/login-identification-form')
    browser.find_element_by_name("identification_number").send_keys(username)
    browser.find_element_by_name("password").send_keys(password)
    button = browser.find_element_by_tag_name('button')
    button.click()

    browser.get('http://srbiau.daan.ir/session-list#session-list')
    vurud = browser.find_element_by_xpath('//*[@id="session-list"]/div[2]/div[3]/table/tbody/tr/td[3]/a[2]')
    vurud.click()

    time.sleep(15)
    browser.find_element_by_css_selector('#message-input').send_keys(message)
    browser.find_element_by_css_selector('#message-input').send_keys(Keys.ENTER)

elif branch == 'Khorasgan':

    # http://khuisf.daan.ir/
    browser = webdriver.Chrome()
    browser.get('http://khuisf.daan.ir/login-identification-form')
    browser.find_element_by_name("identification_number").send_keys(username)
    browser.find_element_by_name("password").send_keys(password)
    button = browser.find_element_by_tag_name('button')
    button.click()

    browser.get('http://khuisf.daan.ir/session-list#session-list')
    vurud = browser.find_element_by_xpath('//*[@id="session-list"]/div[2]/div[3]/table/tbody/tr/td[3]/a[2]')
    vurud.click()

    time.sleep(15)
    browser.find_element_by_css_selector('#message-input').send_keys(message)
    browser.find_element_by_css_selector('#message-input').send_keys(Keys.ENTER)

elif branch == 'Yadgar Emam':

    # http://iausr.daan.ir/
    browser = webdriver.Chrome()
    browser.get('http://iausr.daan.ir/login-identification-form')
    browser.find_element_by_name("identification_number").send_keys(username)
    browser.find_element_by_name("password").send_keys(password)
    button = browser.find_element_by_tag_name('button')
    button.click()

    browser.get('http://iausr.daan.ir/session-list#session-list')
    vurud = browser.find_element_by_xpath('//*[@id="session-list"]/div[2]/div[3]/table/tbody/tr/td[3]/a[2]')
    vurud.click()

    time.sleep(15)
    browser.find_element_by_css_selector('#message-input').send_keys(message)
    browser.find_element_by_css_selector('#message-input').send_keys(Keys.ENTER)

elif branch == 'Varamin':

    # http://iauvaramin.daan.ir/
    browser = webdriver.Chrome()
    browser.get('http://iauvaramin.daan.ir/login-identification-form')
    browser.find_element_by_name("identification_number").send_keys(username)
    browser.find_element_by_name("password").send_keys(password)
    button = browser.find_element_by_tag_name('button')
    button.click()

    browser.get('http://iauvaramin.daan.ir/session-list#session-list')
    vurud = browser.find_element_by_xpath('//*[@id="session-list"]/div[2]/div[3]/table/tbody/tr/td[3]/a[2]')
    vurud.click()

    time.sleep(15)
    browser.find_element_by_css_selector('#message-input').send_keys(message)
    browser.find_element_by_css_selector('#message-input').send_keys(Keys.ENTER)

elif branch == 'Eslamshahr':

    # http://iiau.daan.ir/
    browser = webdriver.Chrome()
    browser.get('http://iiau.daan.ir/login-identification-form')
    browser.find_element_by_name("identification_number").send_keys(username)
    browser.find_element_by_name("password").send_keys(password)
    button = browser.find_element_by_tag_name('button')
    button.click()

    browser.get('http://iiau.daan.ir/session-list#session-list')
    vurud = browser.find_element_by_xpath('//*[@id="session-list"]/div[2]/div[3]/table/tbody/tr/td[3]/a[2]')
    vurud.click()

    time.sleep(15)
    browser.find_element_by_css_selector('#message-input').send_keys(message)
    browser.find_element_by_css_selector('#message-input').send_keys(Keys.ENTER)

elif branch == 'Shahr Ghods':

    # http://qodsiau.daan.ir/
    browser = webdriver.Chrome()
    browser.get('http://qodsiau.daan.ir/login-identification-form')
    browser.find_element_by_name("identification_number").send_keys(username)
    browser.find_element_by_name("password").send_keys(password)
    button = browser.find_element_by_tag_name('button')
    button.click()

    browser.get('http://qodsiau.daan.ir/session-list#session-list')
    vurud = browser.find_element_by_xpath('//*[@id="session-list"]/div[2]/div[3]/table/tbody/tr/td[3]/a[2]')
    vurud.click()

    time.sleep(15)
    browser.find_element_by_css_selector('#message-input').send_keys(message)
    browser.find_element_by_css_selector('#message-input').send_keys(Keys.ENTER)

elif branch == 'Malard':

    # http://iaumalard.daan.ir/
    browser = webdriver.Chrome()
    browser.get('http://iaumalard.daan.ir/login-identification-form')
    browser.find_element_by_name("identification_number").send_keys(username)
    browser.find_element_by_name("password").send_keys(password)
    button = browser.find_element_by_tag_name('button')
    button.click()

    browser.get('http://iaumalard.daan.ir/session-list#session-list')
    vurud = browser.find_element_by_xpath('//*[@id="session-list"]/div[2]/div[3]/table/tbody/tr/td[3]/a[2]')
    vurud.click()

    time.sleep(15)
    browser.find_element_by_css_selector('#message-input').send_keys(message)
    browser.find_element_by_css_selector('#message-input').send_keys(Keys.ENTER)

elif branch == 'Safardasht':

    # http://safaiau.daan.ir/
    browser = webdriver.Chrome()
    browser.get('http://safaiau.daan.ir/login-identification-form')
    browser.find_element_by_name("identification_number").send_keys(username)
    browser.find_element_by_name("password").send_keys(password)
    button = browser.find_element_by_tag_name('button')
    button.click()

    browser.get('http://safaiau.daan.ir/session-list#session-list')
    vurud = browser.find_element_by_xpath('//*[@id="session-list"]/div[2]/div[3]/table/tbody/tr/td[3]/a[2]')
    vurud.click()

    time.sleep(15)
    browser.find_element_by_css_selector('#message-input').send_keys(message)
    browser.find_element_by_css_selector('#message-input').send_keys(Keys.ENTER)

else:
    print("Please try again.")
