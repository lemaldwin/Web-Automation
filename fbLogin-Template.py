#Author: Lemuel Garcia
#This can only be used if you have the webdriver for Firefox
#This is for Firefox browsers only, if you want to use other browsers 
#download a different webdriver and change the webdriver used in the code


from selenium import webdriver
from selenium.webdriver.common.keys import Keys


username = "email"#use your email here
password = "password" #enter your password here

browser = webdriver.Firefox()
browser.get('https://facebook.com')
assert 'Facebook' in browser.title

inputEmail = browser.find_element_by_name("email")  # Find the search box
inputEmail.send_keys(username)# + Keys.RETURN)

inputPassword = browser.find_element_by_name("pass")
inputPassword.send_keys(password + Keys.RETURN)

#episode
