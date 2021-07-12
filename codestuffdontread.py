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
    import json
    test2 = '0'
    json_data = '{"update" : "1.0"}'
    parsed_json = (json.loads(json_data))
    class Test(object):
        def __init__(self, data):
	        self.__dict__ = json.loads(data)

    test1 = Test(json_data)
    if test1.update == '1.0':
        test2 = '1'
    if test2 == '0':
        print('You need to update, get the update at the github')
    elif test2 == '1':
        print('Your up to date')
    