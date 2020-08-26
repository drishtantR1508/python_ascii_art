#a code by drishtant rai
# https://github.com/drishtantR1508
from PIL import Image
img = Image.open("ganapati10.jpg")

# resize the image
width, height = img.size
aspect_ratio = height/width
new_width = 120
new_height = aspect_ratio * new_width * 0.55
img = img.resize((new_width, int(new_height)))
# greyscale format
img = img.convert('L')
pixels = img.getdata()
chars = [ '@','#', '?', '%','S', '+', '.', ' ',' ',' ',' ',' ',':',',','.','.',' ']
new_pixels = [chars[pixel//25] for pixel in pixels]
new_pixels = ''.join(new_pixels)

new_pixels_count = len(new_pixels)
ascii_im = [new_pixels[index:index + new_width] for index in range(0, new_pixels_count, new_width)]
ascii_im = "\n".join(ascii_im)
print(ascii_im)


with open("ascii_image7.txt", "w") as f:
   f.write(ascii_im)
