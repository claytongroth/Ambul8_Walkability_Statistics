import requests
from bs4 import BeautifulSoup
import sys
import re
import csv

count = 0
#open the MCD csv_
MCDlatlonList = []
with open('MCD.csv', 'rb') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        MCDlatlonList.append([row[1], row[0]])

with open('MCD_Walk_Scores.csv', 'a') as csv_file2:
    writer = csv.writer(csv_file2)
    for coords in MCDlatlonList:
        try:
            scrapeURL = 'https://www.walkscore.com/score/loc/lat='+ coords[0] + '/lng=' + coords[1]
            #print scrapeURL
            count += 1
            response = requests.get(scrapeURL)
            html = response.content
            soup = BeautifulSoup(html, 'html.parser')
            name_box = soup.find('span', attrs={'id': 'score-description-sentence'})
            Text = str(name_box)
            WS = (re.findall('\d+', Text ))[-2]
            print "Walkscore is", WS
            rowtowrite = (WS,coords[0], coords[1])
            print rowtowrite
            writer.writerow(rowtowrite)
            print count
        except:
            print "skip"
