from subprocess import Popen, PIPE
import time
import csv


tempmaclist= []
temprssilist= []
tempptypelist = []
maclist = []
rssilist= []
ptypelist = []
timelist = []

# table structure is time,macaddress,RSSI,packet type
datab=[]
datab.append([])
datab.append([])
datab.append([])
datab.append([])


def run(command):
    process = Popen(command, stdout=PIPE, shell=True)
    while True:
        line = process.stdout.readline().rstrip()
        if not line:
            break
        yield line

if __name__ == "__main__":
    for path in run ('miniterm /dev/ttyUSB0 57600'):
        print (path)
        datab[0].append(time.strftime("%d-%m-%Y %H:%M:%S"))
        tempmaclist.append(path[6:23])
        temprssilist.append(path[27:32])
        tempptypelist.append(path[0:2])

for line in tempmaclist:
    macv= line.decode()
    maclist.append(macv)

for line in temprssilist:
    rssiv= line.decode()
    rssilist.append(rssiv)

for line in tempptypelist:
    ptypev= line.decode()
    ptypelist.append(ptypev)


for add in maclist:
    datab[1].append(add)

for add in rssilist:
    datab[2].append(add)

for add in ptypelist:
    datab[3].append(add)

#####rotates nested list for easier csv writing per row.
databtwist = list(map(list, zip(*datab)))


with open("/home/sga/kosme/datasnif.csv", "a") as csv_file:
    datasnifwrite = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for row in databtwist:
        datasnifwrite.writerow(row)