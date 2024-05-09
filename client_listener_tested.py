import socket
import pyaudio

OUTPUT_SAMPLE_RATE = 44100  # Lowered sample rate

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('192.168.1.26', 8080)  # Replace 'localhost' with the IP address of the server if it's on a different machine
sock.connect(server_address)

# Initialize PyAudio
pya = pyaudio.PyAudio()
stream = pya.open(format=pya.get_format_from_width(width=2), channels=1, rate=OUTPUT_SAMPLE_RATE, output=True)

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
        stream.write(data)

finally:
    # Clean up
    stream.stop_stream()
    stream.close()
    pya.terminate()
    sock.close()