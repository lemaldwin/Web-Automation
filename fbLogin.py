#Automatic facebook login for hydro_gorgo

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from account import Account

credentials=Account()

browser = webdriver.Firefox()
browser.get('https://facebook.com')
assert 'Facebook' in browser.title

inputEmail = browser.find_element_by_name("email")  # Find the search box
inputEmail.send_keys(credentials.getUsername())# + Keys.RETURN)

inputPassword = browser.find_element_by_name("pass")
inputPassword.send_keys(credentials.getPassword() + Keys.RETURN)

#episode
