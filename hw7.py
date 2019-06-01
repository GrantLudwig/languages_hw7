# Homework 7
import re

# REGULAR EXPRESSIONS

# Write patterns for regular expressions a-c here.
# You must use a single regular expression for each item.
# For part d, also include a substitution string.

#a = re.compile(r"^\$[1-9][0-9]*(.[0-9]{2})?")
a = re.compile(r"^\$([1-9][0-9]*|0)(.[0-9]{2}$)?$")

b = re.compile(r"^(3|[0,2,5,6,7,8,9]+$|[0,2,5,6,7,8,9]+3)[0,2,5,6,7,8,9]*($|1)[0,2,5,6,7,8,9]*($|4)[0,2,5,6,7,8,9]*$")

c = re.compile(r"")

d = re.compile(r"")
subStr = r""   # Place what you want to substitute (used in sub)

# TESTS

# Write additional tests for each item.
# Include both matching and non-matching tests.
# A portion of your grade will be based on the thoroughness of your tests.

print("----Part a tests that match:")
print(a.search("$3.56"))
print(a.search("$0.00"))
print(a.search("$0"))
print(a.search("$100"))
print(a.search("$100.10"))
print(a.search("$1000000570.02"))
print(a.search("$706.00"))
print(a.search("$0.25"))

print("----Part a tests that do not match:")
print(a.search("3.56"))
print(a.search("$3.565"))
print(a.search("$003.00"))
print(a.search("$3."))
print(a.search("$0.1"))
print(a.search("$00"))
print(a.search("$00060"))
print(a.search("Not money"))

print("----Part b tests that match:")
print(b.search("098388719400"))
print(b.search("3"))
print(b.search("31"))
print(b.search("314"))
print(b.search("06928388719050"))
print(b.search("0962838879050"))
print(b.search("069828879500"))

print("----Part b tests that do not match:")
print(b.search("098388749100"))
print(b.search("330"))
print(b.search("3030"))
print(b.search("0330"))
print(b.search("04440"))
print(b.search("01110"))
print(b.search("040"))
print(b.search("010"))
print(b.search("0340"))
print(b.search("03410"))
print(b.search("0140"))
print(b.search("04130"))
print(b.search("01340"))
print(b.search(""))
print(b.search("Not digits"))

print("----Part c tests that match:")
print(c.search("['H', 'e', 'l', 'l', 'o']"))

print("----Part c tests that do not match:")
print(c.search("['H', 'e', 'l', '7', 'o']"))

print("----Part d tests that match (and should change):")
print(d.sub(subStr, "May 29, 2019"))

print("----Part d tests that match (and should remain unchanged):")
print(d.sub(subStr, "May 29 19"))

