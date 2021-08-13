import os

ip = raw_input("Please type the subnet you want to investigate ")

host = 0
for host in range(1,255,1):
    cmd = 'shodan host  '  +ip + "."  + str(host)
    print("......................" + cmd + "....................")
    os.system(cmd)
    print("......................" + "Done" + "....................")