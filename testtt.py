#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from io import StringIO
import random
import discord  
import os
from discord.activity import Activity
from dotenv import load_dotenv
from os import path
from typing import List

TOKEN = os.environ['TOKEN']
client = discord.Client()
List = [1,2,3]
List2 = [1,2]
#123

#i = 精煉值
#x = 成功次數
#y = 失敗次數
#z = 爆炸次數
#t = 鐵祝數量
@client.event
async def on_ready():
    print('目前登入身份：', client.user)
    Activity = discord.Game('沒+12不罷休')
    #discord.Status.<狀態>，可以是online,offline,idle,dnd,invisible
    await client.change_presence(status=discord.Status.online, activity=Activity)
@client.event
async def on_message(message):
    i = x = y = z = t = 0
    if message.content == ('精煉'):        
        await message.channel.send("使用鐵匠的祝福精煉到+12....")
        for i in range(0,4):
            i = i + 1
            # print(i)
        while i < 12:
            # print(a)
            # print(i)
            if i < 7:    
                a = random.choices(List2 , weights = [20,20], k = 1)
                if ''.join(map(str,a)) == "1":
                    i = i + 1
                    x = x + 1
                elif ''.join(map(str,a)) == "2":
                    i = 4
                    z = z + 1
            if i >= 7:
                if i == 7:
                    a = random.choices(List2 , weights = [20,20], k = 1)
                    if ''.join(map(str,a)) == "1":
                        i = i + 1
                        x = x + 1
                        t = t + 1
                    elif ''.join(map(str,a)) == "2":
                        i = i
                        y = y + 1
                        t = t + 1
                if i == 8:
                    a = random.choices(List2 , weights = [20,20], k = 1)
                    if ''.join(map(str,a)) == "1":
                        i = i + 1
                        x = x + 1
                        t = t + 2
                    elif ''.join(map(str,a)) == "2":
                        i = i
                        y = y + 1
                        t = t + 2            
                if i == 9:
                    a = random.choices(List2 , weights = [20,20], k = 1)
                    if ''.join(map(str,a)) == "1":
                        i = i + 1
                        x = x + 1
                        t = t + 3
                    elif ''.join(map(str,a)) == "2":
                        i = i
                        y = y + 1
                        t = t + 3            
                if i in range(10,12):
                    a = random.choices(List2 , weights = [20,20], k = 1)
                    if ''.join(map(str,a)) == "1":
                        i = i + 1
                        x = x + 1
                        t = t + 4
                    elif ''.join(map(str,a)) == "2":
                        i = i
                        y = y + 1
                        t = t + 4
        # print("+"+str(i))
        await message.channel.send('成功：'+str(x)+"，失敗："+str(y)+"，爆掉："+str(z)+"，花費鐵祝："+str(t)+"\n"+"總計："+str(x+y+z))        
    if message.content == ('精煉2'):
        await message.channel.send("沒有使用鐵匠的祝福精煉到+12....")
        for i in range(0,4):
            i = i + 1
            # print(i)
        while i < 12:
            # print(a)
            # print(i)
            if i < 7:    
                a = random.choices(List2 , weights = [20,20], k = 1)
                if ''.join(map(str,a)) == "1":
                    i = i + 1
                    x = x + 1
                elif ''.join(map(str,a)) == "2":
                    i = 4
                    z = z + 1
            if i >= 7:
                if i == 7:
                    a = random.choices(List2 , weights = [20,20], k = 1)
                    if ''.join(map(str,a)) == "1":
                        i = i + 1
                        x = x + 1
                        # t = t + 1
                    elif ''.join(map(str,a)) == "2":
                        i = 4
                        z = z + 1
                        # t = t + 1
                if i == 8:
                    a = random.choices(List2 , weights = [20,20], k = 1)
                    if ''.join(map(str,a)) == "1":
                        i = i + 1
                        x = x + 1
                        # t = t + 2
                    elif ''.join(map(str,a)) == "2":
                        i = 4
                        z = z + 1
                        # t = t + 2           
                if i == 9:
                    a = random.choices(List2 , weights = [20,20], k = 1)
                    if ''.join(map(str,a)) == "1":
                        i = i + 1
                        x = x + 1
                        # t = t + 3
                    elif ''.join(map(str,a)) == "2":
                        i = 4
                        z = z + 1
                        # t = t + 3          
                if i in range(10,12):
                    a = random.choices(List2 , weights = [20,20], k = 1)
                    if ''.join(map(str,a)) == "1":
                        i = i + 1
                        x = x + 1
                        # t = t + 4
                    elif ''.join(map(str,a)) == "2":
                        i = 4
                        z = z + 1
                        # t = t + 4
        # print("+"+str(i))
        await message.channel.send('成功：'+str(x)+"，爆掉："+str(z)+"\n"+"總計："+str(x+y+z))



#機器人token讀檔
# load_dotenv('1.env')
# client.run(os.getenv('token'))
client.run(TOKEN)
# client.run('ODg3MzI4Mzc3ODU2NDYyODY5.YUCi8w.Q1G7knLdK6IaR0r1RQySJSsLVNw')