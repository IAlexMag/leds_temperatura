import os

ips= []
ip_range= '192.168.100.'

def scan(ip_range):
    for x in range(1,255):
        ip = ip_range + str(x)
        result = os.popen(f'ping {ip}').read()
        lines = result.split('\n')
        #print(lines)
        if "0%" in lines[9] and "inaccesible" not in lines[2]:
            ip_add = lines[1].split()
            ip_add_2 = ip_add[3]
            ips.append(ip_add_2)

def imp_ip():
    for ip in ips:
        print(ip)

scan(ip_range)
imp_ip()

'''
txt = "Welcome to the jungle"
x = txt.split()
print(x)
'''