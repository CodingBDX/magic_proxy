import pygame
import os,re,sys
magic = '''          .$$      /$$                     /$$                 /$$$$$$$                                        
| $$$    /$$$                    |__/                | $$__  $$                                       
| $$$$  /$$$$  /$$$$$$   /$$$$$$  /$$  /$$$$$$$      | $$  \ $$ /$$$$$$   /$$$$$$  /$$   /$$ /$$   /$$
| $$ $$/$$ $$ |____  $$ /$$__  $$| $$ /$$_____/      | $$$$$$$//$$__  $$ /$$__  $$|  $$ /$$/| $$  | $$
| $$  $$$| $$  /$$$$$$$| $$  \ $$| $$| $$            | $$____/| $$  \__/| $$  \ $$ \  $$$$/ | $$  | $$
| $$\  $ | $$ /$$__  $$| $$  | $$| $$| $$            | $$     | $$      | $$  | $$  >$$  $$ | $$  | $$
| $$ \/  | $$|  $$$$$$$|  $$$$$$$| $$|  $$$$$$$      | $$     | $$      |  $$$$$$/ /$$/\  $$|  $$$$$$$
|__/     |__/ \_______/ \____  $$|__/ \_______/      |__/     |__/       \______/ |__/  \__/ \____  $$
                        /$$  \ $$                                                            /$$  | $$
                       |  $$$$$$/                                                           |  $$$$$$/
                        \______/            ==Bordeaux Team==                               \______/ 

 '''

print(magic)
path2 = os.path.dirname(os.path.realpath(__file__))
keygen = os.path.join(path2, 'keygen.mp3')
pygame.mixer.init()
monson = pygame.mixer.music.load(keygen)
pygame.mixer.music.play(-1,0,0)


print ("What do you want to do ?")
print ("1. Download card's editions")
print ("2. make proper deck and print one file PDF")
print ("3. make deck for website like MPC makingplayercards")
print ("4. Calcul price of your deck")
answer = input("what's your choice?")

if answer == "1":
        exec(open(path2 + "/magic_proxy_set.py").read())

        

if answer == "2":
	exec(open(path2 + "/magic_proxy.py").read())

if answer == "3":
    exec(open(path2 + "/magic_proxy_for_mpc.py").read())
	
    
    
        


        
        


if answer == "4":
        from howmuch import *
        request_url(name)
       
