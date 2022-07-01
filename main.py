from PIL import Image 
from os import listdir
from configparser import ConfigParser

#reading input_path, output_path and treshold from config file
config = ConfigParser()
config.read("config.ini")

#setting it into variables
treshhold = config.get("config_data", "treshhold")
input_path = config.get("config_data", "input_path")
output_path = config.get("config_data", "output_path")


def calculate_brightness(image):
    
    greyscale_image = image.convert('L') 
    histogram = greyscale_image.histogram() 
    pixels = sum(histogram) 
    brightness = len(histogram)
    scale = len(histogram)

    for index in range(0, scale):
        ratio = histogram[index] / pixels
        brightness += ratio * (index - scale)
    return(100 if brightness == 255 else round((brightness / scale)*100))

for i in listdir(input_path):
    picture = Image.open(input_path + i)
    calculated = calculate_brightness(picture)
    position_of_dot = i.find('.')
    if calculated >= int(treshhold):
      picture.save(output_path+i[:position_of_dot]+'_bright_'+str(calculated)+i[position_of_dot:])
    else:
      picture.save(output_path+i[:position_of_dot]+'_dark_'+str(calculated)+i[position_of_dot:])
