import socket
from common_ports import ports_and_services

def get_open_ports(target, port_range, verbose=False):
    open_ports = []

    # Resolve target to IP address
    try:
        ip = socket.gethostbyname(target)
    except socket.gaierror:
        if all(char.isdigit() or char == '.' for char in target):
            return "Error: Invalid IP address"
        return "Error: Invalid hostname"

    # Scan the range of ports
    for port in range(port_range[0], port_range[1] + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            if s.connect_ex((ip, port)) == 0:
                open_ports.append(port)

    # If verbose mode is enabled
    if verbose:
        host_label = f"{target} ({ip})" if target != ip else ip
        result = f"Open ports for {host_label}\nPORT     SERVICE"
        for port in open_ports:
            service = ports_and_services.get(port, "unknown")
            result += f"\n{port:<9}{service}"
        return result

    return open_ports
