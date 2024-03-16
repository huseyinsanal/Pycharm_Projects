import requests
import json

#GET
#user_input = input("enter id: ")
#get_url = f"https://jsonplaceholder.typicode.com/todos/{user_input}"

#get_response = requests.get(url)
#print(get_response.json())

#POST
to_do_item = {"userId" : 2, "title" : "my to do", "completed" : False}
post_url = "https://jsonplaceholder.typicode.com/todos"

#Optional Header
header = {"Content-Type" : "application/json"}

#post_response = requests.post(post_url,json=to_do_item,headers=header)
post_response = requests.post(post_url,data=json.dumps(to_do_item),headers=header)

print(post_response.json())
#print(json.dumps(to_do_item))