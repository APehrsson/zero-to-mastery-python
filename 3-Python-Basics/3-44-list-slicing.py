#List slicing
amazon_cart = [
    'notebook',
    'sunglasses',
    'toys',
    'grapes'
]

print(amazon_cart[0:2])

print(amazon_cart[0::2])

#change list inventory
amazon_cart[0] = 'laptop'
#copy list
newcart = amazon_cart[:]
newcart[0] = 'gum'
print(newcart)
print(amazon_cart)

print(amazon_cart[1:4])
