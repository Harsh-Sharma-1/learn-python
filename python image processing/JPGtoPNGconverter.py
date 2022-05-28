import sys
import os
from PIL import Image

# sys to grab first and second arguments
image_folder = sys.argv[1]
output_folder = sys.argv[2]

# print(image_folder, output_folder)

# check if new/exists if not create it
if not os.path.exists(output_folder):
    os.makedirs(output_folder)


# loop through Pokedex
for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    clean_name = os.path.splitext(filename)
    print(clean_name)
    img.save(f'{output_folder}{clean_name[0]}.png', 'png')
    print('all done!')


# convert images to png
# save them to the new folder
