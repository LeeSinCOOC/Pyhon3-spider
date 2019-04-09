import requests

from requests.packages import urllib3
urllib3.disable_warnings() #忽略警告

import logging #捕获警告到日志
logging.captureWarnings(True)

response = requests.get('https://www.12306.cn',verify=False)
print(response.status_code)