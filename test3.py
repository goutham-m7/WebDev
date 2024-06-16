import csv


def read_numbers_from_csv(filename):
    numbers = set()
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            numbers.add(int(row[0])) 
    return numbers


present_numbers = read_numbers_from_csv('present.csv')
main_numbers = read_numbers_from_csv('main.csv')


numbers_not_in_present = main_numbers - present_numbers

with open('numbers_not_in_present.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for number in numbers_not_in_present:
        writer.writerow([number])

print("Numbers in 'main' but not in 'present' have been saved to 'numbers_not_in_present.csv'.")
