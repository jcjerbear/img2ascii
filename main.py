# import PIL Image for image processing
# import argparse for command line inputs
from PIL import Image
import argparse

# command line input argument handler
parser = argparse.ArgumentParser()

parser.add_argument('file') # input file
parser.add_argument('-o', '--output') # output file
parser.add_argument('--width', type = int, default = 100) # output asciiImage width
parser.add_argument('--height', type = int, default = 100) # output asciiImage height

# obtain/prompt arguments
args = parser.parse_args()

IMG = args.file
WIDTH = args.width
HEIGHT = args.height
OUTPUT = args.output

# define asciiImage character list containing 70 char
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

# RGB to char method: reflect 256 gray scale values onto 70 characters
def RGB2char(r,g,b,alpha = 256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    unit = (256.0 + 1)/length
    return ascii_char[int(gray/unit)]

if __name__ == '__main__':
    txt = "" # initialize txt string
    im = Image.open(IMG) # open up image file according to filename
    im = im.resize((WIDTH,HEIGHT), Image.NEAREST) # resize input image to output requirement size

    for i in range(HEIGHT): # for each row of the resized image
        for j in range(WIDTH): # for each column of the resized image
            txt += RGB2char(*im.getpixel((j,i)))
        txt += '\n'

    print(txt)

    # output asciiImage to output text file
    if OUTPUT:
        with open(OUTPUT,'w') as f:
            f.write(txt)
    else:
        with open("output.txt",'w') as f:
            f.write(txt)
