# FastAPI-gRPC


    python -m venv env

    env\Scripts\activate

    pip install fastapi uvicorn grpcio-tools


    python -m grpc_tools.protoc -I./protos --python_out=protos --grpc_python_out=protos protos/Chat.proto



