from subprocess import Popen, PIPE
import time
import csv

# initialising Arrays
tempmaclist = []
temprssilist = []
tempptypelist = []
maclist = []
rssilist = []
ptypelist = []
timelist = []

# table structure is time,macaddress,rssi,packet-type
datab = []
datab.append([])
datab.append([])
datab.append([])
datab.append([])


# Functie voor console-output capturing, line by line -> https://zaiste.net/realtime_output_from_shell_command_in_python/

def run(command):
    process = Popen(command, stdout=PIPE, shell=True)
    while True:
        line = process.stdout.readline().rstrip()
        if not line:
            break
        yield line


if __name__ == "__main__":
    # miniterm is een serial reader/terminal voor o.a. Nodemcu, Baudrate = 57600(Uit MACsnif.ino), /dev/ttyUSB voor linux, /dev/cu.SLAB_USBtoUAR voor osx, COM8? voor windows
    for path in run('miniterm /dev/ttyUSB0 57600'):
        print(path)
        datab[0].append(time.strftime("%d-%m-%Y %H:%M:%S"))
        # Caputing voor bepaalde datatypes per line
        tempmaclist.append(path[6:23])
        temprssilist.append(path[27:32])
        tempptypelist.append(path[0:2])

for line in tempmaclist:
    macv = line.decode()
    # moet uit Byte datatype in python naar strings moeten decode, voor integratie in database.
    maclist.append(macv)

for line in temprssilist:
    rssiv = line.decode()
    rssilist.append(rssiv)

for line in tempptypelist:
    ptypev = line.decode()
    ptypelist.append(ptypev)


for add in maclist:
    datab[1].append(add)

for add in rssilist:
    datab[2].append(add)

for add in ptypelist:
    datab[3].append(add)

# Draait nested list for easier csv writing per row.
databtwist = list(map(list, zip(*datab)))


# scrijft naar CSV bestand, Locatie moet verandered worden(pi/laptop)
with open("/home/sga/kosme/datasnif.csv", "a") as csv_file:
    datasnifwrite = csv.writer(
        csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for row in databtwist:
        datasnifwrite.writerow(row)
