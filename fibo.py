# from lazy_streams import stream
import time


def factorial(number: int) -> int:
    if number == 1:
        return 1
    else:
        return number * factorial(number-1)


def another_factorial(number: int, acc: int) -> int:
    if number <= 1:
        return acc
    else:
        return another_factorial(number-1, number * acc)


def concatenate_n_times(word: str, number: int, acc: str) -> str:
    if number <= 0:
        return acc
    else:
        return concatenate_n_times(word, number-1, f'{word} {acc}')


def is_prime(number: int) -> bool:
    def is_prime_until(half: int) -> bool:
        if half <= 1:
            return True
        else:
            return number % half != 0 and is_prime(half-1)
    return is_prime_until(number // 2)


def increment_numbers(numbers=None):
    if numbers is None:
        numbers = []
    for i in range(3):
        numbers.append(i)
    print(f'Numbers: {numbers}')



def get_even_numbers(numbers):
    start = time.time()
    even_numbers = []
    if numbers is not None:
        even_numbers = [x for x in numbers if x % 2 == 0]
    end = time.time()
    print(end - start)



def get_users():
    print("Les rèves des gens")



if __name__ == '__main__':
    user = 0
    if user:
        print("Bonjour")
    # get_users()
#     # print(another_factorial(4500, 1))
#     a_list = []
#     if a_list is not None:
#         new_list = list(map(lambda x: x*2, a_list))
#         print(new_list)




