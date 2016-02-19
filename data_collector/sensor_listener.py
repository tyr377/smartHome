#!/usr/bin/python.
# -*- coding: utf-8 -*-
'''
Created on 19 Feb 2016
@author: Christian Wichner
'''

import socket


class SensorListener(object):
  def __init__(self, port=4221):
    self.sock = socket.socket(
        socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    self.sock.bind(('', port))
  
  def receiveAndNotify(self, notifier):
    message = self.sock.recv(1024).split(',')
    notifier.publish(message)
    