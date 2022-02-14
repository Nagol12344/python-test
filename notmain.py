import time
import random
from codestuffdontread import end1
wood = False
food = False

atu = 'Whats your pick? '

time.sleep(2)
print('You have been runing for hours')
time.sleep(4)
print('do you want to stop?')
time.sleep(2)
print('type 1 for yes')
print('type 2 for no')
sn = input(atu)
if sn == '1':
    print('you stop running')
    time.sleep(3)
    print('you sit down')
    time.sleep(2)
    print('You take a quick nap and wake up about 2 hours later')
    time.sleep(3)
    print('what do you want to do now?')
    time.sleep(3)
    print('Type 1 to explore')
    print('Type 2 to bulid something')
    print('Type 3 to go hunting')
    print('Type 4 to climb a tree')
    time.sleep(2)
    fobml = int(input(atu))
    if fobml == 1:
        print('you find a crab')
        food = True
        foodname = "crab"
        print('good job')
    if fobml == 2:
        print('What would you like to bulid?')
        print('Type 1 for a house')
        print('Type 2 for a shed')
        print('Type 3 for a fire')
        print("Type 4 for a shelter")
        BUILD = int(input(atu))
        if BUILD == 1:
          print("You start breaking down trees")
          time.sleep(3)
          print("You realise that you dont know how to bulid a house")
          time.sleep(2)
          print("You earned wood!!!!!!")
          wood = True
        if BUILD == 2:
          print("You start breaking down trees")
          time.sleep(3)
          print("You made a small shed")
          time.sleep(1)
          print("Its a nice shed")
          time.sleep(1)
          house = True
          housename = "Shed"
        if BUILD == 3:
         print("You gather some wood for a fire")
         time.sleep(2)
         RNG = random.randint(1,100)
         #print("RNG "+RNG)
         if RNG > 50:
           print("The fire lit!")
         else:
            print("The fire set the forest ablaze, killing you")
            end1()
        if BUILD = 4:
          print("")
    if fobml == 3:
        print("You grab a stick and start hunting")
        time.sleep(3)
        print('You find a deer')
        food = True
        foodname = "dear"
        print('Noice')
    if fobml == 4:
        print('You climb a tree')
        time.sleep(3)
        print("You find nothing")
        time.sleep(2)
        print("You wasted time")
elif sn == '2':
    print('you keep running')
    print('after 2 more hours you run off a cliff')
    end1()

