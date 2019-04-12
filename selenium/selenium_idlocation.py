from selenium import webdriver
from selenium.webdriver import ActionChains

browser = webdriver.Chrome()
browser.get('http://www.zhihu.com/explore')

logo = browser.find_element_by_class_name('zu-top-link-logo')
print(logo.id)
print(logo.location)
print(logo.tag_name)
print(logo.size)