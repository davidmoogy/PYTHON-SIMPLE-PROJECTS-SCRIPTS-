import socket
import ipaddress
import concurrent.futures

def scan_ip(ip):
    """Attempt to connect to the specified IP address on port 80."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)  # Set timeout for socket connection
            result = sock.connect_ex((ip, 80))  # Try to connect to port 80
            if result == 0:
                print(f"Active device found at {ip}")
            else:
                print(f"Inactive device at {ip}")
    except socket.error as err:
        print(f"Socket error for {ip}: {err}")

def scan_network(ip_range):
    """Scan a range of IP addresses to find active devices."""
    print(f"Scanning network range: {ip_range}")
    # Generate IP addresses in the specified range
    try:
        for ip in ipaddress.IPv4Network(ip_range, strict=False):
            # Use a thread pool to scan IP addresses concurrently
            with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
                executor.submit(scan_ip, str(ip))
    except ValueError as ve:
        print(f"Invalid IP range: {ve}")

if __name__ == "__main__":
    # Specify the IP range to scan (e.g., '192.168.1.0/24')
    ip_range = input("Enter the IP range to scan (e.g., 192.168.1.0/24): ")
    scan_network(ip_range)
