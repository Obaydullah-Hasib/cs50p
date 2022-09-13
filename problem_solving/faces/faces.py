def main():
    string = input()
    string = emoji_converter(string)
    print(string, end="")


def emoji_converter(string):
    string = string.replace(":)", "🙂").replace(":(", "🙁")
    return string


main()
