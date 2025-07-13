def check_number(num):
    if num > 7:
        print("Hello")

def check_name(name):
    if name == "John":
        print("Hello, John")
    else:
        print("There is no such name")

def filter_multiples_of_three(arr):
    print("Numbers divisible by 3:")
    for number in arr:
        if number % 3 == 0:
            print(number)

def main():
    try:
        number_input = int(input("Enter a number: "))
        check_number(number_input)
    except ValueError:
        print("Invalid input. Please enter an integer.")

    name_input = input("Enter a name: ")
    check_name(name_input)

    array_input = input("Enter numbers separated by spaces: ")
    try:
        array = list(map(int, array_input.split()))
        filter_multiples_of_three(array)
    except ValueError:
        print("Invalid input. Please enter numbers only.")

if __name__ == "__main__":
    main()
