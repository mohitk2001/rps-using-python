import random

condition={
    "rock":{
        "rock":0.5,
        "paper":1,
        "scissor":0
    },
    "paper":{
        "rock":0,
        "paper":0.5,
        "scissor":1
    },
    "scissor":{
        "rock":1,
        "paper":0,
        "scissor":0.5
    }
}

db=['rock','paper','scissor']
index=random.randint(0,2)
computer=db[index]
# print(computer)
user=input("Player choose your pick up among rock,paper and scissor: ")
def Decider(computer,user):
    print("Computer choice is "+computer + " and User Choice is "+user)
    print("So result is :")
    if(condition[computer][user]==1):
        print("User Won 🥇")
    elif(condition[computer][user]==0):
        print("Computer won 🥇")
    elif(condition[computer][user]==0.5):
        print("Tie 🥈")


Decider(computer,user)
