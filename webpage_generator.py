from html.parser import HTMLParser
import sys

IP:str = sys.argv[1] if len(sys.argv) == 2 else "127.0.0.1"
NEW_WEBSITE:str = ""

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        global NEW_WEBSITE, IP
        out="<"+str(tag)
        for att,value in attrs:
            if (tag == "link" and 'rel' in attrs and att == 'href'):
                value = 'http://'+IP+'/favicon.ico'
            elif (tag == "div" and att == 'background'):
                value = 'http://'+IP+'/background.png'
            elif (tag == "video" and att == 'poster'):
                value = 'http://'+IP+'/background.png'
            elif (tag == "source" and att == 'src'):
                value = 'http://'+IP+':8899/playlist.m3u8'
            value = '\"'+str(value)+'\"'
            out+=" "+str(att)+"="+str(value)
        NEW_WEBSITE+=str(out)+">"
    def handle_endtag(self, tag):
        global NEW_WEBSITE
        NEW_WEBSITE+="</"+str(tag)+">"
    def handle_data(self, data):
        global NEW_WEBSITE
        NEW_WEBSITE+=str(data)

parser = MyHTMLParser()
with open('html/index.html',"r") as webpage:
    data = webpage.read()
    parser.feed(data)
with open('html/index.html',"w") as webpage: webpage.write(NEW_WEBSITE)
