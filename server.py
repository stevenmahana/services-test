import time
import zmq

class Services(object):

    @staticmethod
    def receive_message():

        context = zmq.Context()
        socket = context.socket(zmq.REP)
        socket.bind("tcp://*:5569")

        while True:
            #  Wait for next request from client
            message = socket.recv()
            print("Received request: %s" % message)

            #  Do some 'work'
            time.sleep(1)

            #  Send reply back to client
            socket.send(b"Services Data")

if __name__ == '__main__':
    zs = Services()
    zs.receive_message()