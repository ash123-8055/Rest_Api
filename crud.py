import requests as req

BASE_URL = "http://localhost:8000/"

def post_info(url, value):
    res = req.post(url, json=value)
    print(res.text)

def get_info(url):
    res = req.get(url)
    print(res.text)
    print(res.status_code)

def del_info(url):
    res = req.delete(url)
    print(res.text)
    print(res.status_code)

def put_info(url, value):
    res = req.put(url, json=value)  
    print(res.text)
    print(res.status_code)

def patch_info(url, value):
    res = req.patch(url, json=value)
    print(res)
    print(res.text)
    print(res.status_code)

data = {"first_name": "John", "last_name": "Marsh"}
another_data = {"first_name": "Halo"}  

get_info(BASE_URL+ "get_items")
post_info(BASE_URL + "get_items", data)
get_info(BASE_URL)
put_info(BASE_URL, data)
get_info(BASE_URL)
patch_info(BASE_URL, another_data)
get_info(BASE_URL)
del_info(BASE_URL)
get_info(BASE_URL)
