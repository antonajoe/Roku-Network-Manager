### defines functions that import new scripts to the Roku Script Server


import tkinter.filedialog
#import tkinter.messagebox

# Asks user for list of scripts to import and returns just the filenames without path or filetype endings
# Example: "script1.vbs" is returned as ['script1']
 
def addScripts():
    
    cut = 0                                             # variable will hold number of files not imported
    Scripts = tkinter.filedialog.askopenfilenames()     # opens file explorer for file selection
    if Scripts == (''):
        exit()
         
    newScripts = []                                     # ask user to open the files they want 
    
    for script in (Scripts):                            # parses chosen filenames and adds pure filenames to a list    
        script = (script.split("/"))
        #print(script)
        script = (script[len(script)-1])
        #print(script)
        script = script.split(".")
        #print(script[0])
        if script[1] not in ["vbs", "js", "php"]:       # increments non-chosen count if file type is not compatible
            cut += 1
        else:
            script.remove(script[1])
            #print(script)                    # adds those files that are compatible to the new list
            newScripts.append(script)
    
    # return newScripts 
    
    if cut == 0:                                            # displays confirmation to user of whether all files have been imported   
        print("All scripts have been added successfully!")  # or number of those not imported
        print()
        print("Scripts:")
        print()
        prntStrings(newScripts)
        print()
        print("Have been imported")
    else:
        print(cut, " script(s) could not be added. Compatible file types are .vbs, .js, and .php")    
    
    return newScripts 


def prntStrings(newScripts):
    
    for name in newScripts:                      
        
        name = str(name)
        name = name.lstrip('[\'')
        name = name.rstrip('\']')             # convert list obj to string and extract filename
        print(name)