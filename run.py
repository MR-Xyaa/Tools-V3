## WARNA ASU #####
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
##################

import random
import sys
import time
import os
def inu_ganteng_banget(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.1)
user_reply = input("Namamu Bang? \x1b[1;92m")





print ("\x1b[1;91mBang\x1b[1;92m", user_reply)
time.sleep(5)
inu_ganteng_banget('TOOLS V3 BELUM UPDATE KONTOL GW CAPE BIKIN TOOLS TAI')
