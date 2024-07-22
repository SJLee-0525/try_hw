# 아래 함수를 수정하시오.
def capitalize_words(input_words):
    split_words_list = input_words.split(' ')
    
    new_words_list = []
    for split_word in split_words_list:
        new_word_list = []

        split_word_list = list(split_word)
        split_word_list[0] = split_word_list[0].upper()

        new_word = ''.join(split_word_list)
        new_words_list.append(new_word)
    
    new_words = ' '.join(new_words_list)
    
    return new_words


result = capitalize_words("hello, world!")
print(result)
