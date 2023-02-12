import socket as socket_module
import Configs


def start_client():
    socket = socket_module.socket(family=socket_module.AF_INET, type=socket_module.SOCK_DGRAM)

    socket.settimeout(Configs.timeout)
    send_message(socket=socket)


def send_message(socket: socket_module.socket):
    try:
        encoded_message = str.encode(Configs.client_message)

        socket.sendto(encoded_message, Configs.server_socket)
        receive_message(socket=socket)
    except KeyboardInterrupt:
        print("\nKeyboard interrupt")
    except Exception as error:
        print(f"ERROR: {error}")

    close_connection(socket=socket)


def receive_message(socket: socket_module.socket):
    server_data, server_address = socket.recvfrom(Configs.buffer_size)
    decoded_message = bytes.decode(server_data)

    print(f"NEW ANSWER FROM SERVER\nADDRESS: {server_address}\nANSWER: {decoded_message}\n---\n")


def close_connection(socket: socket_module.socket):
    socket.close()
    print("CONNECTION CLOSED")


if __name__ == "__main__":
    start_client()
