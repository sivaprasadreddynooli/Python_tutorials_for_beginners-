#this is the different way of imporing the request from urllib ,
#this is different from the earlier method , this would be explained later
from urllib import request

goo_url = 'http://www.sample-videos.com/csv/Sample-Spreadsheet-10-rows.csv'

def dwnld_from_url(csv_url):
    response = request.urlopen(csv_url)
    text = response.read()
    csv_text = str(text)
    lines = csv_text.split("\\n")
    dest_url = r'goo.txt'
    fw = open(dest_url,'w')
    for line in lines:
        fw.write(line + "\n")
    fw.close()


dwnld_from_url(goo_url)
