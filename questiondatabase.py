import csv
import pandas as pd
import firebase_admin
import json
from firebase_admin import db



cred_obj = firebase_admin.credentials.Certificate('hackathon-798eb-firebase-adminsdk-kkqc1-0ef2bb2df7.json')
default_app = firebase_admin.initialize_app(cred_obj, {
	'databaseURL':"https://hackathon-798eb-default-rtdb.firebaseio.com/"
	})

linenumbertotal = 0
ref = db.reference("/")
answered = pd.read_csv("questionsanswer.csv")

def answer(linenumber, answeredquestion):
   answered.loc[linenumber, 'answer'] = answeredquestion
   answered.to_csv("questionsanswer.csv", index=False)
   print(answered)
   ref1 = ref.child('question'+str(linenumber))
   ref1.update({'answer':answeredquestion})
 
def ask(subject, question):
   row = [len(answered)+1, subject, question]
   with open('questionsanswer.csv', 'a') as csvfile:
       writer = csv.writer(csvfile)
       writer.writerow(row)
       print(row)
       qnumb='question'+str(row[0])
       row.pop(0)
       ref.update({qnumb:row})

#ask('science','how do you make 4+5')
#answer(7, 'cookies')
