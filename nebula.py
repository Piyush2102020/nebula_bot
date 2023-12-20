import requests
import random
import time
from firebase_admin import credentials, db
import firebase_admin

no_of_bots = 10 #set the number of bots you want to generate
delay=2  #the delay of bot msg generation
no_of_msg_per_bot = 5 #how many msg you want to assign to a bot
url = 'https://randomuser.me/api/' #you can use any other site for random name generation but then change the code accordingly
sentences = []
gender=["male","female","Not Confirmed","Non Binary"] #list of genders you are using or you can use the site generated genders also
cred = credentials.Certificate('tracki-5f30e-firebase-adminsdk-lad77-afad164095.json')  #your credentials in case you are using firebase
firebase_admin.initialize_app(cred, {
    'databaseURL': 'your_database_url_here'  #database url
})

# Function to print messages
def new_msg(bots):
    for bot in bots:
        random.shuffle(bots)
        msg={'sender':bot['sender'],
             'gender':bot['gender'],
             'message':random.choice(bot['message']),
             'age':str(bot['age']),
             'uid':bot['uid']}
        print("newmsg",msg)
        path=db.reference('home') #heres the refrence to the databse in which we are pusing data
        path.push().set(msg)
        time.sleep(delay)
    
#function to generate bots
def gen_bot():
    global sentences
    global no_of_bots
    global no_of_msg_per_bot
    

    with open("chat_data.txt", "r") as file:
        for row in file:
            if len(row.strip()) != 0:
                sentences.append(row.strip()) 
    

    params = {'results': no_of_bots}
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()['results']

        bots = [{
            'sender': f"{user['name']['first']}",
            'gender': user['gender'],
            'age': random.randint(18, 45),
            'message': random.sample(sentences, no_of_msg_per_bot),
            'uid':'bot'
        } for user in data]
        

        random.shuffle(bots)
        for bot in bots:
            random.shuffle(bot['message'])
        new_msg(bots)
        
    else:
        print("Failed to fetch random names.")


while True:
    gen_bot()
