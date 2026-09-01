import socket
def get_remote_machine_info():
    remote_host = 'www.icicibank.com'
    try:
        ipaddr=socket.gethostbyname(remote_host)
        print("IP address: %s" %ipaddr)
        paddress=socket.inet_aton(ipaddr)#Converting IP Address Into Binary Form
        print("Packed 32 Bit Binary Format = " , paddress)
    except socket.error as err_msg:
        print("%s: %s" %(remote_host, err_msg))

get_remote_machine_info()
