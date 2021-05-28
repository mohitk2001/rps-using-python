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
def Decider(computer,user,db):
    print("Computer choice is "+computer + " and Player Choice is "+user)
    print("So result is :")
    if(condition[computer][user]==1):
        print("Player Won 🥇")
    elif(condition[computer][user]==0):
        print("Computer won 🥇")
    elif(condition[computer][user]==0.5):
        print("Tie 🥈")


exist=False       
for x in db:
    if user == x:
        print(user,x)
        exist=True
        
        
print(exist)
if(exist):
    Decider(computer,user,db)
else:
    print(f"Player you picked {user}, watch your pick up options:{db} ")
