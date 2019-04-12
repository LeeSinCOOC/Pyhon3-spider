from selenium import webdriver
from selenium.webdriver import ActionChains

browser = webdriver.Chrome()
browser.get('http://www.zhihu.com/explore')

logo = browser.find_element_by_class_name('question_link')
print(logo.text)