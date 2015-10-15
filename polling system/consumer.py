import time
import zmq
import random

def consumer():
    voter_id = random.randrange(1,10005)
    print "Voter ID #%s" % (voter_id)
    context = zmq.Context()
    # recieve work
    consumer_receiver = context.socket(zmq.PULL)
    consumer_receiver.connect("tcp://127.0.0.1:5557")
    # send work
    consumer_sender = context.socket(zmq.PUSH)
    consumer_sender.connect("tcp://127.0.0.1:5558")

    work = consumer_receiver.recv_json()
    #choice_list = work['String']
    print(work['String'])
    choice = raw_input()
    result = { 'Voter ID' : voter_id, 'vote' : choice}
    consumer_sender.send_json(result)


consumer()
print "Thanks for voting"