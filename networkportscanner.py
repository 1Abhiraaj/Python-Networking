import socket

def is_host_live(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            s.connect((ip, port))
        return True
    except (socket.timeout, ConnectionRefusedError):
        return False

def scan_ports(ip, port_range):
    open_ports = []
    for port in range(port_range[0], port_range[1] + 1):
        if is_host_live(ip, port):
            open_ports.append(port)
    return open_ports

def main():
    target_ip = input("Enter the target IP address: ")
    start_port = int(input("Enter the start port: "))
    end_port = int(input("Enter the end port: "))

    port_range = (start_port, end_port)
    
    if start_port > end_port or start_port < 1 or end_port > 65535:
        print("Invalid port range. Please enter a valid range.")
        return

    if is_host_live(target_ip, 80): 
        print(f"Host {target_ip} is live.")
        open_ports = scan_ports(target_ip, port_range)
        if open_ports:
            print("Open ports:")
            for port in open_ports:
                print(port)
        else:
            print("No open ports found.")
    else:
        print(f"Host {target_ip} is not live.")

if __name__ == "__main__":
    main()