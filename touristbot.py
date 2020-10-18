"""
This is a program for a chat bot...
1.The bot will start with a greeting and self intro and ask for name of the person
2.The bot will greet and welcome the person
3.Bot will ask what a person want to do, it will offer a choice of things based upon what the bot is designed for
4.It will respond to users input appropriately
"""
import random #random is a library it will give some random things from your collection
import os
from datetime import datetime #datetime is a library to get current date and time 
def greet_and_introduce():
    #declare some list of responses
    responses = [    
        "Hi i'm travellerbot I can help you by providing simple travel tips and giving details of some tourist places in India.",
        "Wonderful, It is so nice to be in touch with you.",
        "Hi i'm a  travellerbot i can do following tasks. "
    ] 
    #pick a response at random and return that
    print( random.choice(responses) )  

def welcome(name):
    #Declare some list of messages 
    messages = [
        "Nice to meet you",
        "Lets have some good time together",
        "I like to spend sometime wit u."
    ]
    print(random.choice(messages))
def get_timeofday_greeting():
    #collect the time from device and display appropriate greeting
    current_time = datetime.now()
    timeofday_greeting = "Good Morning"
    if current_time.hour > 12 and current_time.hour<17:
        timeofday_greeting = "Good Afternoon"
    elif current_time.hour >= 17 and current_time.hour <22:
        timeofday_greeting = "Good Evening"
    elif current_time.hour >= 22:
        timeofday_greeting = "Hi, THat's late"
    print(timeofday_greeting)  
def welcome2(name):
    #displays a welcome message to user
    messages = [
        "Nice to meet you",
        "Lets have some good time together"
    ]

    print(f"{get_timeofday_greeting()}, {random.choice(messages)}")

def show_menu():
    # displays a set of operations that this bot can do
    print("select a task that i can do for you ")
    print("1. Tell some travelling tips")
    print("2. get current date and time")
    print("3. Tell about tourist places in India")
    print("4. end this chat")
    print("- * - * - * - * - * - ")
    try:
        return int(input("Enter your choice [1-4]: "))
    except:
        print("Only enter choice from 1, 2,3and 4")
        return 0
def date():
    # displays the time and date at the time of chatting
    from datetime import date
    today = date.today()
    print("Today's date is:", today)
    

def travel_tips():
    #These are some travel tips displayed to user
    tips=[
        "Always pack a towel.",
        "Buy a small backpack/suitcase.",
        "Take an extra bank card and credit card with you.",
        "When you go out, take only what you need.",
        "Always carry a lock.",
        "Lunchtime is the best time to visit historical sites.",
        "Get city attraction cards."   
        ]
    print(random.choice(tips))
    print("*************************************************")

def Tourist_places():
    def show_menu2():
        #simply displays these below mentioned choices for user and asks for requirment and prints the data accordingly
        print(" I can help you providing details to explore below parts of India : ")
        print("1. North India")
        print("2. South India")
        print("3. East India")
        print("4. West India")
        print("- * - * - * - * - * - ")
        print()
        try:
        	return int(input("Enter your choice [1-4] to select ur area of intrest: "))
        except:
        	print("Only enter choice from 1, 2,3and 4")
    choice=show_menu2()
    file=open(os.getcwd()+"\\chatbot\\bot_info.txt","r")
    data=file.read().split("***")
    file.close()
    if(choice==None):
        pass
    elif (choice==1):
        print(data[0])
        print("***************************************************")
    elif(choice==2):
        print(data[1])
        print("***************************************************")
    elif(choice==3):
        print(data[2])
        print("***************************************************")
    elif(choice==4):
        print(data[3])
        print("***************************************************")

def bot():
    #these are all functions that bot will use
    greet_and_introduce()
    name = input("your name: ")
    welcome(name)
    get_timeofday_greeting()
    choice=show_menu()
    while choice !=4:
        if (choice==1):
            travel_tips()
        elif(choice==2):
            print(str(datetime.now()))
            print("***********************************")
        elif(choice==3):
            Tourist_places()
        elif(choice==4):
            break
        else:
            print("I don't understand that")
            choice=show_menu()
        choice=show_menu()


bot()
