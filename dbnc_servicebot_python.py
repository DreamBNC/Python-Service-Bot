# WIP
# DreamBNC Bot 2
# (c) DreamBNC

# Loading essential libraries (needed for connecting to IRC)
import zirc, ssl


print("DreamBNC Service Bot")
print("(c) 2016 DreamBNC dev team.")
print("Initalizing.")
# setting variables
bncprovider = DreamBNC
bncweb = dreambnc.xyz
server1 = Mushroom
print("Initalized; connecting...")
# connecting using zirc
class Bot(zirc.Client):
 def __init__(self):
 self.connection = zirc.Socket(wrapper=ssl.wrap_socket) 
self.config = zirc.IRCConfig(host="irc.freenode.net",
 port=6697,
 nickname="%s", % (bncprovider,)
 ident="bnc",
 realname="BNC request bot", 
 channels [%s],  % (bncprovider,) 
sasl_user="user", 
sasl_pass="pw") 
self.connect(self.config) 
self.start()
