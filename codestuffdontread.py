import time


def end():
    print('You have failed')
    time.sleep(2)
    print('Please wait...')
    time.sleep(7)
    print('Now ending all code, please wait...')
    time.sleep(10)
    print('Done!')
    time.sleep(2)

def win1():
    time.sleep(2)
    print('You run into the trees')
    time.sleep(2)
    print('The villagers dont follow you')
    time.sleep(2)
    print('You passed the first level')
    time.sleep(2)
    print('It only gets harder after then this')
    exec(open("notmain.py").read())

def updatecheck():
    print('no new updates needed')