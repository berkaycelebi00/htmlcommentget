import requests
from optparse import OptionParser

url = ""


def optParser():
    parser = OptionParser()
    parser.add_option("-u", "--url", dest="url",
                  help="Please write your url")
    (options, args) = parser.parse_args()
    if not options.url:   
        parser.error('Url is not given')
    return options
    


def getComments(url):
    data = requests.get(url).text
    i = 0
    empStr = ""
    while i < len(data):
        if data[i] == "<" and data[i+1] == "!" and data[i+2] == "-" and data[i+3] == "-":
            while i < len(data):
                empStr+=data[i]
                if data[i] == "-" and data[i+1] == "-" and data[i+2] == ">":
                    empStr+="-->\n"
                    break
                i += 1
        i += 1
    return empStr
    

url = optParser().url
print(getComments(url))