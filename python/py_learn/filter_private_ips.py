def f(ip : list(int)) -> list(int):
    filt_ip = []
    for i in ip:
        if(i.split('.')[0] == '10'):
            filt_ip.append(i)
        elif(int(i.split('.')[0]) == 172 and (16 <= int(i.split('.')[1]) <= 31)):
            filt_ip.append(i)
        elif(i.split('.')[0] == '192' and i.split('.')[1] == '168'):
            filt_ip.append(i)
    return filt_ip

def main():
    ips = ["192.168.1.1", "8.8.8.8", "10.0.0.1", "172.16.0.1", "1.1.1.1"]
    res = f(ips)
    print(res)

if __name__ == '__main__':
    main()

