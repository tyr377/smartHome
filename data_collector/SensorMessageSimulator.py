'''
Created on 12 Feb 2016

@author: Christian Wichner
'''

import random
import socket
import sys
import time
import uuid

MCAST_GRP = ''
MCAST_PORT = 4221
MCAST_DLY = 1.0
MCAST_UUID = '%X' % uuid.getnode()

def main(argv):
  sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
  sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 16)
  while True:
    temperature = random.uniform(5,45)
    humidity = random.uniform(0,100)
    message = '%s,%.2f,%.2f' % (MCAST_UUID, temperature, humidity)
    sock.sendto(message, (MCAST_GRP, MCAST_PORT))
    #print('message send: %s' % message)
    time.sleep(MCAST_DLY)


if __name__ == '__main__':
  main(sys.argv)