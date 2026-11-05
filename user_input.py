from validations import validate_positive_num

def user_input_num(msg):
    input_num = ""
    while not validate_positive_num(input_num):
        print("You must enter a positive whole number.")
        input_num = input(f"{msg}: ")
    return int(input_num)

if __name__ == "__main__":
    user_input_num("hi")