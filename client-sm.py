import grpc

import sys
sys.path.append('protos')
from protos.Chat_pb2_grpc import RealTimeChatServiceStub
from protos.Chat_pb2 import MessageRequest

def send_message(sender, receiver, content):
    channel = grpc.insecure_channel('localhost:5001')
    stub = RealTimeChatServiceStub(channel)
    message = MessageRequest(sender=sender, receiver=receiver, content=content)
    response = stub.SendMessage(message)
    return response.message

if __name__ == '__main__':
    sender = "sender_user_id"
    receiver = "receiver_user_id"
    content = "Hello, this is a test message!"
    response = send_message(sender, receiver, content)
    print("Response:", response)
