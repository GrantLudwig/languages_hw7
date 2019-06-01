# Homework 7
import re

# REGULAR EXPRESSIONS

# Write patterns for regular expressions a-c here.
# You must use a single regular expression for each item.
# For part d, also include a substitution string.

a = re.compile(r"")

b = re.compile(r"")

c = re.compile(r"")

d = re.compile(r"")
subStr = r""   # Place what you want to substitute (used in sub)

# TESTS

# Write additional tests for each item.
# Include both matching and non-matching tests.
# A portion of your grade will be based on the thoroughness of your tests.

print("----Part a tests that match:")
print(a.search("$3.56"))

print("----Part a tests that do not match:")
print(a.search("3.56"))

print("----Part b tests that match:")
print(b.search("098388719400"))

print("----Part b tests that do not match:")
print(b.search("098388749100"))

print("----Part c tests that match:")
print(c.search("['H', 'e', 'l', 'l', 'o']"))

print("----Part c tests that do not match:")
print(c.search("['H', 'e', 'l', '7', 'o']"))

print("----Part d tests that match (and should change):")
print(d.sub(subStr, "May 29, 2019"))

print("----Part d tests that match (and should remain unchanged):")
print(d.sub(subStr, "May 29 19"))

