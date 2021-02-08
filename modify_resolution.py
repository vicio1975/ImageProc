## -*- coding: utf-8 -*-
#"""
#@author: VS

import os
from PIL import Image

def main():

    """
    Thi is the main program
    """
    location = os.getcwd()
    try:
        filenames = sorted((fn for fn in os.listdir(location) if fn.endswith('.jpg')))
        for filename in filenames:
            foo = Image.open(filename)
            size = (os.stat(filename).st_size)/1000
            file = filename[:-3] + "_out.jpg"
            print("Processing ",filename)
            while size > 400:
                print("...")
                foo.save(file,optimize=False,quality=55)
                size = (os.stat(file).st_size)/1000
   
                
    except Exception as e:
        raise e
        print("No image files in here!")

if __name__ == "__main__":
    main()

