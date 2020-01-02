#https://vk.com/id528797001
from time import sleep
import requests
import datetime
datetime.datetime.now()

token='57da844e6876e3e01596435a15264c5cbc8f58f2408b72784b19ea4eb06e3106886075e7c50aaff9ea5db'
flag = 0
while True:
    r = requests.get('https://api.vk.com/method/users.get?', params={
        'access_token':token,
        'user_ids':'id#########',
        'fields':'online',
        'v':5.103,
    })
    data = r.json()
    status = data['response'][0]['online']
    print(status)
    database = open('data.txt','a')
    if status == 1:

        if flag == 0:
            database.write('online from: '+str(datetime.datetime.now()) + '\n')
        flag = 1
    else:
        if flag == 1:
            database.write('log out from: '+str(datetime.datetime.now()) + '\n')
            flag = 0
    check = open('Exit.txt', 'r')
    if check.read() == 'exit':
        database.close()
        check.close()
        break
    sleep(15)





#oauth.vk.com/authorize?client_id=7239056&scope=photos,audio,video,docs,notes,pages,status,offers,questions,wall,groups,messages,email,notifications,stats,ads,offline,docs,pages,stats,notifications&response_type=token
