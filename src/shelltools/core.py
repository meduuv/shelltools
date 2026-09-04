import shlex

def split_command(command: str) -> list[str]:
    """Parse a shell-like command into arguments without executing it."""
    if not command.strip(): return []
    return shlex.split(command, posix=True)
