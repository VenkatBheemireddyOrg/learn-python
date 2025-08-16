import sys

x = sys.argv[1]

if x == "t2.micro":
    print("the micro instance is 2 dollars cost")
elif x == "t2.medium":
    print("the medium instance is 4 dollars cost")
elif x == "t2.large":
    print("the large instance is 6 dollars cost")
else:
    print("the requested instance is not available")
