with open('sad.txt', mode='w') as my_file: #better way to read files. Doesn't require for you to close the file after opening it
    text = my_file.write(':(')
    print(text)

