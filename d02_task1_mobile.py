mob_nbr = "012-456-890"

mob_nbr_part1 = mob_nbr[0:3]
mob_nbr_part2 = mob_nbr[4:7]
mob_nbr_part3 = mob_nbr[8:11]

mob_nbr_delimit1 = mob_nbr[3:4]
mob_nbr_delimit2 = mob_nbr[7:8]

print("mob_nbr_part1 :", mob_nbr_part1)
print("mob_nbr_part2 :", mob_nbr_part2)
print("mob_nbr_part3 :", mob_nbr_part3)

print("mob_nbr_delimit1 :", mob_nbr_delimit1)
print("mob_nbr_delimit2 :", mob_nbr_delimit2)

valid = True

if not mob_nbr_delimit1 == "-":
    valid = False

if not mob_nbr_delimit2 == "-":
    valid = False

if not mob_nbr_part1.isdigit():
    valid = False

if not mob_nbr_part2.isdigit():
    valid = False

if not mob_nbr_part2.isdigit():
    valid = False

if not mob_nbr_part3.isdigit():
    valid = False

print("Mobile Number and Result is :", mob_nbr, valid)
