
from turtle import bgcolor
import firebase_admin
import json
from firebase_admin import db
import time
from threading import Thread

 
cred_obj = firebase_admin.credentials.Certificate('textjson.json')
default_app5 = firebase_admin.initialize_app(cred_obj, {
    'databaseURL':"https://hackathontext-default-rtdb.firebaseio.com/"
    }, name='app2')
 
global usertolookandtalkto
usertolookandtalkto = ""
username = 'rami'
def couldnotmatch():
    print('couldnt match')
 
def proceedwithchat():
    for users in (ref12.get()).keys():
        if users != username:
            print("matched!\nYou are matched with user: " +str(users))
            usertotalkto = users
            time.sleep(2)
            ref12.update({username:{'looking': False}})
            break
 
 
    def sendmessage():
        #ref12.update({username:{'looking':False,'chat': str(usertotalkto) + " has opened a chat with you! "}})
        chatopen = True
        while chatopen == True:
           
 
           
            texttosend = input("What do you want to say: ")
            ref12.update({username:{'looking':False,'chat': texttosend}})
            if texttosend == 'end':
                ref12.update({username:{'looking':False,'chat':''}})
                break
    def retrieveinfo():
        x = ""
        while True:
            if (ref12.get()[usertotalkto]) != x:
                whattosay = str((ref12.get()[usertotalkto])).split(",")[0].split(":")[1]
                print(('\n')+str(users) + " has said: "+whattosay)
                x=(ref12.get()[usertotalkto])
 
            else:
                x=(ref12.get()[usertotalkto])
 
            time.sleep(0.0001)
           
           
    Thread(target = retrieveinfo).start()
    Thread(target = sendmessage).start()
   
 
global ref12
ref12 = db.reference("/",default_app5)
def userislooking(user):
    global usertolookandtalkto
    ref12.update({user:{"chat":"", 'looking': True}})
    checkbreak = False
    for y in range(15):
        if checkbreak == True:
            break
        else:
            for i in (list((ref12.get()).keys())):
                print(i)
                if i != username:
                    print(ref12.get()[i]['looking'])
                    if ref12.get()[i]['looking'] == True:
                        print(ref12.get()[i]['looking'])
                        usertolookandtalkto = i
                        proceedwithchat()
                        checkbreak = True
                        return True
                        #break
                    elif y == 5:
                        return False
                        couldnotmatch()
                        ref.update({user:{'looking': False}})
        time.sleep(1)
           
 
   
   
 
'''
userresponse = input("Search for a user? ")
if userresponse[0].lower() in ['yes','y']:
    userislooking(username)

'''