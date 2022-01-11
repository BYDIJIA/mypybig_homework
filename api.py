from fastapi import APIRouter
from fastapi import FastAPI
app = FastAPI()
# coding=utf-8
import pymongo
api =APIRouter()
from fastapi.middleware.cors import CORSMiddleware
"""????????
up:string
title:"String
play:String
commit:String
"""
myclient = pymongo.MongoClient('mongodb://admin:admin888@127.0.0.1:27017/Bilibili?authSource=admin')
mydb = myclient['Bilibili']
collist = mydb.list_collection_names()


#跨域处理
# 前端页面url
origins = [
    "http://localhost",
    "http://localhost:8080",
]

# 后台api允许跨域
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



# #test




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
获取全站的排行榜播放量  全站前五up主
"""
@app.get('/get_all_one')
async def get_all_one():
    all_onelists=[]
    for top_list in top_lists:
        if top_list in collist:
            mycol = mydb[top_list]
            al_li=mycol.find({},{'_id': 0,'up':1,'commit':1}).limit(5)
            # print(al_li)
            for list in al_li:
                newList = {
                    'name':list['up'],
                    'value':list['commit']
                }
                # x=mycol.find_one()
                all_onelists.append(newList)
            # print(lists)
            return all_onelists
    # return {"name":top_list,"play":result["play"],"code":200,"message":"success"}

"""
获取音乐的排行榜
"""
@app.get('/get_music')
async def get_music():
    music_lists=[]
    if 'music' in collist:
        mycol = mydb['music']
        music_li=mycol.find({},{'_id': 0}).limit(101)
        for list in music_li:
        # x=mycol.find_one()
            newList = {
                'name': list['up'],
                'value': list['play']
            }
            music_lists.append(newList)
        return music_lists
            # for dict in lists:
            #     return {"up":dict["up"],"title":dict['title'],"play":dict["play"],"commit":dict["commit"],"code":200,"message":"success"}

"""
获取食物的排行榜的播放量 
"""
@api.get('/get_food_play')
async def get_food_play():
    food_lists=[]
    if 'food' in collist:
        mycol = mydb['food']
        food_li=mycol.find({},{'_id': 0,'up':1,'play':1}).limit(101)
        for list in food_li:
            newList = {
                 list['up'],
                list['play']
            }
            # x=mycol.find_one()
            food_lists.append(newList)
            # print(lists)
        return food_lists
    # return {"title": x['title'], "play": x["play"], "code": 200,"message": "success"}

"""
获取食物的排行榜的评论量
"""
@api.get('/get_sports_comm')
async def get_sports_comm():
    sports_lists=[]
    if 'sports' in collist:
        mycol = mydb['sports']
        sports_li=mycol.find({}, {'_id': 0,'title':1,'commit':1}).limit(101)
        for list in sports_li:
            newList = {
                 list['title'],
                list['commit']
            }
            sports_lists.append(newList)
        return sports_lists
    # return {"up": x["up"],"commit": x["commit"], "code": 200,"message": "success"}

"""
获取game的播放量排行榜
"""
@api.get('/get_game_play')
async def get_game_play():
    game_lists=[]
    if 'game' in collist:
        mycol = mydb['game']
        game_li=mycol.find({}, {'_id': 0,'up':1,'play':1}).limit(101)
        for list in game_li:
            newList = {
                list['up'],
                list['play']
            }
            # x=mycol.find_one()
            game_lists.append(newList)
        return game_lists
    # return {"up": x["up"], "play": x["play"], "code": 200,"message": "success"}


"""
获取knowledge的排行榜 轮播表
"""
@api.get('/get_knowledge_comm')
async def get_knowledge_comm():
    kno_lists=[]
    if 'knowledge' in collist:
        mycol = mydb['knowledge']
        kon_li=mycol.find({}, {'_id': 0,'title':1,'commit':1}).limit(101)
        for list in kon_li:
            # x=mycol.find_one()
            newList = {
                 list['title'],list['commit']
            }
            kno_lists.append(newList)
        return kno_lists
    # return {"up": x["up"],"commit": x["commit"], "code": 200,"message": "success"}

"""
获取全站的排行榜
"""
@api.get('/get_all')
async def get_all():
    allists=[]
    if 'all' in collist:
        mycol = mydb['all']
        all_li=mycol.find({},{'_id': 0,'title':1,'play':1}).limit(101)
        for list in all_li:
            # x=mycol.find_one()
            newList = {
                'name': list['title'],
                'value': list['play']
            }
            allists.append(newList)
            # print(lists)
        return allists
    # return {"title":x['title'],"code":200,"message":"success"}

app.include_router(api)