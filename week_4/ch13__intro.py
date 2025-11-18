# dictionary {key : value, key1 : value1}, Those records or pairs are not ordered

# KEYS

# VALUES

phone_book = {'Gang': '3068888888', 'Luigi': '2131111111'}
print(phone_book['Gang'])


# what type of data can be a dictionary key
# immutable data can be a key, int, float, string

# add record
phone_book['Mario'] = '2132222222'
# change a record
phone_book['Mario'] = '2138888888'

print(phone_book)

# remove record
phone_book.pop('Mario')   # pop using key
print(phone_book)

# look-up
# print(phone_book['bowser'])  # this will create an error
for key in phone_book:  # iterates over all keys in a dict
    if key == 'bowser':
        print(phone_book[key])

value = phone_book.get('bowser', 'bowser does not exist')  # returns bowser's phonenumber if key bowser is there, otherwise, return the message
print(value)




# value can also be a dict
contact = {'Gang': {'phone': "3068888888",
                    'email': 'gang.li@usask.ca'},
           'Luigi': {'phone': "3061111111",
                     'address': 'mushroom kingdom'}
           }


# When work with dict, always be clear: what is the key, what is the value!!