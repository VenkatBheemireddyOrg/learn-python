mobile = "012-456-890"

my_list = ["0","1","2","3","4","5","6","7","8","9"]

m1 = mobile[0:1]
m2 = mobile[1:2]
m3 = mobile[2:3]
s1 = mobile[3:4]
m4 = mobile[4:5]
m5 = mobile[5:6]
m6 = mobile[6:7]
s2 = mobile[7:8]
m7 = mobile[8:9]
m8 = mobile[9:10]
m9 = mobile[10:11]

result = True

if s1 != "-":
    result = False

if s2 != "-":
    result = False

print(m1)

if m1 not in my_list :
    result = False

if m2 not in my_list :
    result = False

if m3 not in my_list :
    result = False

if m4 not in my_list :
    result = False

if m5 not in my_list :
    result = False

if m6 not in my_list :
    result = False

if m7 not in my_list :
    result = False

if m8 not in my_list :
    result = False

if m9 not in my_list :
    result = False

print("result is :", result)
