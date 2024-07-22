# 아래 함수를 수정하시오.
def reverse_string(string):
    string = list(string)

    string.reverse()
    string = ''.join(string)
    
    return string

result = reverse_string("Hello, World!")
print(result)  # !dlroW ,olleH
