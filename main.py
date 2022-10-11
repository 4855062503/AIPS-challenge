'''
AIPS Coding Challenge - Alex Boyle / +642102693307
'''
import io

def print_stars():
    # prints a row of asterisks | void
    print("*********************\n")

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
        print("{0} {1}\n".format(date, count))

def top_three(file_):
    # prints the top three half hours by count | void
    count_dict = {}
    for line in file_:
        line_array = line.split()
        count_dict["{0}".format(line)] = int(line_array[len(line_array) - 1])
    sorted_array = sorted(count_dict, key=count_dict.get, reverse=True)
    print(sorted_array[0]) 
    print(sorted_array[1]) 
    print(sorted_array[2]) 

def main():
    # main function to run | void
    print_stars()
    with open("input.txt", "r") as f:
        total = count_all(f)
        print("total is {0}\n".format(total))
    print_stars()
    with open("input.txt", "r") as f:
        print_dates(f)
    print_stars()
    with open("input.txt", "r") as f:
        top_three(f)
    print_stars()
main()

