import random


def generate_random_string(length):
    letters_and_digits = [chr(i) for i in range(97, 123)] + [str(i) for i in range(10)]
    return ''.join(random.choices(letters_and_digits, k=length))
if __name__=="__main__":
    print(f"RA_CO={generate_random_string(8)}")