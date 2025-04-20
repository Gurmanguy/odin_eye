import psutil


def to_str(val):
    """
    Convert a value to a string for spreadsheet output:
    - If val is None ➞ return empty string.
    - If val is a list or tuple ➞ join elements with a comma.
    - Otherwise ➞ return str(val).
    """
    if val is None:
        return ""
    if isinstance(val, (list, tuple)):
        return ", ".join(str(x) for x in val)
    return str(val)


def get_proc_info(pid):
    """
    Given a PID ( return a tuple (name, cmdline_list).
    If the process does not exist or access is denied, return ("", []).
    """
    try:
        p = psutil.Process(pid)
        return p.name(), p.cmdline()
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        return "", []