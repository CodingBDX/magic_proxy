

try:
    import requests
    import scrython
    import imageio
    import requests
    import time
    import config
    import numpy as np
    import os
    import os.path
    from fpdf import FPDF, HTMLMixin
    import glob
    from numpy.fft import fft2, ifft2, fftshift, ifftshift
    from skimage.transform import resize
    import pygame
    import shutil
    import subprocess

except ImportError:
  print ("Trying to Install required module:")
  os.system('pip3 install requests')
  os.system('pip3 install scrython')
  os.system('pip3 install imageio')
  os.system('pip3 install time')
  os.system('pip3 install numpy')
  os.system('pip3 install pygame')
import shutil
import subprocess
import scrython
import imageio
import requests
import time
import config
import numpy as np
import os
import os.path
from fpdf import FPDF, HTMLMixin
import glob
from numpy.fft import fft2, ifft2, fftshift, ifftshift
from skimage.transform import resize








path2 = os.path.dirname(os.path.realpath(__file__))
   




   
print ("where is name txt for price's ?")
answer2=input("enter your_file.txt =>")



filePath2 = os.path.join(path2, answer2)
filePath3 = os.path.join(path2, "card.txt")


usd = "eur"
def nameBar(name, manaCost):
    return "{} {}".format(name, manaCost)

def typeBar(typeLine, rarity):
    return "{} | {}".format(typeLine, rarity[:1].upper())

def powerAndToughness(power, toughness):
    return "{}/{}".format(power, toughness)

def process_card(cardname, expansion=None):
    time.sleep(0.05)

    # try/except in case the search doesn't return anything
    
    try:
        query = cardname 
        data = scrython.cards.Search(q=query)
        
        for card in data.data():
            
            eur = str(card["prices"]["eur"]) 
            usd = str(card["prices"]["usd"]) 
            
            print(query + "|", card['set_name'] + "| price :"+ eur + " eur" +"|" + usd + " $" + "\n")
            
            

           
            
                    
    except scrython.foundation.ScryfallError:
        print("Couldn't find card: " + cardname)
        return


       

    

    
        
out=""
with open(filePath2) as f:
    
   for ligne in f:
        ligne=ligne.strip()
        ligne=ligne.replace('Sideboard:', '').replace('Sauvegarder', '')
        if ligne !='' and not ligne.startswith("//"):
            n,mot=ligne.replace('SB:','').split(maxsplit=1)
            out+=(mot+'\n')*int(n)
        
             
with open(filePath3,'w') as f:
    f.write(out)

if __name__ == "__main__":
    # Loop through each card in cards.txt and scan em all


    with open(filePath3, 'r') as fp:
        for cardname in fp:
            cardname = cardname.rstrip()
            try:
                pipe_idx = cardname.index("|")
                process_card(cardname[0:pipe_idx], cardname[pipe_idx+1:])
            except ValueError:
                process_card(cardname)

    

