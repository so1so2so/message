# -*- coding: UTF-8 -*
from django.shortcuts import render
import xml.etree.ElementTree as ET
import time
import sys,os
import random
from ftplib import FTP
reload(sys)
sys.setdefaultencoding('utf8')
a =str(time.time())


def ftpconnect(host, username, password):
    ftp = FTP()
    # ftp.set_debuglevel(2)
    ftp.connect(host, 21)
    ftp.login(username, password)
    ftp.cwd('/test')
    return ftp

def uploadfile(ftp, name):
    fp = open(name, 'rb')
    ftp.storbinary('STOR  %s' % os.path.basename(name), fp)
    ftp.set_debuglevel(0)
    fp.close()


def SendMessage(request):
    if request.method == 'POST':
        tree = ET.parse("allmessage/new.xml")
        root = tree.getroot()
        for node in root.iter('content'):
            node.text = str(request.POST.get('text'))
        for node in root.iter('phone'):
            node.text = str(request.POST.get('phone'))
        code = []  # 空列表
        for i in range(6):
            if i == random.randint(0, 9):
                code.append(str(random.randint(0, 9)))
            else:
                tmp = random.randint(65, 90)
                code.append(chr(tmp))
        code = ''.join(code)
        print code
        name = 'allmessage/'+a+code+'.xml'
        print name
        tree.write(name, "UTF-8", xml_declaration=True)
        ftp = ftpconnect(host='192.168.1.11',username='ftpuser',password='ftppwd')
        status = uploadfile(ftp, name)
        print status
        return render(request, 'message.html')
    else:
        return render(request, 'message.html')
