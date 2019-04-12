from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://www.zhihu.com/explore')
print(browser.get_cookies())
print("#"*20)
browser.add_cookie({'name':'bbb','domain':'www.zhihu.com','value':'germey'})
print(browser.get_cookies())

browser.delete_all_cookies()
print(browser.get_cookies())
