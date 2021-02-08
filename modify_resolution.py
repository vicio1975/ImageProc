## -*- coding: utf-8 -*-
#"""
#@author: VS

import os
from PIL import Image
import PIL

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
            if size > 500 and size <= 600:
                while size > 400:
                    print("...")
                    foo.save(file,optimize=True,quality=65)
                    size = (os.stat(file).st_size)/1000
            elif size > 600 and size <= 1000:
                while size > 400:
                    print("...")
                    foo.save(file,optimize=True,quality=65)
                    size = (os.stat(file).st_size)/1000
            elif size > 1200:
                h, w = foo.size
                fixed_height = 1000
                height_percent = (fixed_height / float(foo.size[1]))
                width_size = int((float(foo.size[0]) * float(height_percent)))
                foo = foo.resize((width_size, fixed_height), PIL.Image.NEAREST)
                foo.save(file)
                while size > 400:
                    print("...")
                    foo.save(file,optimize=True,quality=65)
                    size = (os.stat(file).st_size)/1000
   
                
    except Exception as e:
        raise e
        print("No image files in here!")

if __name__ == "__main__":
    main()

