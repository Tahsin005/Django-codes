import requests
import json

URL= "http://127.0.0.1:8000/studentapi/"

def get_data(id = None):
    data = {}
    if id is not None:
        data = {'id' : id}
    json_data = json.dumps(data)
    r = requests.get(url = URL, data = json_data)
    data = r.json()
    print(data)

def post_data():
    data = {
        'name' : 'mohit',
        'roll' : 190,
        'city' : 'yyy'
    }
    
    json_data = json.dumps(data)
    
    r = requests.post(url = URL, data = json_data)
    data = r.json()
    print(data)
    
    
def update_data():
    data = {
        'id' : 3,
        'name' : 'Cubox',
        'roll' : 70,
        'city' : 'nice'
    }
    
    json_data = json.dumps(data)
    
    r = requests.put(url = URL, data = json_data)
    data = r.json()
    print(data)
    
def delete_data():
    data = {
        'id' : 6,
    }
    
    json_data = json.dumps(data)
    
    r = requests.delete(url = URL, data = json_data)
    data = r.json()
    print(data)

# delete_data()
# update_data() 
post_data()
# get_data()
    
    
    
    