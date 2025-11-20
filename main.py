geusts = "Ben"  "Marie"  "Mark"
for person in ("(ben)", "(marie)", "(mark)"):
    print(f"Hello {person}, I would like to invite you to dinner")

    # one geusts can't make it
geust: str = "Ben" "Marie" "Mark"
unable_to_attend = "Ben"
print(f"unfortunately, (unable_to_attend) can't make it to the dinner")

# Replace guest

# print new invitations
for person in geusts:
    print("hello {roy}, you are invited to dinner!")

guests = ["roy", "marie", "cynthia"]
print("good news we found a bigger dinner table.")
# Add new guests
guests.insert(0, "eva")
guests.insert(len(guests) // 2, "frank")
guests.append("noel")
for persons in guests:
    print(f"hello {geusts}, you are invited to dinner!")
