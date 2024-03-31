from concurrent import futures
import grpc
import logging

import sys
sys.path.append('protos')
from protos.Chat_pb2_grpc import add_RealTimeChatServiceServicer_to_server
from protos.Chat_pb2 import MessageResponse, UserID, UsersIDsListResponse, UserIDsList

class ChatServer:
    def start(self):
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=1000))
        add_RealTimeChatServiceServicer_to_server(self, server)
        server.add_insecure_port(f'[::]:{5001}')
        server.start()
        print("gRPC runing on 5001")
        server.wait_for_termination()

    @staticmethod
    def SendMessage(request, context):
        content = request.content
        sender = request.sender
        receiver = request.receiver
        print(f"Message received from {sender} to {receiver}: {content}")
        return MessageResponse(message="Message received successfully")

    @staticmethod
    def GetUserFollowingFollowers(request, context):
        user_id = request.userid
        print(user_id)
        return UsersIDsListResponse(userIDsLists=[UserIDsList(userIdsList=["user1", "user2", "user3"])])

if __name__ == '__main__':
    
    logging.basicConfig()
    chat_server = ChatServer()
    chat_server.start()
