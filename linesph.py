import csv
hlist=[]
uhlist=[]
unique = []
with open('/home/sga/kosme/datatest.csv', 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        # print(", ".join(row[1:9]))
        # print(row[1][0:2])
        hlist.append(row[1][0:2])
        # print (row[1][9:26])
    for hour in hlist:
        if hour not in uhlist:
            uhlist.append(hour)   
        
    for hour in uhlist:
        hour=[]
        for row in spamreader:
            print (row[1][9:26])
            # if (row[1][9:26]) not in hour:
            #     hour.append(row[1][9:26])
##22-01-2019, 10:41:18,64:a2:f9:ea:7b:30,-16,40





    
print(len(unique))




