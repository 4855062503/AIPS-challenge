'''
AIPS Coding Challenge - Alex Boyle / +642102693307
'''
import io

def count_all(file_):
    # returns a total | int
    total = 0
    for line in file_:
        line_array = line.split()
        total += int(line_array[len(line_array) - 1])
    return total

def print_dates(file_):
    # prints all dates + count | void
    for line in file_:
        line_array_date = line.split('T')
        date = line_array_date[0]
        line_array_count = line.split()
        count = int(line_array_count[len(line_array_count) -1])
        print("{0} {1}".format(date, count))


def main():
    # main function to run | void
    with open("input.txt", "r") as f:
        total = count_all(f)
        print("total is {0}".format(total))
    with open("input.txt", "r") as f:
        print_dates(f)
main()

