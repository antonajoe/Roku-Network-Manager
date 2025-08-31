The code in these folders is a personal project that I worked on this past summer(2017) for a couple of weeks after graduating from Utica College. The Python code is mine, the Brightscript code is Roku's except for minor alterations. The "scythe" image is not mine either.

Problem and Goal:

The goal of the application is to provide the user a way to perform network administration or other computing functions while on their couch watching their Roku Player. In particular, the Roku does not have the structure to support VPN client operation. Some might solve this by having the Player's internet connection run through another machine, for example, a firewall which is running a VPN client. The problem is that some Apps don't allow content to be viewed from VPN connection IP's. Thus the idea to run a script server on another machine on the user's LAN that the Roku can access. A script can be written that will access the firewall over an SSH connection and automatically modify a firewall rule that will send the Roku Player's traffic either in the clear, or through the VPN tunnel. This effectively allows any VPN client to serve as a VPN client for the Roku. In addition, any other type of script that can be run from, say a Windows machine, can be triggered to run as well.

The exciting part:

This actually works! while the Roku is designed to stream media, the Brightscript code when combined with the setup discussed below will trigger the script to run on the remote machine, and can even be made to look not completely ugly in the process. It succesfully retrieves, labels, and displays the scripts on the server and allows the user to run them with a press of the remote.

Drawbacks:

It kind of complicated to setup and would require A LOT more work to really function reliably and look decent. Also, different users will have different LAN configurations, many will not want this functionality, many will not know how to write their own scripts, etcetera... with this in mind I didn't develop it past the point of adding the VPN scripts and a Shutdown and Restart script respectively, and don't really plan to.

The Setup:

If you want to try this out for yourself, a minimal LAN configuration is as follows:

1) A router\firewall serving a subnet with both a Roku Player and PC\Linux\Mac on it.
2) SSH access configured between the Router and PC
3) A web server running on the PC, I used XAMPP\Apache
4) the Python code in Roku Script Server\src\rokuServerClass.py might need to be modified to point to your server. Further work on this code could make this part much easier.
5) Putty or some other SSH client on the PC to access the Router
6) VBS scripts that perform functions on the Router\Firewall, a Restart or Shutdown script is pretty easy to do.
7) A folder called "api" in htdocs with a file called scripts.xml that the Roku will get the script information from, a folder called "images" in htdocs that holds the icons for the scripts, and a folder called "scripts" that will hold the actual VBS (or other) scripts themselves.
8) Eclipse IDE, or other method of sideloading developer Roku Apps onto the Roku, Roku must also be in Developer Mode, search this to find out how to if needed.

It worked for me, I can't guarantee that it will work for you even with all of the above, hence why I'm not still actively developing it, but it was a lot of fun!!!