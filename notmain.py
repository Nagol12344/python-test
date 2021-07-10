import time
import random
from codestuffdontread import end

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
elif sn == '2':
    print('you keep running')
    print('after 2 more hours you run off a cliff')
    end()
