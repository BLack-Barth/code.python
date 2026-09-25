#rich | pyfiglet | keyword | range
#list=[,] | sets={,} | tuples=(,) | dict={key:value,}
# range(start,stop,step)
# input -> str |  int(input) -> int | float(input) -> float
# import getpass
#password = getpass.getpass('Please enter psswd:')
# def => define
# https://jsonplaceholder.typicode.com/posts
from rich import print
import requests

URL = 'https://jsonplaceholder.typicode.com/users'
data = {
    "userId" : 11,
    "name" : "black bart",
    "job" : "bug bounty hunter"
}
response = requests.post(URL,data)
print(f'code status : {response.status_code}')
print(response.json())