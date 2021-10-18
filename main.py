import sys
from PIL import Image, ImageDraw, ImageFont

def square_box(image):
    
    width = image.size[0]
    height = image.size[1]
    short_edge = min(height, width)

    left = (width - short_edge) / 2
    upper = (height - short_edge) / 2
    right = left + short_edge
    bottom = upper + short_edge

    return (left, upper, right, bottom)

def resize_square(image):
    
    dimension=720

    return image.resize(
    (dimension, dimension),
    resample = None,
    box = square_box(image),
    reducing_gap = None)

def write_text(image_dir, text, text_color, text_pos='center'):

    image = resize_square(Image.open(image_dir))

    font = ImageFont.truetype("font.ttf", 72)
    v_pos = (0.5 if text_pos == 'center' else (0.2 if text_pos == 'up' else 0.8))

    draw = ImageDraw.Draw(image)

    text_width, text_height = draw.textsize(text, font=font)

    # sketchy handler for longer text
    if text_width > 640:
        times = text_width/640
        font = ImageFont.truetype("font.ttf", int(72/times))
        text_width, text_height = draw.textsize(text, font=font)

    text_height += int(text_height*0.2)
    text_h_pos = (720-text_width)*0.5
    text_v_pos = (720-text_height)*v_pos

    draw.text((text_h_pos, text_v_pos), text=text, fill=text_color, font=font)
    
    return image

if __name__ == "__main__":
    '''
    How to run:
    $ python3 main.py image_directory 'Cover Title' text_color text_position
    '''

    image_dir = sys.argv[1] # background image directory
    title = sys.argv[2] # a string
    text_color = sys.argv[3] # 'white' or '#ffffff' or (255, 255, 255)
    text_pos = sys.argv[4] # 'center' or 'up' or 'down'

    write_text(image_dir, title, text_color, text_pos).save(f"{title} cover.jpg")
    
    print(f"Image saved as '{title} cover.jpg' in the current directory.")
