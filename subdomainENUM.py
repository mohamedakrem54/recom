# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# |                      SubRecon                           |
# | [ + ] SubdomainS Recon using List                       |

import socket
from termcolor import colored
import os
os.system("cls|clear")
url = input("Site ::>> ")
with open("../db/subdomains.txt") as f:
    lines = [line.rstrip() for line in f]
    file = open(f"_{url}.txt","w")
    for i in lines:
        try:
            p = (f"{i}.{url}")+":"+socket.gethostbyname(f"{i}.{url}")
            print(colored(p,"green"))
            file.write(p+"\n")
        except:
            print(colored((f"NO: {i}.{url}                                                                                                                 \r"),("red")),end="")
            print("\r",end="")

file.close()
