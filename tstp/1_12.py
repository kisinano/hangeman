import csv
with open(r'C:\Users\Administrator\Desktop\chengji.csv','r',encoding = 'utf-8') as f:
    r = csv.reader(f,delimiter = ',')
    for i in r:
        print(','.join(i[0:1]))
 
