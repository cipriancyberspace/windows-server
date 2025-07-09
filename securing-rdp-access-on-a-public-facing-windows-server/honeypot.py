import socket
from datetime import datetime

HOST = "0.0.0.0"
PORT = 33891  # Port fals, să nu intri în conflict cu 3389 real

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"[+] Listening on port {PORT} (Fake RDP Honeypot)...")

    while True:
        conn, addr = s.accept()
        with conn:
            ip = addr[0]
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f"[{timestamp}] Connection from {ip}")
            with open("rdphoney_log.txt", "a") as f:
                f.write(f"{timestamp} - {ip}\n")
