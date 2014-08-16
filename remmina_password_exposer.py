from Crypto.Cipher import DES3
import base64
import os
import re


# costanti :)
REMMINA_FOLDER = '.remmina/'
REMMINA_PREF   = 'remmina.pref'

REGEXP_ACCOUNTS = r'[0-9]{13}\.remmina'
REGEXP_PREF     = r'remmina.pref'

diz = {}

fs = open(REMMINA_FOLDER+REMMINA_PREF)
fso = fs.readlines()
fs.close()

for i in fso:
    if re.findall(r'secret=', i):
        r_secret = i[len(r'secret='):][:-1]
        print 'found secret', r_secret
    
for f in os.listdir(REMMINA_FOLDER):
    if re.findall(REGEXP_ACCOUNTS, f): 
        
        o = open( REMMINA_FOLDER+f, 'r')
        fo = o.readlines()
        o.close()
        
        for i in fo:
            if re.findall(r'password=', i):
                r_password = i[len(r'password='):][:-1]
            if re.findall(r'name=', i):
                r_name = i.split('=')[1][:-1]

        #~ print fo
        #~ print 'found', f
        
        password = base64.decodestring(r_password)
        secret = base64.decodestring(r_secret)
        
        diz[r_name] = DES3.new(secret[:24], DES3.MODE_CBC, secret[24:]).decrypt(password)
        print r_name, diz[r_name]
        

