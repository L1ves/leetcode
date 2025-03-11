import socket
import math
import re

# Server connection details
HOST = 'challenge01.root-me.org'
PORT = 52002

# Create a TCP socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Connect to the server
    s.connect((HOST, PORT))

    # Receive data from the server
    data = s.recv(1024).decode()  # Decode bytes to string
    print("Received:", data)

    parts = re.findall(r'\d+', data)
    if len(parts) >= 2:
        n1 = float(parts[1])
        n2 = float(parts[2])
        print(n1)
        print(n2)

        # Calculate the result
        sqrt_n1 = math.sqrt(n1)  # Square root of 668
        result = sqrt_n1 * n2  # Multiply
        result_rounded = "{:.2f}".format(result)  # Round to 2 decimal places # Convert to float        # Send the result back to the server
        print(result_rounded)
        s.send((result_rounded + "\n").encode())  # Encode string to bytes

        # Receive the final response from the server
        response = s.recv(1024).decode()
        print(f"Server response: {response}")
