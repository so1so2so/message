# -*- coding: UTF-8 -*
from django.shortcuts import render
import xml.etree.ElementTree as ET
import datetime
import sys
reload(sys)
sys.setdefaultencoding('utf8')
a =str(datetime.datetime.now())
def SendMessage(request):
    if request.method == 'POST':
        tree = ET.parse("allmessage/new.xml")
        root = tree.getroot()
        for node in root.iter('content'):
            node.text = str(request.POST.get('text'))
        for node in root.iter('phone'):
            node.text = str(request.POST.get('phone'))
        tree.write("allmessage/"+a+'.xml', "UTF-8")
        return render(request, 'message.html')
    else:
        return render(request, 'message.html')
