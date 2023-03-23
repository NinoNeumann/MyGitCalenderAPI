# -*- coding: UTF-8 -*-
import requests
import re
from bs4 import BeautifulSoup
from http.server import BaseHTTPRequestHandler
import json

def list_split(items, n):
    return [items[i:i + n] for i in range(0, len(items), n)]
def getdata(name):
    gitpage = requests.get("https://github.com/" + name)
    soup = BeautifulSoup(gitpage.text,'html.parser')
    data_list = soup.find_all(class_ = "ContributionCalendar-day")
    data_set = []
    length = len(data_list)-5 # 有五个格子是 最后的标尺
    # 定义正则：
    contri_reg = re.compile(r'(.*?) contribution[s]* on')
    contributions = 0
    for idx in range(length):
        data_date = data_list[idx]["data-date"]
        data_contri = contri_reg.findall(data_list[idx].text)
        data_contri = int(data_contri[0]) if data_contri[0] != 'No' else 0
        contributions = contributions+data_contri
        data_set.append({"date":data_date,"count":data_contri})

    d_set = list_split(data_set, 7)
    return {
        "total": contributions,
        "contributions": d_set
    }



class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        path = self.path
        user = path.split('?')[1]
        data = getdata(user)
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode('utf-8'))
        return
