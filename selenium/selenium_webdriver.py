from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://www.taobao.com')
print(browser.page_source)

#查找节点
input_first = browser.find_element_by_id('q')
input_second = browser.find_element_by_css_selector('#q')
input_third = browser.find_element_by_xpath('//*[@id="q"]')                                                    

print(input_first,input_second,input_third)

#查找多个节点
lis = browser.find_elements_by_css_selector('.service-bd li')
print(lis)
browser.close()