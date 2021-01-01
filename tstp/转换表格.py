import csv
with open(r'C:\Users\Administrator\Desktop\12.csv','r',encoding = 'UTF-8') as f:
    r = csv.reader(f,delimiter = ',')
    for qu in r :
        print('.'.join(qu))

