# This demonstration shows you how to call methods on string objects.


# initialize some variables to play with
url = 'www.engineering.usask.ca'

# find the location of the first period in the url
print(url.find('.'))  # .find() will return the index of the first found

# count the number of periods in the url
print(url.find('.'))

# find the location of the SECOND period in the url
first_period_index = url.find('.')
short_url = url[first_period_index+1 : ]
print(short_url)
first_period_index_short_url = short_url.find('.')
print('index of second period in url is ',
      first_period_index_short_url + first_period_index + 1)



#----------------------------------------
s = ' CMPT 142 '
# remove white space
print(
s.rstrip(),  # remove trailing space
s.lstrip(),  # remove leading space
s.strip(),   # remove both leading and trailing space
s.replace(' ', ''),  # replace all spaces with empty string ''
s.strip().count(' '),   # count number of spaces excluding leading or trailing space
sep = ('\n')
)

# ------------------------
# count the number of characters in the url after removing "www."
print(url.replace('www.', ''))
print(url.removeprefix('www.'))

print('use lstrip() to remove')
print(url.lstrip('www.'))
print(url.lstrip('w.'))   # w and . are the garbage to be removed, so it removes w s and .
u#rl.lstrip() is the same as url.lstrip(' ')

# useful in practice?
# letter = input(' please type a letter in lowercase: ').lower()
# print(letter)


# strings are immutable, all these methods create a copy




# how do I know what kind of methods are out there? How do I know the syntax/usage?
# dir('letter')
# help('letter'.upper)   # upper is the method name, do not include ()
