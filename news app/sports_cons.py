#
#   Sports news client
#   Connects SUB socket to tcp://localhost:5556

import sys
import zmq

#  Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://localhost:5556")

news_filter="SP"
# Python 2 - ascii bytes to unicode str
if isinstance(news_filter, bytes):
    news_filter = news_filter.decode('ascii')
i=0
socket.setsockopt_string(zmq.SUBSCRIBE,news_filter)
print("SPORTS NEWS")
while(i<4):
    news_string = socket.recv_string()
    print news_string[2:]
    i=i+1
    #if news_string[:2]==news_filter:
    #	print news_string[2:]
   	#	i = i+1
