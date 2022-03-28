from PIL import Image, ImageFilter

img = Image.open("./section17/pokedex/pikachu.jpg")
filtered_img = img.filter(ImageFilter.BLUR)
filtered_img.save("blur.png", "png")
