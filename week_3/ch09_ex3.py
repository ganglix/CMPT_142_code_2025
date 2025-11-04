# Write a Python function that uses a for-loop to print the
# number of times each lowercase vowel (a,e,i,o,u) occurs in a
# string s. e.g. "piece" prints "a:0 e:2 i:1 o:0 u:0".
from statsmodels.sandbox.regression.try_ols_anova import anova_str

s = "piece"

# check only 'e': how many 'e's are there, print e:2
a_count = 0
e_count = 0
for c in s:
    if c == 'a':
        a_count += 1
    if c == 'e':
        e_count += 1
print("a:"+str(a_count), "e:"+str(e_count))
