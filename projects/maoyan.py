import requests
import time
from lxml import etree
def get_1_page(url):
    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    r = requests.get(url,headers=headers)
    if r.status_code == 200:
        return r.text
    return None
def parse_page(html):
    html = etree.HTML(html)
    result_NO = html.xpath('//dd/i/text()')
    result_title = html.xpath('//dd//p/a/text()')
    return result_NO,result_title
def main():
    url = 'http://maoyan.com/board/4?offset='
    for i in range(10):
        url = url + str(i*10)
        html = get_1_page(url)
        parse = parse_page(html)
        NO = parse[0]
        title = parse[1]
        for i in range(len(NO)):
            print(NO[i]+'---'+title[i])
        time.sleep(2)
main()