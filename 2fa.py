import os, platform
try:
    import requests
except:
    os.system('pip install requests')
    print(" Update Checking")
os.system("git pull")

import requests
bit = platform.architecture()[0]
if bit == '64bit':
    from rxs_2fa import ReyadXShipu
    ReyadXShipu()
else:
    print('\n YOUR DEVICE IS NOT SUPPORT THIS TOOL')
    os.system('exit')
