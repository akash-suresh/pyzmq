import time
import zmq

def producer():
    context = zmq.Context()
    zmq_socket = context.socket(zmq.PUSH)
    zmq_socket.bind("tcp://127.0.0.1:5557")
    # Start your result manager and workers before you start your producers
    while(1):
        message = { 'String': 'Welcome to Elections 2015 \n Enter your vote \n 1. BJP \n 2. Congress \n 3. AAP \n 4. NULL'}
        zmq_socket.send_json(message)

producer()