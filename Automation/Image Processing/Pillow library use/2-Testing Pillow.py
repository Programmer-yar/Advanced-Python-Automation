from PIL import Image

size = (350, 350)

im = Image.open("debt.jpg")
print(im.format, im.size, im.mode)
im1 = im.resize(size)
im1.save('debt-resized-thumbnail.jpg')

