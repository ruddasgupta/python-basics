import time


def print_file_content():
    with open('first.txt', 'r') as first, open('second.txt', 'r') as second:
        print('First File')
        print(first.read())
        time.sleep(2)
        print('Second File')
        print(second.read())


if __name__ == '__main__':
    # open both files
    with open('first.txt', 'r') as first_file, open('second.txt', 'a') as second_file:

        print_file_content()

        # read content from first file
        for line in first_file:
            # append content to second file
            second_file.write(line)

        print_file_content()
