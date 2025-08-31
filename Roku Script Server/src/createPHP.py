### takes input list of pure filenames (with no path or extension) and creates PHP file with that name 

import os
 
def createPHP(newList):
    
    os.chdir(r'C:/xampp/htdocs/')             #change to whatever server directory will be accessed by the client API call
    
    for name in newList:                      # take input name and inject it into predefined PHP file only needing a new path/filename argument
        
        name = str(name)
        name = name.lstrip('[\'')
        name = name.rstrip('\']')             # convert list obj to string and extract filename
        newPHP = open(name + '.php', "w")     # creates the file and opens it for writing
        code = ("<?php\n shell_exec(\'c:/xampp/htdocs/scripts/" + name + ".vbs\');\n \
        header(\'Location: http://192.168.3.5/index.html?success=true\');\n \
        ?>")
        newPHP.write(code)                    #writes the PHP code to the new file

## add return for UI output that indicates success if true "Creating PHP files... Success!"