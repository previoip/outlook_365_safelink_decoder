def copyToClipboard(string):
    import subprocess
    import platform
    string = string.strip()
    platform = platform.system()
    
    if platform == 'Windows':
        # windows shell
        clipcmd = 'clip'
    elif platform == 'Darwin':
        # mac bash?
        clipcmd = 'pbcopy'
    else:
        raise ValueError(f'{plarform=} : Unassigned copy command for current platform.')

    cmd = f'echo {string}|{clipcmd}'
    return subprocess.check_call(cmd, shell=True)
