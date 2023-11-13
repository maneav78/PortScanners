import socket
import time

start_time = time.time()
target =  input("Enter the host: ")
m_ip = socket.gethostbyname(target)
print("Starting scanning on host: ", m_ip)

for i in range(50,500):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn = s.connect_ex((m_ip, i))
    if(conn == 0):
        print('Port %d: OPEN' % (i,))
    s.close()
print('Time taken: ', time.time() - start_time)