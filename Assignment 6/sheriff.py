from hashtable import *
import csv
import re

reverse_lookup = HashTable(2**11)


def valid_number(phone_number):
    pattern = re.compile("^[\dA-Z]{3}-[\dA-Z]{3}-[\dA-Z]{4}$", re.IGNORECASE)
    return pattern.match(phone_number) is not None


if __name__ == '__main__':
    # load phone directory into hash table
    with open('phone_database.csv', newline='') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            reverse_lookup.put(row[2], row[1] + ' ' + row[0])
        print('Loaded', len(reverse_lookup), 'items.')

    while True:
        phone = input('Enter a phone number to search for, or 0 to quit: ')
        if phone == '0':
            print('Exiting.')
            exit(1)
        elif not valid_number(phone):
            print('Invalid format for phone number. Try again.')
        else:
            result, slot = reverse_lookup.get(phone)
            if result is None:
                print('No such number in the registry.')
            else:
                print('{} is registered to {}. The data is stored in slot {}.'.format(phone, result, slot))
