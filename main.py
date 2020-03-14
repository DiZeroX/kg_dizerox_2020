import sys


def is_one_to_one_mapped(s1, s2):
    # TODO: complete function
    if len(s1) != len(s2):
        return False

    character_map = {}
    for index, char in enumerate(s1):
        if char in character_map:
            # A repeated character in string1 must have the same mapped character in string2
            if character_map[char] != s2[index]:
                return False
        else:
            character_map[char] = s2[index]
    return True


if __name__ == "__main__":
    if len(sys.argv) != 3:  # Exactly 2 command line arguments are required
        sys.exit("Invalid number of arguments")
    string1 = sys.argv[1]
    string2 = sys.argv[2]
    result = is_one_to_one_mapped(string1, string2)
    output = str(result).lower()
    print(output)

