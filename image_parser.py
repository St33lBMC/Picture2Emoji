from PIL import Image
import numpy as np

class Parser():
    def __init__(self):
        pass
    
    #im too lazy to do the parser myself so I will just use pillow's :D
    def parse_to_pixel_matrix(self, path):
        img = Image.open(path)
        img = img.resize((20, 20), Image.LANCZOS)
        return np.array(img)
    