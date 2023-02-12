import socket as socket_module
import Configs


def start_server():
    socket = socket_module.socket(family=socket_module.AF_INET, type=socket_module.SOCK_DGRAM)

    socket.bind(Configs.server_socket)

    print(f"LISTENING ON: {Configs.server_socket}\n")

    is_listening = True

    while is_listening:
        try:
            listen_clients(socket=socket)
        except KeyboardInterrupt:
            print("\nKeyboard interrupt")
            close_connection(socket=socket)

            is_listening = False
        except Exception as error:
            print(f"\nCLOSE SOCKET WITH ERROR: {error}")
            close_connection(socket=socket)

            is_listening = False


def listen_clients(socket: socket_module.socket):
    client_data, client_socket = socket.recvfrom(Configs.buffer_size)
    decoded_message = bytes.decode(client_data)

    print(f"NEW MESSAGE FROM CLIENT\nADDRESS: {client_socket}\nMESSAGE: {decoded_message}\n---\n")

    encoded_message = str.encode(Configs.server_message)

    try:
        socket.sendto(encoded_message, client_socket)
    except Exception as error:
        print(f"CLOSE CONNECTION WITH CLIENT {client_socket} WITH ERROR: {error}")


def close_connection(socket: socket_module.socket):
    socket.close()
    print("STOP LISTENING")


if __name__ == "__main__":
    start_server()
