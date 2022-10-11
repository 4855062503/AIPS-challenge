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

def main():
    # main function to run | void
    with open("input.txt", "r") as f:
        total = count_all(f)
        print("total is {0}".format(total))
main()

