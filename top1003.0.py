#!/usr/bin/env python
import pymongo
from pymongo.collection import Collection
from pymongo.database import Database

import traceback
from bs4 import BeautifulSoup
import requests
top_lists=["all",
        "guochuang",
        "douga",
        "music",
        "dance",
        "game",
        "knowledge",
        "tech",
        "sports",
        "car",
        "life",
        "food"]

"""
Spyder
@author:dijia
@datetime:2021/12/13 19:44
"""

#连接数据库mongodb
def save_mgb(top,top_list):
    try:
        myclient=pymongo.MongoClient('mongodb://admin:admin888@127.0.0.1:27017/top?authSource=admin')
        collection=Collection(Database(myclient,'top'),top_list)
        for info in top:
            collection.insert_one(info)#插入一条数据循环
        print("数据库连接成功")
    except Exception as e:#异常处理 利用异常库处理
        with open('logger.log', "a") as f:
            traceback.print_exc(file=f)
        print("数据库连接失败",e)
        collection.close()



#获取单个页面的网页资源
def getMainPage(url):
    # 根据url发送请求给服务器
    # 获取html文本
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36'
    }#请求头
    try:
        response = requests.get(url=url, headers=headers, timeout=20)#get请求
        response.raise_for_status()#判断请求状态 返回状态码
        response.encoding = response.apparent_encoding#获取网页编码格式
        return response.text
    except:
        with open('logger.log', "a") as f:
            traceback.print_exc(file=f)
        return "网页访问失败"
#解析html文本 把需要的数据挑出来
def getAllPage(pageText):
    try:
        soup = BeautifulSoup(pageText,'html.parser')
        items = soup.findAll('li', {'class': 'rank-item'})
        top=[]
        for itm in items:
            title = itm.find('a', {'class': 'title'}).text
            up = itm.find('span', {'class': 'data-box up-name'}).text.strip()
            play=itm.find('div',{'class':'detail-state'}).find_all('span')[0].text.strip()
            commit=itm.find('div',{'class':'detail-state'}).find_all('span')[1].text.strip()
            top.append({'title':title,'up':up,'play':play,'commit':commit})
    except:
        with open('logger.log', "a") as f:
            traceback.print_exc(file=f)
    return top

if __name__=="__main__":
    for top_list in top_lists:
        url="https://www.bilibili.com/v/popular/rank/"+top_list
        print(url)
        pageText=getMainPage(url)
        top=getAllPage(pageText)
        save_mgb(top,top_list)



