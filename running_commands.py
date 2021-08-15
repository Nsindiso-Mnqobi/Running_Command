import os
from datetime import date

today= date.today()
Date = str(today.strftime("%d_%m_%y"))
ip = input("Please type the subnet you want to investigate? ")
with open("Shodan_logs_"+Date+".txt", "w+") as file:
    print("File has been created")
    
host = 0

for host in range(1,3,1):

    cmd = 'ping -c2 '  + ip + "."  + str(host) + " >> "+ "Shodan_logs_" + Date +".txt"
    print("......................" + ip +"."+ str(host) + "....................")
    os.system(cmd)
    print("......................" + "Done"+ "....................")
    
        