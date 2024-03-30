import socket
import pyaudio as pyaudio


HOST = "127.0.0.1"
PORT = 5000


def audio_server(audio):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    print(f"Server listening on {HOST}:{PORT}")

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    print(f"Server success connect")

    p = pyaudio.PyAudio()
    stream = p.open(
        format=pyaudio.paInt32,
        channels=1,
        rate=44100,
        frames_per_buffer=1024,
        output=True
    )

    try:
        bytes_sent = 0
        while bytes_sent < len(audio.raw_data):
            bytes_sent += client_socket.send(audio.raw_data[bytes_sent:])
        print("Audio data sent successfully.")
    except Exception as e:
        raise e

    client_socket, address = server_socket.accept()
    print(f"Connection from {address} established.")

    try:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break

            stream.write(data)
    except Exception as e:
        raise e

    client_socket.close()
