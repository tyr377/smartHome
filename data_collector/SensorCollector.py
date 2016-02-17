#!/usr/bin/python.
# -*- coding: utf-8 -*-
'''
Created on 11 Feb 2016
@author: Christian Wichner
'''

import paho.mqtt.client as mqtt
import socket
import sys

class MqttNotifier(object):
  def __init__(self, host='127.0.0.1', port=1883):
    self.client = mqtt.Client()
    self.client.connect(host, port)
    
  def publish(self, x):
    self.client.reconnect()
    self.client.publish('sensor/%s/' % x[0], '%s,%s' % (x[1], x[2]))
  

class SensorListener(object):
  def __init__(self, port=4221):
    self.sock = socket.socket(
        socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    self.sock.bind(('', port))
  
  def receiveAndNotify(self, notifier):
    message = self.sock.recv(1024).split(',')
    notifier.publish(message)

 
def main(argv):
  listener = SensorListener()
  notifier = MqttNotifier()
  while True:
    listener.receiveAndNotify(notifier)
  

if __name__ == '__main__':
  main(sys.argv)