from pprint import pprint
import os
import httpx
url = "https://jsonplaceholder.typicode.com/todos"
response = httpx.get(url=url)
data = response.json()

os.mkdir("todos")
os.chdir("todos")
for todo in data:
    with open(f"{todo['id']}.txt", "w") as f:
        f.write(f"Title: {todo['title']}\n")
        f.write(f"User Id: {todo['userId']}\n")

