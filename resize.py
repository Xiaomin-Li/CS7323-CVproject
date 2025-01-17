from PIL import Image
import os, sys

# path = "/home/lixm/Desktop/srgan/data2017/DIV2K_train_LR_bicubic_X4/DIV2K_train_LR_bicubic/X4/"
path = '/home/lixm/Desktop/ESRGAN/LR/'
dirs = os.listdir( path )

final_size = 128;

def resize_aspect_fit():
    for item in dirs:
         if item == '.DS_Store':
             continue
         if os.path.isfile(path+item):
             im = Image.open(path+item)
             f, e = os.path.splitext(path+item)
             size = im.size
             ratio = float(final_size) / max(size)
             new_image_size = tuple([int(x*ratio) for x in size])
             im = im.resize(new_image_size, Image.ANTIALIAS)
             new_im = Image.new("RGB", (final_size, final_size))
             new_im.paste(im, ((final_size-new_image_size[0])//2, (final_size-new_image_size[1])//2))
             new_im.save(f + 'resized.png', 'PNG', quality=90)
resize_aspect_fit()
