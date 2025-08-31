import tkinter
import tkinter.filedialog
import os
import sys
import shutil


class rokuServer:
    def __init__(self, rootDir=(r"C:/xampp/htdocs/"), scriptDir=(r"C:/xampp/htdocs/scripts/"), apiDir=(r"C:/xampp/htdocs/api/"), imagesDir=(r"C:/xampp/htdocs/images/"), serverPath=(r"http://192.168.3.5/")):
        self.__rootDir=rootDir
        self.__scriptDir=scriptDir
        self.__apiDir=apiDir
        self.__imagesDir=imagesDir
        self.__serverPath=serverPath
                 
    ### GET and SET methods for the Roku Server Class
        
    def getRootDir(self):
        return self.__rootDir
    
    def getScriptDir(self):
        return self.__scriptDir
            
    def getApiDir(self):
        return self.__apiDir
                
    def getImagesDir(self):
        return self.__imagesDir
                
    def getServerPath(self):
        return self.__serverPath
                
    def setRootDir(self, rootDir):
        self.__rootDir = rootDir
        
    def setScriptDir(self, scriptDir):
        self.__scriptDir = scriptDir
        
    def setApiDir(self, apiDir):
        self.__apiDir = apiDir
        
    def setImagesDir(self, imagesDir):
        self.__imagesDir = imagesDir
                    
    def setServerPath(self, serverPath):
        self.__serverPath = serverPath            
    
    #### Other METHODS used by the class ####      
    
    ### copies selected files to a new directory
    
    def copy(self, files):
        
        for file in files:
            
            sourceDir = file
            destination = self.getScriptDir()
            shutil.copy(sourceDir, destination)
            
    ### removes brackets and single quotes from each list item and prints the resulting string
    
    def prntStrings(self, newScripts):
    
        for script in newScripts:                      
            
            script = str(script)
            script = script.lstrip('[\'')
            script = script.rstrip('\']')             # convert list obj to string and extract filename\script
            print(script)      

    ### Asks user for list of scripts to import, copies them to the server folder, and creates a PHP trigger script       

    def addScripts(self):

        cut = 0                                             # variable will hold number of files not imported
        scripts = tkinter.filedialog.askopenfilenames()     # opens file explorer for file selection
        if scripts == (''):
            exit()
        
        files = scripts
        self.copy(files)                                    # copies files to the server directory
        newScripts = []                                      
        
        for script in (scripts):                            # parses chosen filenames and adds extensionless filenames to a list    
            script = (script.split("/"))
            script = (script[len(script)-1])
            name = script                                   # holds filename with extension for adding to the PHP
            script = script.split(".")
            if script[1] not in ["vbs", "js", "php"]:       # increments non-chosen count if file type is not compatible
                cut += 1
            else:
                script.remove(script[1])
                newScripts.append(script)                   # adds those files that are compatible to the new list
                self.createPHP(script, name)
                
                                
        if cut == 0:                                            # displays confirmation to user of whether all files have been imported   
            print("All scripts have been added successfully!")  # or number of those not imported
            print()
            print("Scripts:")
            print()
            self.prntStrings(newScripts)       
            print()
            print("Have been imported")
             
        else:
            print(cut, " script(s) could not be added. Compatible file types are .vbs, .js, and .php")    
            
    ### creates the server PHP that can be accessed by the client api call for each script 
    
    def createPHP(self, script, name):

        os.chdir(self.getRootDir())                             #change to whatever server directory will be accessed by the client API call
                              
        script = str(script)
        script = script.lstrip('[\'')                           # convert list obj to string and extract filescript
        script = script.rstrip('\']')
        PHP = script + '.php'                
        newPHP = open(PHP, "w")                                 # creates the file and opens it for writing
        code = ("<?php\n shell_exec(\'c:/xampp/htdocs/scripts/" + name + "\');\n \
        header(\'Location: http://192.168.3.5/index.html?success=true\');\n \
        ?>")
        newPHP.write(code)                                      #writes the PHP code to the new file
        self.addXML(name, PHP)
        ## add print for UI output that indicates success if true "Creating PHP files... Success!"
    
    
    
    
    def getDescription(self, name):
        
        desc = input("Please enter a brief description for the " + name + " script: ")
        desc = str(desc)
        return desc
        
    
    ### adds an entry to the "scripts.xml" (or relevant file) so that the server will serve it when called by the API call
    def addXML(self, name, PHP):
        
        title = name
        linkUrl = (self.getServerPath() + "/" + PHP)
        description = self.getDescription(name)
        pubdate ='08/12/2017'   
       
            
        newItem = ("    <item>\n \
          <title>"+ title +"</title>\n \
          <link>"+ linkUrl +"</link>\n \
          <description>"+ description +"</description>\n \
          <pubDate>" + pubdate + "</pubDate>\n \
          <media:content url=\"" + linkUrl + "\">\n \
          <media:description>"+ description +"</media:description>\n \
          <media:thumbnail url=\"http://192.168.3.5/images/scythe_icon_focus_hd.png\"/>\n \
          <media:title>"+ title +"</media:title>\n \
          </media:content>\n \
         </item>\n \
     </channel>\n</rss>")                      
        os.chdir(self.getApiDir())
        infile = open('scripts.xml', "r")
        file = infile.read()
        position = len(file)-1
        newPosition = (position - 17)
        file = ((file[0:newPosition]) + "\n"  + newItem)
        infile.close()
        outfile = open('scripts.xml', "w")
        outfile.write(file)
        outfile.close()