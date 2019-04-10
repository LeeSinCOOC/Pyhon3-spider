from lxml import etree

html = etree.parse('./txt.txt',etree.HTMLParser())
result = etree.tostring(html)
print(result)