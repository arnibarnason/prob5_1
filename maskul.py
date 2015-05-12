from bs4 import BeautifulSoup
import requests as r
from getpass import getpass
import argparse

parser = argparse.ArgumentParser(description="""Returns a project on Myschool. First parameter preceding a '-c' contains a comment to the teacher and the second parameter preceding a '-f' contains the path of the file to turn in""")
parser.add_argument('p', help='Path to the projects website')
#parser.add_argument('-c', '--comment', nargs='?', default='', help='Comment to the teacher')
#parser.add_argument('-f', action='store_true', default='',help='Path to the file to turn in')
args = parser.parse_args()

url = args.p

authentication = (input('Username: '), getpass())
res = r.get(url, auth=authentication)

filePath = input("Path to the file: ")# args.-foo
comment = input("Comment for the teacher: ")#args.c

soup = BeautifulSoup(res.text)

formURL = soup.find('form', id='form1')['action']

fileToUpload = {'file': open(filePath, 'rb')}
data = {'athugasemdnemanda': comment}

rex = r.post('https://myschool.ru.is/myschool/'+formURL, 
        data=data, files=fileToUpload, auth=authentication)
