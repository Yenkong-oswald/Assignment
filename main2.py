places = ["Cameroon", "New York", "Cape Town", "Ghana", "Sydney"]

print("Original list:")
print(places)

print("\nAlphabetical order (using sorted):")
print(sorted(places))

print("\nList after sorted() call (should be unchanged):")
print(places)

print("\nReverse alphabetical order (using sorted with reverse=True):")
print(sorted(places, reverse=True))

print("\nList after reverse sorted() call (should be unchanged):")
print(places)

places.reverse()
print("\nList after reverse():")
print(places)

places.reverse()
print("\nList after second reverse() (back to original):")
print(places)

places.sort()
print("\nList after sort() (alphabetical):")
print(places)

places.sort(reverse=True)
print("\nList after sort(reverse=True) (reverse alphabetical):")
print(places)