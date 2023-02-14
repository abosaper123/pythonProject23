from PIL import Image
my_image=Image.open("F:\players\8036d57eef28b99f0ddab55820932414.png")
my_image.show()
my_box=(500,500,800,800)
my_newimage=my_image.crop(my_box)
my_newimage.show()
my_converted=my_image.convert("L")
my_converted.show()