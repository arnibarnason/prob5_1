from bs4 import BeautifulSoup
import requests as r
from getpass import getpass
import argparse

# From stackoverflow, originally from Steven Bethard on Google groups
# Gives error message and shows help if parameters are incorrect
class MyParser(argparse.ArgumentParser):
    def error(self, message):
        sys.stderr.write('error: %s\n' % message)
        self.print_help()
        sys.exit(2)


parser = argparse.ArgumentParser(description="""Returns a project on Myschool. First parameter (optional) preceding a '-c' contains a comment to the teacher and the second parameter (optional) preceding a '-f' contains the path (as a string) of the file to turn in""")
parser.add_argument('-c', nargs='?', action='store', dest='c', help='Comment to the teacher')
parser.add_argument('-f', nargs='?', action='store', dest='f', help='Path to the file to turn in')
parser.add_argument('p', help='Path to the projects website')
args = parser.parse_args()
url = args.p

authentication = (input('Username: '), getpass())
res = r.get(url, auth=authentication)

filePath = args.f
comment = args.c

soup = BeautifulSoup(res.text)

formURL = soup.find('form', id='form1')['action']

if not filePath is None:
    fileToUpload = {'file': open(filePath, 'rb')}
else:
    fileToUpload = {}

data = {'athugasemdnemanda': comment}

rex = r.post('https://myschool.ru.is/myschool/'+formURL, 
    data=data, files=fileToUpload, auth=authentication)
