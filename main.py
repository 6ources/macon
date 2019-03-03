import subprocess
subprocess.call("clear")
#
print("\033[36m ___      ___       __       ______    ______    _____  ___   \033[0m") 
print("\033[36m|   \    /   |     /  \     / _  \  /     \  (\   \|  \       \033[0m") 
print("\033[36m| \  \  //   |    /    \   (: ( \___)// ____  \ |. \\   \    | \033[0m") 
print("\033[36m|  \  \/.    |   /' /\  \   \/ \    /  /    ) :)|: \.   \\   | \033[0m") 
print("\033[36m|: \.        |  //  __'  \  //  \ _(: (____/ // |.  \    \. | \033[0m") 
print("\033[36m|.  \    /:  | /   /  \\   \(:   _)  \\        /  |    \    \ | \033[0m") 
print("\033[36m|___|\__/|___|(___/    \___)\_______)\"__ ___/    \___|\____\) \033[0m")
print("\033[34m                                                                .....$m0k3y.....\033[0m") 


#interface selection
print("tell me the interface you want to change-")
a=input("\033[41mpress 1 for eth0, 2 for wlan0, 3 for others...=\033[0m")
if a==1:
    interface="eth0"
elif a==2:
    interface="wlan0"
elif a==3:
    interface=raw_input("\033[41mok so the interface name is?...=\033[0m")
else:
    print("\033[41mwrong input! TRY AGAIN\033[0m")

#random/custom mac!
print("Do you want a new random mac or custom mac?")
b=input("\033[41mpress 1 for random and 2 for custom input...=\033[0m")
if b==1:
    subprocess.call("ifconfig " + interface + " down",shell=True)
    subprocess.call("macchanger -r "+ interface ,shell=True)
    subprocess.call("ifconfig " + interface + " up",shell=True)
    subprocess.call("clear")
    subprocess.call("ifconfig",shell=True)
elif b==2:
    print("tell me the custom input you want!")
    print("try to start the first pair with 00...")
    custmac=raw_input("\033[41mit should be 6 pair : -colon- between each pair...=\033[0m")
    #code for custom mac
    subprocess.call("ifconfig " + interface +" down",shell=True)
    subprocess.call("ifconfig " + interface +" hw ether "+ custmac,shell=True)
    subprocess.call("ifconfig " + interface +" up",shell=True)
    subprocess.call("clear")
    subprocess.call("ifconfig",shell=True)
else:
    print("\033[41mwrong input! TRY AGAIN\033[0m")
print("\033[31m....you're ready to go\033[0m")
