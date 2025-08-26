from PIL import Image, ImageFilter

img = Image.open('./pokedex/pikachu.jpg')
filtered_image = img.convert('L') #Converts the picture. Diffrent choices available
filtered_image.save('grey.png', 'png')

#box = (100, 100, 400, 400)
#region = filtered_image.crop(box)
#region.save('cropped.png', 'png')

#resize = filtered_image.resize((300, 300))
#resize.save('resized.png', 'png')

#filtered_image.show()#Opens a window with the picture showing
#crooked = filtered_image.rotate(90)#Rotates the picture
#crooked.save('crooked.png', 'png')

#filtered_image = img.filter(ImageFilter.BLUR) #other options are SMOOTH, SHARPEN
#filtered_image.save('blur.png', 'png')


#Get diffrent information about the picture:
#print(img)
#print(img.format)
#print(img.size)
#print(img.mode)
#print(dir(img))