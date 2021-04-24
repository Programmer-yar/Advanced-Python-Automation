from PIL import Image
image_path = "flying_suite.jpg"
rename = "flying_suite resized 350x350.jpg"
im = Image.open(image_path)
print(im.format, im.size, im.mode)

im1 = im.convert('RGB')
im1 = im1.resize((350, 350))
print(im1.size)
im1.save(rename)
