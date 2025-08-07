basket = [1,2,3,4,5]
#Length of list
print(len(basket))

#adding
basket.append(100)
new_list = basket
print(basket)
print(new_list)

basket.insert(4,100)
print(basket)

#removeing
basket.pop(0) #om inget anges tar den bort det sista, om siffra enges tar den bort enligt index
print(basket)

#clear tar bort hela listan

basket = ['a','b','c','d','e','d']
print(basket.index('d', 0, 4)) #man kan söka efter en specefik sak i listan eller ange ett spann att söka mellan, tex 0-4

print('d' in basket)
print('x' in basket)

print(basket.count('d'))

basket.sort()
print(basket)
print(sorted(basket)) #visar listan i ordning utan att ändra den, mer än i det begärda resultatet
basket.reverse()
print(basket)

print(list(range(1,100)))
print(list(range(100)))

sentence = '!'
new_sentence = sentence.join(['Hi', 'my', 'name', 'is', 'JOJO'] )

print(new_sentence)

