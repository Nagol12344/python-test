import time, json, urllib, os


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
    response = urllib.request.urlopen('https://raw.githubusercontent.com/Nagol12344/python-test/main/update.json')
    return response.read()

def json_to_dict(json_string):
    return json.loads(json_string)

def check_if_update_available(json1, json2):
    if int(json1['version']) > int(json2['version']):
        return True
    else:
        return False

def check_update():
    file = get_file_from_internet_as_var()
    file1 = json_to_dict(file)
    update = '{"version":"1.0"}'
    update1 = json_to_dict(update)
    check = check_if_update_available(file1, update1)