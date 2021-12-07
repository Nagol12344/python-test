import time, json, os
from urllib.request import urlopen


def end1():
    print('You have failed')
    time.sleep(2)
    print('Please wait...')
    time.sleep(7)
    print('Now ending all code, please wait...')
    time.sleep(10)
    print('Done!')
    time.sleep(2)
    exit()


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

def get_file_from_internet_as_var():
    response = urlopen('https://raw.githubusercontent.com/Nagol12344/python-test/main/update.json')
    return response.read()

def json_to_dict(json_string):
    return json.loads(json_string)

def check_if_update_available(json1, json2):
    if float(json1['version']) > float(json2['version']):
        return False
    else:
        return True

def check_update():
    file = get_file_from_internet_as_var()
    file1 = json_to_dict(file)
    update = '{"version" : "1.4"}'
    update1 = json_to_dict(update)
    check = check_if_update_available(file1, update1)
    if check == True:
        print("Your up to date!")
    if check == False:
        print("There is an update available!\nPlesase download it on github!");
        os.system("error")
