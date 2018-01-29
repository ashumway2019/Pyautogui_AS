import pyautogui as pg
import time
import webbrowser 

# Sets points to zero at start
points = 0

#Question 1
#Question for player
answer = pg.prompt("""
What college do you want to go to?
Yale
Brown
USC
Dartmouth
Don't go
""")


#Gives points based on choice
if answer == "Yale":
    points += 1
elif answer == "Princeton":
    points += 2
elif answer == "USC":
    points += 5
elif answer == "Dartmouth":
    points += 4
elif answer == "Don't go":
    points += 3

#Question 2
#Question for player
answer = pg.prompt("""
What would you rather do?
Go shopping
Write a book
Party
Go on a run
Design clothes
""")

#Gives points based on choice
if answer == "Design clothes":
    points += 1
elif answer == "Go shopping":
    points += 2
elif answer == "Write a book":
    points += 3
elif answer == "Go on a run":
    points += 4
elif answer == "Party":
    points += 5
    
answer = pg.prompt("""
What is your dream job?
Author
Designer
Socialite
Businessman
Editor
""")

if answer == "Designer":
    points += 1
elif answer == "Socialite":
    points += 2
elif answer == "Author":
    points += 3
elif answer == "Editor":
    points += 4
elif answer == "Businessman":
    points += 5

answer = pg.prompt("""
Where would you like to be right now?
Paris 
The Hamptons
At Dartmouth
Foreign country
Chilling in hyour home
""")

if answer == "Paris":
    points += 1
elif answer == "The Hamptons":
    points += 2
elif answer == "At Dartmouth":
    points += 3
elif answer == "Foreign country":
    points += 4
elif answer == "Businessman":
    points += 5
    
#End of survey
pg.alert("You are...")

#Blair
if points < 6:
    pg.alert("Blair Waldorf")
    webbrowser.open("https://typeset-beta.imgix.net/elite-daily/2017/05/08091733/blair-waldorf-gossip-girl.jpg")
#Serena
if points >=6 and points <9:
    pg.alert("Serena Vanderwoodsen")
    webbrowser.open("https://vignette.wikia.nocookie.net/degrassi/images/5/57/Serena-van-der-woodsen.jpg/revision/latest?cb=20140111173557")
#Dan
if points >=9 and points <=12:
    pg.alert("Dan Humphrey")
    webbrowser.open("https://vignette.wikia.nocookie.net/gossipgirl/images/9/91/Dan_humphrey.jpg/revision/latest?cb=20160829014238")
#Nate
if points >12 and points <=16:
    pg.alert("Nate Archibald")
    webbrowser.open("https://typeset-beta.imgix.net/elite-daily/2017/05/08023505/nate-archibald.jpg?w=800&h=800&auto=format&q=70&fit=crop&crop=faces")
#Chuck
if points >=17 and points <=20:
    pg.alert("Chuck Bass")
    webbrowser.open("https://upload.wikimedia.org/wikipedia/en/a/a2/Chuck_Bass_Season_3.jpg")
    


