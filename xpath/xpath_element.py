from lxml import etree

html = etree.parse('./txt.txt',etree.HTMLParser())

print(html)

result1 = html.xpath('//li/*')
print(result1)

##############
'''
子节点  ----/
子孙节点----//
父节点  ----..or::
    
属性匹配
result = html.xpath('//li[@class='value']')

文本获取---text()
result = html.xpath('//li[@class='value']/text()')

属性获取---@href
result = html.xpath('//li/a/@href')

属性多值匹配---contains() #复数
result = html.xpath('//li[contains(@class,'li')]/text()')

多属性匹配---and等运算符
result = html.xpath('//li[contains(@class,'li') and @name='item']/text()')

按序选择
result = html.xpath('//li[1]/a/text()') 选择第一个节点
result = html.xpath('//li[last()]/a/text()')选择最后一个节点
result = html.xpath('//li[position<3]/a/text()')选择位置小于3的节点
result = html.xpath('//li[last()-2]/a/text()')选择倒数第三个节点

节点轴选择
/ancestor::*
/ancestor::div
/attribute::*
/child::a[@href='link.html']
/descendant::span
/following::*[2]
/following-sibling::*
