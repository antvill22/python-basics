def convert(input):
    input = input.replace(":)", "🙂" )
    input = input.replace(":(", "🙁")
    return input

def main():
    user_input = input()
    converted_str = convert(user_input)
    print(converted_str)

main()