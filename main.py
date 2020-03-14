import sys


def is_one_to_one_mapped(string1, string2):
    # TODO: complete function
    return False


if __name__ == "__main__":
    if len(sys.argv) != 3:  # Exactly 2 command line arguments are required
        sys.exit("Invalid number of arguments")
    string1 = sys.argv[0]
    string2 = sys.argv[1]
    output = is_one_to_one_mapped(string1, string2)
    print(output)

