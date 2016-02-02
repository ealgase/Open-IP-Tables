import os
ip=open('index.sh','w')
ip.write('#/bin/bash\n')
for i in range(65536):
    ip.write('sudo iptables -I INPUT -p tcp --dport '+ str(i)+' --syn -j ACCEPT\necho Port '+ str(i) +' opened.\n')
    print('Port '+ str(i)+' added.')
ip.close()
os.system('clear')
os.system('chmod 777 index.sh')
os.system('sudo bash index.sh')
