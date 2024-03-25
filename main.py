from test_server import MServer
from test_client import MClient

if __name__ == '__main__':
    server = MServer()
    client = MClient(host='127.0.0.1', port=840)
