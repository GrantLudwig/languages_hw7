# Homework 7
import re

# REGULAR EXPRESSIONS

# Write patterns for regular expressions a-c here.
# You must use a single regular expression for each item.
# For part d, also include a substitution string.

#a = re.compile(r"^\$[1-9][0-9]*(.[0-9]{2})?")
a = re.compile(r"^\$([1-9][0-9]*|0)(.[0-9]{2}$)?$")

b = re.compile(r"^(3|[0,2,5,6,7,8,9]+$|"
               r"[0,2,5,6,7,8,9]+3)[0,2,5,6,7,8,9]*"
               r"($|1)[0,2,5,6,7,8,9]*"
               r"($|4)[0,2,5,6,7,8,9]*$")

c = re.compile(r"^\[(('[a-zA-Z]', )*'[a-zA-Z]')?\]$")

#Old version
#d = re.compile(r"^(?P<month>[A-Z][a-z]{2})\s(?P<day>[0-3]?[1-9]),?\s[0-9]{2}(?P<year>[0-9]{2})$")
d = re.compile(r"^(?P<month>Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+"
               r"(?P<day>[0-3]?[0-9]),?\s+"
               r"[0-9]{2}(?P<year>[0-9]{2})$")
subStr = r"\g<day> \g<month> \g<year>"   # Place what you want to substitute (used in sub)

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
print(c.search("[]"))
print(c.search("['H']"))
print(c.search("['H', 'e', 'L', 'l', 'O', 'T', 'h', 'e', 'r', 'e']"))
print(c.search("['H', 'e', 'L', 'l', 'O', 'T', 'h', 'e', 'r', 'e', 't', 'e', 's', 't']"))

print("----Part c tests that do not match:")
print(c.search("Nope"))
print(c.search("['H', 'e', 'l', '7', 'o']"))
print(c.search("['H', 'e', 'L', 'l', 'O', ' ', 'T', 'h', 'e', 'r', 'e']"))
print(c.search("['H',]"))
print(c.search("[ 'H']"))
print(c.search("[ ]"))
print(c.search("['H',  'e']"))
print(c.search("['H', 'e', ':', 'l', 'o']"))
print(c.search("['Hello', 'there']"))
print(c.search("('l', 'l')"))
print(c.search("['Hello', 'there'"))

print("----Part d tests that match (and should change):")
print(d.sub(subStr, "May 29, 2019"))
print(d.sub(subStr, "May 29 1818"))
print(d.sub(subStr, "Oct 02 1990"))
print(d.sub(subStr, "Jan 1 0000"))
print(d.sub(subStr, "Jan   30  5000"))

print("----Part d tests that match (and should remain unchanged):")
print(d.sub(subStr, "May 29 19"))
print(d.sub(subStr, "May 29 19000"))
print(d.sub(subStr, "May 29 400"))
print(d.sub(subStr, "oct 29 2019"))
print(d.sub(subStr, "October 26 1997"))
print(d.sub(subStr, "Nope"))
print(d.sub(subStr, "Oct. 26, 1997"))
print(d.sub(subStr, "The 1 2000"))

