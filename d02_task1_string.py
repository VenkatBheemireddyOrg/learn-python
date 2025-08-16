mobile = "012-456-890"

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

if m1 != "0" or "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9" :
    result = False

if m2 != "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" :
    result = False

if m3 != "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" :
    result = False

if m4 != "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" :
    result = False

if m5 != "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" :
    result = False

if m6 != "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" :
    result = False

if m7 != "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" :
    result = False

if m8 != "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" :
    result = False

if m9 != "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" :
    result = False

print("result is :", result)
