# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import Chat_pb2 as Chat__pb2


class RealTimeChatServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SendMessage = channel.unary_unary(
                '/chat.RealTimeChatService/SendMessage',
                request_serializer=Chat__pb2.MessageRequest.SerializeToString,
                response_deserializer=Chat__pb2.MessageResponse.FromString,
                )
        self.GetUserFollowingFollowers = channel.unary_unary(
                '/chat.RealTimeChatService/GetUserFollowingFollowers',
                request_serializer=Chat__pb2.UserID.SerializeToString,
                response_deserializer=Chat__pb2.UsersIDsListResponse.FromString,
                )


class RealTimeChatServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SendMessage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUserFollowingFollowers(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RealTimeChatServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SendMessage': grpc.unary_unary_rpc_method_handler(
                    servicer.SendMessage,
                    request_deserializer=Chat__pb2.MessageRequest.FromString,
                    response_serializer=Chat__pb2.MessageResponse.SerializeToString,
            ),
            'GetUserFollowingFollowers': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUserFollowingFollowers,
                    request_deserializer=Chat__pb2.UserID.FromString,
                    response_serializer=Chat__pb2.UsersIDsListResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'chat.RealTimeChatService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class RealTimeChatService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SendMessage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/chat.RealTimeChatService/SendMessage',
            Chat__pb2.MessageRequest.SerializeToString,
            Chat__pb2.MessageResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetUserFollowingFollowers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/chat.RealTimeChatService/GetUserFollowingFollowers',
            Chat__pb2.UserID.SerializeToString,
            Chat__pb2.UsersIDsListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
