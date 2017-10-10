from Crypto.Cipher import DES3
import base64

f = open('3des.txt')
s = []
line = f.readline()
while(line):
    s.append(line)
    line = f.readline()
f.close()

cipher = ''.join(s).replace('\n','').replace(' ','')
cipher = cipher.decode('hex')               #密文是16进制的，先decode一下
keyList = []
for k in range(999999):
    iv = str(k).zfill(6)                       #str.zfill()返回指定长度的字符串，前面补0
    try:
        key = 'COPACOBANA'+iv
        des3=DES3.new(key,DES3.MODE_CBC,IV=('0'*16).decode('hex'))
        plaintext = des3.decrypt(cipher)
        if plaintext.find('COPACOBANA')>=0:
            print iv
            keyList.append(key)
            print plaintext
            print '*'*50
            continue
        

    except TypeError:
        continue
print len(keyList)                          #发现不止一个6位数字可以正确解密，但到119991就不输出了
