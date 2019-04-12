from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://www.taobao.com')
browser.get('http://www.baidu.com')
browser.get('http://www.python.org')
browser.back()
time.sleep(1)
browser.forward()
browser.close()
