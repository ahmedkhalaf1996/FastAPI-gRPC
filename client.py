import grpc

import sys
sys.path.append('protos')
from protos.Chat_pb2_grpc import RealTimeChatServiceStub
from protos.Chat_pb2 import UserID

def get_followers(user_id):
    channel = grpc.insecure_channel('localhost:5001')
    stub = RealTimeChatServiceStub(channel)
    user_id_message = UserID(userid=user_id)
    response = stub.GetUserFollowingFollowers(user_id_message)
    return response.userIDsLists[0].userIdsList

if __name__ == '__main__':
    user_id = "your_user_id_here"
    followers = get_followers(user_id)
    print("Followers:", followers)
