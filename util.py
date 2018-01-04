import subprocess

def smart_bool(s):
    if s is True or s is False:
        return s
    if str(s).lower() in ("yes", "y", "true",  "t", "1", "ok"):
        return True
    if str(s).lower() in ("no",  "n", "false", "f", "0",
                    "0.0", "", "none", "[]", "{}", "fail", "failed"):
        return False
    raise Exception('Invalid value for boolean conversion: ' + str(s))

def cmd(cmd, output=True):
    if output:
        return subprocess.Popen(
            cmd, shell=True,
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT).stdout.read()
    else:
        subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

def toHex(s):
    lst = []
    for ch in s:
        hv = hex(ord(ch)).replace('0x', '')
        if len(hv) == 1:
            hv = '0'+hv
        lst.append(hv)
    
    return reduce(lambda x,y:x+y, lst)