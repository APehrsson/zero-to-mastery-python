from translate import Translator

translator = Translator(to_lang="ja")

with open('test.txt', mode='r') as my_file:
        to_be_translated = my_file.read()

translation = translator.translate(to_be_translated)
with open('test-ja.txt', mode='w') as my_file2:
        my_file2.write(translation)

print(translation)