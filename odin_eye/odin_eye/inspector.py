import psutil
from .utils import to_str, get_proc_info

class ProcessInspector:
    """
    Collects process-level information from the local system.
    """
    ATTRS = ['cmdline', 'net_connections', 'exe', 'ppid', 'username']

    def collect(self) -> list[list]:
        """
        Returns:
            A 2D list where the first row is the header:
            ['PID', 'cmdline', 'net_connections', 'exe', 'ppid', 'username']
            and each subsequent row contains string values.
        """
        procs = {p.pid: p.info for p in psutil.process_iter(self.ATTRS)}
        header = ['PID'] + self.ATTRS
        rows = [header]

        for pid, info in sorted(procs.items()):
            row = [pid]
            for attr in self.ATTRS:
                row.append(to_str(info.get(attr)))
            rows.append(row)

        return rows


class NetworkInspector:
    """
    Collects network connection information and enriches it with process details.
    """
    def collect(self) -> list[list]:
        """
        Returns:
            A 2D list where the first row is the header:
            ['PID', 'ProcessName', 'CmdLine', 'Status', 'LocalAddress', 'RemoteAddress']
        """
        connections = psutil.net_connections(kind='inet')
        header = ['PID', 'ProcessName', 'CmdLine', 'Status', 'LocalAddress', 'RemoteAddress']
        rows = [header]

        for conn in connections:
            name, cmd_line = get_proc_info(conn.pid)
            laddr = f"{conn.laddr.ip}:{conn.laddr.port}" if conn.laddr else ""
            raddr = f"{conn.raddr.ip}:{conn.raddr.port}" if conn.raddr else ""
            rows.append([
                conn.pid,
                name,
                to_str(cmd_line),
                conn.status,
                laddr,
                raddr
            ])

        return rows