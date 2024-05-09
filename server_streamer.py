import socket
import threading
import pyaudio

# Audio settings
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

# Create a PyAudio object
p = pyaudio.PyAudio()

# Open the microphone stream
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_address = ('0.0.0.0', 8080)
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

def handle_client(connection, client_address):
    try:
        print('connection from', client_address)

        # Send data in a loop
        while True:
            print('sending data')
            data = stream.read(CHUNK)
            connection.sendall(data)

    finally:
        # Clean up the connection
        connection.close()

while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()

    # Start a new thread to handle this client
    client_thread = threading.Thread(target=handle_client, args=(connection, client_address))
    client_thread.start()