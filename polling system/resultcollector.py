import time
import zmq

def poll(vote_count,vote):
    vote_count[vote-1] = vote_count[vote-1] + 1
    return vote_count

def result_collector():
    vote_count=[0,0,0,0]
    context = zmq.Context()
    results_receiver = context.socket(zmq.PULL)
    results_receiver.bind("tcp://127.0.0.1:5558")
    #collecter_data = {}
    print("boo")
    for x in range(3):       
        result = results_receiver.recv_json()
        voter_id = result['Voter ID']
        print 'voter with ID ',voter_id,' has voted'
        vote=int(result['vote'])
        vote_count[vote-1] = vote_count[vote-1] + 1
    print "BJP ", vote_count[0]
    print "Congress ", vote_count[1]
    print "AAP ", vote_count[2]
    print "NULL ",vote_count[3]

result_collector()
#print "Done"