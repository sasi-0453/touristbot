"""
    1.*This is a travellerbot.
      *This travellerbot greets the user,introduce itself to the user and ask for the name  of the user.
      *travellerbot provide the following information.
    2.travellerbot  will greet and welcomes the user.
    3.travellerbot will ask the user to enter in which direction they want to explore. travellerbot will respond according to
      how it was designed .It will give some choices to the user.
    4.traveller will respond to users input appropriately.
    """
import random
from datetime import datetime


def greet_and_introduce():
    greet = [
        "Hi! I am traveller.Hope you are safe in this pandemic.I am here to help you provide inforamtion about travelling .May I know your name please? ",
        "hello! This is travellerbot.Hope you are doing good.I will descibe the facts and importance of tourist spots.Your name please?",
        "what's up! I am travellerbot. How can I help you to provide information about places to visit? what is your name?"
    ]

    print(random.choice(greet))


def timegreeting():
    time_point = datetime.now()
    greet_on_time = "display the greetings based on time"
    if (time_point.hour > 12 and time_point.hour < 17):
        greet_on_time = "very good morning"
        print(greet_and_introduce)
    elif (time_point.hour >= 17 and time_point.hour < 22):
        greet_on_time = "Good evening"
        print(greet_and_introduce)
    elif (time_point.hour >= 22):
        greet_on_time = "hi,that's late"
    return greet_on_time


def HI(name):
    messages = [
        "Nice to meet you",
        "Lets have some good time together",
        "lets move on to find the wonderful places to visit",
        "happy browsing",
        "let's start searching places to visit"
    ]

    print(f"{timegreeting()}, {random.choice(messages)}")


def explore():
    print("1.choose option 1 to do CALCULATIONS : ")
    print("2.GET CURRENT TIME")
    print("3.TO KNOW THE FACTS AND BESTPLACES IN NORTH INDIA TO VISIT ")
    print("4.TO KNOW THE FACTS AND BESTPLACES IN SOUTH INDIA TO VISIT ")
    print("5.TO KNOW THE FACTS AND BESTPLACES IN  EAST INDIA TO VISIT ")
    print("6.TO KNOW THE FACTS AND BESTPLACES IN  WEST INDIA TO VISIT ")
    print("7.TOURISM TIPS")
    print("8.STOP EXPLORING")
    print("*********************")
    try:
        return int(input("NOW YOU CAN CHOOSE OPTIONS FROM[1-8]"))
    except:
        print("You have possibility to select options from 1 to 8 only! ")
        return 0;


def calculation():
    expr = input("Enter an expression: ")
    print("Here you can do calulations.")
    try:
        print("Result = ", eval(expr))
    except Exception as e:
        print(str(e))


def tips():
    tips = ["1. Always pack a towel",

            "2.Buy a small backpack/suitcase",

            "3. Take an extra bank card and credit card with you",

            "4.When you go out, take only what you need.",

            "5.Always carry a lock.",

            "6.Lunchtime is the best time to visit historical sites.",

            "7. Get city attraction cards."
            ]
    print(tips)


def north():
    facts = ["1.Agra : Home to one of the 7 wonders of the world, the Taj Mahal ** best time to visit: oct to mar",

             "2.Amritsar,Punjab : Home of the glorious Golden Temple, the iconic city of Amritsar **Best Time: October to March",

             "3.Haridwar,UK  : Considered as one of the seven holiest cities in India,Haridwar has a perennial mystical air around it, and is the perfect holiday option for anyone seeking spiritual connection as well as a chance to indulge in and get closer to nature **Best Time: Throughout the year",

             "4.Leh Ladakh : A land like no other with superabundance of attractions to visit and phantasmagoric and fabulous landscapes ** best time to visit: jun to sep",

             "5.Shimla,Himachal Pradesh : Probably the most popular hill station in northern India  ** Best Time: October to June",

             "6.Vaishno Devi Mandir,JK :this town is the holy cave temple of Mata Vaishnodevi, with spirituality and vibrancy lingering in the atmosphere.** Best Time: Throughout the year "
             ]
    print(facts)


def south():
    a = [
        "1.Alleppey,Kerala :   Extremely famous for its beautiful backwaters, the city of Alleppey in Kerala is also known for its beaches, temples and traditional boat races   ** Best Time: June to March ",

        "2.Andaman&Nicobar islands :    Lagoons of crystal clear water and scenic beaches topped with a little bit of history make Andaman and Nicobar one of the most perfect choices for an enjoyable     ** best time to visit: oct to june",

        "3.coorg,karnataka : This popular coffee producing hill station is not only popular for its beautiful green hills and the streams cutting right through them. It also stands as a popular destination because of its culture and people.        ** best time to visit: oct to mar   ",

        "4.Kodaikanal,TN : Green Valley View       ** Best Time: September to May",

        "5.Madurai,TN : Madurai Meenakshi Amman Temple      ** Best Time: October to March",

        "6.munnur,kerala : 	tea gardens,little hill stations , famous for its tea estates, exotic lush greenery and craggy peaks, is located in the Western Ghats and is one of the best places to visit in Kerala.    	** best time to visit:september to may",

        "7.Mysore,Karnataka : It is replete with the history of its dazzling royal heritage, intricate architecture, its famed silk sarees, yoga, and sandalwood, to name just a few        ** Best Time: Throughout the year",

        "8.ooty,Tamilnadu : For every mountain lover, the very idea of travelling to the city known as the Queen of the Hills holds an allure like no other     ** Best Time: Throughout the year",

        "9.Tirupati,Ap : Home to many heritage sites, and a plethora of ancient temples and monuments, Tirupati is one of the oldest cities of India and finds mention in plenty of ancient texts       ** Best Time: September to March",
        ]
    print(a)


def east():
    b = [
        "1.Bodh Gaya :  It was here under the Bodhi tree that Gautama Buddha attained enlightenment. The place is bustling with pilgrims all through the year who come to pay their homage in the monasteries, shrines and temples     ** Best Time: October to March  ",

        "2.Cherrapunjee,Meghalaya : Among the wettest place on the Earth, Cherrapunjee with its clean and pristine surroundings is an excellent place to sit back and unwind.       ** Best Time: September to May      ",

        "3.darjeeling,west bengal : mesmerising sunrises, the untouched beauty of the hills     ** best time to visit:feb to march and sep to dec       ",

        "4.konark,Orissa : Konark, in the state of Orissa is rebnowned world over for the Sun Temple       ** Best Time: September to March   ",

        "5.Puri,Orissa : One of the four must-visit pilgrimage sites for Hindus (Char-Dham), Puri is a beach city with its most famous attraction as the Jagannath temple.       ** Best Time: July to March     ",

        "6.Varanasi,UP : The city which can be aptly described as a melting pot where both life and death come together.        ** Best Time: October to March      "
        ]
    print(b)


def west():
    c = [
        " 1.Ajanta and Ellora Caves   :  the magnificent paintings of Ajanta and well-carved sculptures of Ellora. The rock-cut caves containing carvings are the finest example of Indian paintings and sculpture.    ** Best Time: June to March ",

        "2.Goa   :  you think of sandy beaches, amazing parties, beautiful little villages, delicious food, and a magical holiday experience        ** best time to visit: oct to march ",

        "3.Hampi,Karnataka : this place is a historical delight for travellers. Surrounded by 500 ancient monuments, beautiful temples, bustling street markets, bastions, treasury building and captivating remains of Vijayanagar Empire, Hampi is a backpacker's delight.        **Best Time: October to March.  ",

        "4.Kutch,Gujarath    :   Kutch Desert Wildlife Sanctuary **Best Time: July to March  ",

        "5.Mahabaleshwar  : A hill town in Western Ghats, apart from its strawberries, Mahabaleshwar is also well known for its numerous rivers, magnificent cascades and majestic peaks.       ** Best Time: October to June  ",

        "6.Udaipur,Rajasthan :  This 'Venice of the East' has an abundance of natural beauty, mesmerising temples and breathtaking architecture which makes it a must-visit destination in India.       ** Best Time: October to March "
        ]
    print(c)


def travellerbot():
    greet_and_introduce()
    name = input("your name: ")
    HI(name)
    choice = explore()
    while choice != 8:
        if (choice == 1):
            calculation()
            print("----------------------------------------------------------")
        elif (choice == 2):
            print(str(datetime.now()))
            print("----------------------------------------------------------------")
        elif (choice == 3):
            north()
            print("----------------------------------------------------------------------")
        elif (choice == 4):
            south()
            print("---------------------------------------------------------------------------")
        elif (choice == 5):
            east()
            print("--------------------------------------------------------------------")
        elif (choice == 6):
            west()
            print("--------------------------------------------------------------------")
        elif (choice == 7):
            tips()
            print("------------------------------------------------------------------")
        elif (choice == 8):
            print("I dont understand that")
            print("-------------------------------------------------------------------")
            choice = explore()
        choice = explore()


travellerbot()