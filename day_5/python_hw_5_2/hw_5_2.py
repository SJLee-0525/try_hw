# 아래 함수를 수정하시오.
def count_character(sentence, target):
    sentence = list(sentence)
    
    count = 0
    for s in sentence:
        if target == s:
            count += 1
    
    return count

result = count_character("Hello, World!", "o")
print(result)  # 2
