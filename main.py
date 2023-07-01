import os
import socket


def get_my_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        ip_address = s.getsockname()[0]
    except socket.error:
        ip_address = "127.0.0.1"
    finally:
        s.close()
    return ip_address


IPAddress = '192.168.43.138'

print(f"The file server ip is {IPAddress}")
