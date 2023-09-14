'''
Create a gif file and save it to disc
'''


import sys
from PIL import Image

f_path = r'C:\\Users\\royaw\Documents\\CS50\\Images\\'
images = []
# f_path = r"C:\\Users\\royaw\Documents\\CS50\\Images\\"

for arg in sys.argv[1:]:
    image = Image.open(f_path + arg)
    images.append(image)

images[0].save(
    f_path + 'Costumes.gif',
    save_all = True,
    append_images = [images[1]],
    duration = 200,
    loop = 0,
    
)

## Added f_path to my folder images as don't wnat the directory 8_file_IO getting too crowded.