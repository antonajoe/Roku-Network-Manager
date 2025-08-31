### adds an entry to the "scripts.xml" (or relevant file) so that the server will serve it when called by the API call

import os

def addXML():
    
    title = "new title"
    linkUrl = "http://192.168.3.5/script.php"
    desc = "getDescription()"
    pubdate ='mm/dd/yyyy'
    
        
    newItem = ("    <item>\n \
      <title>"+ title +"</title>\n \
      <link>"+ linkUrl +"</link>\n \
      <description>" + desc + "</description>\n \
      <pubDate>" + pubdate + "</pubDate>\n \
      <guid isPermaLink=\"false\">decbe34b64ea4ca281dc09997d0f23fd</guid>\n \
      <media:content channels=\"2\" bitrate=\"1328.0\" duration=\"53\" fileSize=\"8731706\" framerate=\"23.976\" height=\"720\" type=\"video/mp4\" width=\"1280\" isDefault=\"true\" url=\"" + linkUrl + "\">\n \
      <media:description>" + desc + "</media:description>\n \
      <media:keywords> Key, Words </media:keywords>\n \
      <media:thumbnail url=\"http://192.168.3.5/images/\"/>\n \
      <media:title>" + title + "</media:title>\n \
      </media:content>\n \
     </item>\n \
 </channel>\n</rss>")                      
    os.chdir(r'C:/xampp/htdocs/api/')
    infile = open('scripts.xml', "r")
    file = infile.read()
    position = len(file)-1
    newPosition = (position - 17)
    file = ((file[0:newPosition]) + "\n"  + newItem)
    infile.close()
    outfile = open('scripts.xml', "w")
    outfile.write(file)
    outfile.close()
    
addXML()

