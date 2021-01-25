# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 19:22:25 2021

@author: vk779
"""

import requests
import threading
import shutil
import os 
start = 1000
logo='''
██████  ██████   ██████       ██ ███████  ██████ ████████     ██   ██  ██████  ████████ ███████  ██████ ██ ███████ ███    ██ ████████ ██ ███████ ████████ 
██   ██ ██   ██ ██    ██      ██ ██      ██         ██        ██   ██ ██    ██    ██    ██      ██      ██ ██      ████   ██    ██    ██ ██         ██    
██████  ██████  ██    ██      ██ █████   ██         ██        ███████ ██    ██    ██    ███████ ██      ██ █████   ██ ██  ██    ██    ██ ███████    ██    
██      ██   ██ ██    ██ ██   ██ ██      ██         ██        ██   ██ ██    ██    ██         ██ ██      ██ ██      ██  ██ ██    ██    ██      ██    ██    
██      ██   ██  ██████   █████  ███████  ██████    ██        ██   ██  ██████     ██    ███████  ██████ ██ ███████ ██   ████    ██    ██ ███████    ██    
                                                                                                                                                          
                                                                                                                                                          
'''

print(logo)  
print("Created by v1n33t  All rights reserved")   
x = input("Enter where to start from default 1000")
url= ""
def download(i):

    response = requests.get(url+str(i)+".jpg", stream=True)
    if(response.status_code==200):
        with open(str(i)+".jpg", 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
        del response
        print("%d downloaded"%i)
    else:
        print("%d named employ doest exist"%i)

print("Starting to use all cores and threads")
for i in range(start, 2000):
    threading.Thread(target=download(i)).start()
    print("downloading ,", i)