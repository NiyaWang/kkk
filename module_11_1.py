from PIL import Image
im = Image.open("fe.jpg")

im.show()

print(im.format, im.size, im.mode)
new_size = (600, 800)
resized_image = im.resize(new_size)
resized_image.save("fe1.jpg")
resized_image.show()

out = im.point(lambda i: i * 20)
out.show()

im.save("fe2.png")
