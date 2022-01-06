import os
import time
import datetime

ip = int(raw_input("How many times do you want to commit? \n"))
autoPush = raw_input("Auto git push when commited? (y/n) \n")

for i in range(ip):
        date = datetime.datetime.now().strftime("%d-%b-%Y(%H:%M:%S)")
	fp = open(date + ".py", 'w')
	fp.write('print(\"' + date + '\")')
	fp.close()
	os.system('git add \"' + date + '.py\"')
	os.system('git commit -m \"New Commit at:' + date + '\"')

print("Commited " + str(ip) + " times")

if autoPush == "y":
	os.system('git push')
