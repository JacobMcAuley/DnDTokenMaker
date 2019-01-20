import numpy as np
from PIL import Image, ImageDraw, ImageChops

OFFSET = 20
OFFSET2 = 20

def crop_image(x, y, x2, y2, image):

    # Open the input image as numpy array, convert to RGB
    img=Image.open(image).convert("RGB")
    npImage=np.array(img)

    # Create same size alpha layer with circle
    alpha = Image.new('L', img.size,0)
    draw = ImageDraw.Draw(alpha)
    draw.ellipse([x - OFFSET, y - OFFSET, (x+x2) + OFFSET2, (y+y2) +OFFSET2], fill=255)

    # Convert alpha Image to numpy array
    npAlpha=np.array(alpha)

    # Add alpha layer to RGB
    npImage=np.dstack((npImage,npAlpha))

    # Save with alpha\
    Image.fromarray(npImage).save('result.png')

    img2 = Image.open('result.png')
    img2.crop([x - OFFSET, y - OFFSET, (x+x2) + OFFSET2, (y+y2) +OFFSET2]).save('token.png')