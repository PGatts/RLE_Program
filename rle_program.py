# Param Gattupalli
# RLE Project

from console_gfx import ConsoleGfx

# Convert list into hexadecimal values
def to_hex_string(data):
    result = ''
    # Convert to hexadecimal digit by digit
    for digit in data:
        char = str(digit) if digit < 10 else chr(digit + 87)
        result += char
    return result

# Determine how many runs of a single number there are
def count_runs(flat_data):
    i, count, j = 0, 0, 0
    while i < len(flat_data):
        # Count runs until reaching the end of the list or the run becomes longer than 15
        while i + j < len(flat_data) and flat_data[i+j] == flat_data[i] and j < 16:
            j += 1
        i += j
        count += 1
        j = 0
    return count

# Convert flat data into rle data
def encode_rle(flat_data):
    i, j = 0, 0
    rle_data =[]

    while i < len(flat_data):
        # Count runs until reaching the end of the list or the run becomes longer than 15
        while i + j < len(flat_data) and flat_data[i+j] == flat_data[i] and j < 15:
            j += 1

        # Add the count of the run and the repeating digit to the rle list
        rle_data.append(j)
        rle_data.append(flat_data[i])
        i += j
        j = 0
    return rle_data

# Determine how long the flat data list will be based on rle data
def get_decoded_length(rle_data):
    length = 0
    # Sums up values in even indices
    for i in range(0,len(rle_data),2):
        length += rle_data[i]
    return length

# Convert rle data list to flat data list
def decode_rle(rle_data):
    i = 0
    flat_data = []
    for i in range(0,len(rle_data),2):
        for j in range(rle_data[i]):
            flat_data.append(rle_data[i+1])

    return flat_data

# Convert hexadecimal string to flat data list
def string_to_data(data_string):
    data = []
    # Insert decimal value of each character in the string to the list
    for char in data_string:
        if char.isdigit():
            data.append(int(char))
        else:
            data.append(ord(char.lower()) - 87)

    return data

# Convert rle data list to readable rle data string
def to_rle_string(rle_data):
    result = ''
    # Append run length and digit to string, dividing each run with ':'
    for i in range(0,len(rle_data), 2):
        digit = rle_data[i+1]
        digit = str(digit) if digit < 10 else chr(digit + 87)
        result += str(rle_data[i]) + digit + ':'
    return result[:-1]

# Convert readable rle data string to rle data list
def string_to_rle(data_string):
    rle_data = []
    runs = data_string.split(':')
    for run in runs:
        num = int(run[:-1])
        rle_data.append(num)

        char = run[-1]
        char = int(char) if char.isdigit() else ord(char.lower()) - 87
        rle_data.append(char)

    return rle_data


# Prints user menu
def print_menu():
    print("\nRLE Menu")
    print("--------")
    print("0. Exit")
    print("1. Load File")
    print("2. Load Test Image")
    print("3. Read RLE String")
    print("4. Read RLE Hex String")
    print("5. Read Data Hex String")
    print("6. Display Image")
    print("7. Display RLE String")
    print("8. Display Hex RLE Data")
    print("9. Display Hex Flat Data")


def main():
    # Display intro messages
    print("Welcome to the RLE image encoder!\n")

    print("Displaying Spectrum Image:")
    ConsoleGfx.display_image(ConsoleGfx.test_rainbow)

    # Continues until user chooses to exit
    choice = -999
    while choice != 0:
        print_menu()
        choice = int(input("\nSelect a Menu Option: "))

        # Performs operation based on user input
        match choice:
            case 0:
                exit()
            case 1:
                image_data = ConsoleGfx.load_file(input("Enter name of file to load: "))
            case 2:
                image_data = ConsoleGfx.test_image
                print("Test image data loaded.")
            case 3:
                rle_string = input("Enter an RLE string to be decoded: ")
                image_data = decode_rle(string_to_rle(rle_string))
            case 4:
                rle_hex_string = input("Enter the hex string holding RLE data: ")
                image_data = decode_rle(string_to_data(rle_hex_string))
            case 5:
                flat_hex_string = input("Enter the hex string holding flat data: ")
                image_data = string_to_data(flat_hex_string)
            case 6:
                if image_data == ConsoleGfx.test_image:
                    print("Displaying image...")
                ConsoleGfx.display_image(image_data)
            case 7:
                print("RLE representation:", to_rle_string(encode_rle(image_data)))
            case 8:
                print("RLE hex values:", to_hex_string(encode_rle(image_data)))
            case 9:
                print("Flat hex values:", to_hex_string(image_data))


if __name__ == "__main__":
    main()
