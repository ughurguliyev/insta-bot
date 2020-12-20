from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options

import time

from .repository import Repo

# PATH = '/usr/local/bin/chromedriver'
list = []

options = Options()

options.add_argument('--headless')
options.add_argument('--disable-gpu')

driver = webdriver.Firefox(options=options)


def login():

    driver.get('https://www.instagram.com/accounts/login/')

    time.sleep(5)

    username_input = driver.find_element_by_name('username')
    password_input = driver.find_element_by_name('password')
    username_input.send_keys('seleniumbotpy')
    password_input.send_keys('Glyv3791@@')

    time.sleep(5)

    login_button = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
    login_button.send_keys(Keys.RETURN)

    time.sleep(10)


def start_bot():

    login()

    driver.get('https://www.instagram.com/temirchiniz/')

    time.sleep(10)

    followers_button = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
    followers_button.send_keys(Keys.RETURN)

    time.sleep(10)

    try:
        wait = WebDriverWait(driver, 10)
        main = driver.find_element_by_class_name('isgrP')
        scroll = 0
        while scroll < 1:
            driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', main)
            time.sleep(2)
            scroll += 1

        products = main.find_elements_by_xpath('/html/body/div[5]/div/div/div[2]/ul/div/li')

        for product in products:
            header = product.find_element_by_class_name('FPmhX')
            user_link = product.find_element_by_class_name('FPmhX').get_attribute('href')
            user_title = product.find_element_by_class_name('wFPL8')
            profile_img = product.find_element_by_class_name('_6q-tv').get_attribute('src')
            if '44884218_345707102882519_2446069589734326272_n.jpg' in profile_img:
                list.append(f'username:{header.text} - link {user_link} - title {user_title.text}')

    except:
        print('error happened 2')
        pass

    Repo().write_file(list)

    driver.quit()