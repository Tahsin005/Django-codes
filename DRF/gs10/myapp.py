import requests
import json

URL= "http://127.0.0.1:8000/studentapi/"

def get_data(id = None):
    data = {}
    if id is not None:
        data = {'id' : id}
    headers = {
        'content-Type' : 'application/json'
    }
    
    json_data = json.dumps(data)
    
    r = requests.get(url = URL, headers = headers, data = json_data)
    data = r.json()
    print(data)

def post_data():
    data = {
        'name' : 'mohit',
        'roll' : 190,
        'city' : 'yyy'
    }
    headers = {
        'content-Type' : 'application/json'
    }
    
    json_data = json.dumps(data)
    
    r = requests.post(url = URL, headers = headers, data = json_data)
    data = r.json()
    print(data)
    
    
def update_data():
    data = {
        'id' : 4,
        'name' : 'Cubox',
        'city' : 'nice'
    }
    headers = {
        'content-Type' : 'application/json'
    }
    
    json_data = json.dumps(data)
    
    r = requests.put(url = URL, headers = headers, data = json_data)
    data = r.json()
    print(data)
    
def delete_data():
    data = {
        'id' : 4,
    }
    headers = {
        'content-Type' : 'application/json'
    }
    
    json_data = json.dumps(data)
    
    r = requests.delete(url = URL, headers = headers, data = json_data)
    data = r.json()
    print(data)

delete_data()
# update_data() 
# post_data()
# get_data(1)