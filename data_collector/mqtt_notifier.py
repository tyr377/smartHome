# -*- coding: utf-8 -*-
'''
Created on 19 Feb 2016
@author: Christian Wichner
'''

import paho.mqtt.client as mqtt


class MqttNotifier(object):
  def __init__(self, host='127.0.0.1', port=1883):
    self.client = mqtt.Client()
    self.client.connect(host, port)
    
  def publish(self, x):
    self.client.reconnect()
    self.client.publish('sensor/%s/' % x[0], '%s,%s' % (x[1], x[2]))