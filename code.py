#rich | pyfiglet | keyword | range
#list=[,] | sets={,} | tuples=(,) | dict={key:value,}
# range(start,stop,step)
# input -> str |  int(input) -> int | float(input) -> float
# import getpass
#password = getpass.getpass('Please enter psswd:')
from rich import print
name = input('name :')
city = input('city :')
with open("test.txt","a",encoding="utf-8") as moh :
    moh.write(f"\nname is : {name}")
    moh.write(f"\ncity is : {city}")