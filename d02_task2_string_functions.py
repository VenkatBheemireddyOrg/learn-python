my_text = "   Python is great language  "
print("my_text :", my_text)

### strip() function removes both head and tail spaces
my_strip = my_text.strip()
print("my_strip :", my_strip)

my_split = my_strip.split()
print("my_split :", my_split)

my_lower = my_strip.lower()
print("my_lower :", my_lower)

my_upper = my_text.upper()
print("my_upper : ", my_upper)

print("my_length :", len(my_strip))

my_replace = my_text.replace("great", "super")
print("my_replace :", my_replace)


