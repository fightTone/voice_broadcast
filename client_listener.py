import numpy as np
import simpleaudio as sa
import socket

OUTPUT_SAMPLE_RATE = 22050  # Lowered sample rate

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('192.168.1.2', 8080)  # Replace 'localhost' with the IP address of the server if it's on a different machine
sock.connect(server_address)

try:
    while True:
        # Receive data
        data = sock.recv(1024)
        if not data:
            print("no data")
            break
        else:
            print("data received")
        # Play audio
        try:
            audio_data = np.frombuffer(data, dtype=np.int16)
            sa.play_buffer(audio_data, 1, 2, OUTPUT_SAMPLE_RATE)
        except Exception as e:
            print(f"Error playing audio: {e}")
            break

finally:
    # Clean up
    sock.close()