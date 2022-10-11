'''
AIPS Coding Challenge - Alex Boyle / +642102693307
'''
import io

def print_stars():
    # prints a row of asterisks | void
    print("*********************\n")

def count_all(file_name):
    # returns a total | int
    with open(file_name, "r") as file_:
        total = 0
        for line in file_:
            line_array = line.split()
            total += int(line_array[len(line_array) - 1])
        return total

def return_dates(file_name):
    # returns all dates + count | str
    return_str = ""
    with open(file_name, "r") as file_:
        for line in file_:
            line_array_date = line.split('T')
            date = line_array_date[0]
            line_array_count = line.split()
            count = int(line_array_count[len(line_array_count) -1])
            return_str += "{0} {1}\n".format(date, count)
    return return_str

def top_three(file_name):
    # returns the top three half hours by count | str
    return_str = ""
    with open(file_name, "r") as file_:
        count_dict = {}
        for line in file_:
            line_array = line.split()
            count_dict["{0}".format(line)] = int(line_array[len(line_array) - 1])
        sorted_array = sorted(count_dict, key=count_dict.get, reverse=True)
        return_str += sorted_array[0]
        return_str += sorted_array[1]
        return_str += sorted_array[2]
    return return_str

def least_cars(file_name):
    # returns the cars with the least total in 1.5hrs | str
    return_str = ""
    with open(file_name, "r") as file_:
        min_value = 99999999999999999999999999999999999999999
        min_array = []
        lines_array = file_.readlines()
        for x in range(len(lines_array)):
            if x < len(lines_array) - 3:
                line_a_array = lines_array[x].split()
                line_b_array = lines_array[x+1].split()
                line_c_array = lines_array[x+2].split()
                line_a_count = int(line_a_array[len(line_a_array) - 1])
                line_b_count = int(line_b_array[len(line_b_array) - 1])
                line_c_count = int(line_c_array[len(line_c_array) - 1])
                count_sum = line_a_count + line_b_count + line_c_count 
                if count_sum < min_value:
                    min_value = count_sum
                    min_array = [lines_array[x], lines_array[x+1], lines_array[x+2]]
            else:
                break
        for line in min_array:
            return_str += line
        return return_str

def main():
    # main function to run | str
    print_stars()
    total = count_all("input.txt")
    print("total is {0}\n".format(total))
    print_stars()
    print(return_dates("input.txt"))
    print_stars()
    print(top_three("input.txt"))
    print_stars()
    print(least_cars("input.txt"))
    print_stars()
main()

