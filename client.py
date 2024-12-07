import requests
import json
import sched
import time

def init_req():
    url_init = "http://127.0.0.1:8000/init"
    response_init = requests.get(url_init)
    if(response_init.status_code == 200):
        return{"message":f"__CORRECT__"}
    return{"message":f"__ERROR__"}

def list_req():
    url_list = "http://127.0.0.1:8000/list"    
    response_list = requests.get(url_list)
    
    dictionary = json.loads(response_list.text)
    for example in dictionary:
        print(example)

def imulate(scheduler):
    list_req()
    s.enter(15, 1, imulate, (scheduler,))
    print('______________')

print('__START__')
init_req()

s = sched.scheduler(time.time, time.sleep)
s.enter(1, 1, imulate, (s,))
s.run()

print('__STOP__')
