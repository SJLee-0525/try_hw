def rental_book(name, borrow_book):
    decrease_book(borrow_book)
    print(f'{name}님이 {borrow_book}권의 책을 대여하였습니다.')

def decrease_book(borrow_book):
    global number_of_book
    number_of_book -= borrow_book
    print(f'남은 책의 수 : {number_of_book}')

number_of_book = 100

rental_book('홍길동', 3)
