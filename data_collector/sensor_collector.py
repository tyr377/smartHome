#!/usr/bin/python.
# -*- coding: utf-8 -*-
'''
Created on 11 Feb 2016
@author: Christian Wichner
'''

import sys
from mqtt_notifier import MqttNotifier
from sensor_listener import SensorListener


def main(argv):
  listener = SensorListener()
  notifier = MqttNotifier()
  while True:
    listener.receiveAndNotify(notifier)
  

if __name__ == '__main__':
  main(sys.argv)