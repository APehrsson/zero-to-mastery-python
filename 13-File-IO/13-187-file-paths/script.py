with open('../13-186-read-write-append/sad.txt', mode='a') as my_file:
    text = my_file.write(':(..')
    print(text)