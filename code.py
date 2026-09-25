#rich | pyfiglet | keyword | range
#list=[,] | sets={,} | tuples=(,) | dict={key:value,}
# range(start,stop,step)
# input -> str |  int(input) -> int | float(input) -> float
# import getpass
#password = getpass.getpass('Please enter psswd:')
# def => define
from rich import print

def addnum(num1 , num2):
    return num1 + num2

num1 = int(input('Enter number 1:'))
num2 = int(input('Enter number 2:'))

result = addnum(num1 , num2)

print('result = ' + str(result))