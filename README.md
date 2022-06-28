# CLI Outlook Safelink Decoder

### background

a python implementation from this [strange looking website]( http://www.o365atp.com/) i use quite frequently to peek encoded url from outlook. 

### usage

running without params will prompt manual input

`python o365sl.py`

by default the program will append parsed result in clipboard, flag `--d` disables default clipboard operation, `--s` enables silent mode.

`python o365sl.py {url}`
`python o365sl.py {url} --d`
`python o365sl.py {url} --s`

combining both flags will results in... nothing.