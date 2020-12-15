# advent of code 2020
# day 4
# count how many passports are valid


# a class to hold data input for each field in the passport
class document:
    def __init__(self, byr=0, iyr=0, eyr=0, hgt='', hcl='', ecl='', pid=0, valid=False):
        self.byr = byr
        self.iyr = iyr
        self.eyr = eyr
        self.hgt = hgt
        self.hcl = hcl
        self.ecl = ecl
        self.pid = pid
        self.valid = valid

# just read it in
def readin():
    passports = []
    passport = ""
    count = 0

    with open('da4.txt', 'r') as f:
        Lines = f.readlines()
        # read in all the lines, then go through them
        # this takes data from multiple lines and combines to a single line
        for line in Lines:
            # newline separates each passport
            if line != "\n":
                passport += " "
                passport += line.strip()
            else:
                # add to the list of passports
                passports.append(passport)
                passport = ""
            count += 1
        # one more append to catch the last entry not appended in loop above
        passports.append(passport)
        print(count)

    if f.closed:
        return passports
    else:
        print("error closing file")


# print all the passports in the list
def printPassports(passports):
    i = 1
    for passport in passports:
        print(i, ". ", passport)
        i += 1


# is a passport entry valid? Must have each of the prefixes in fields
def isValid(passport):
    fields = ["byr:", "iyr:", "eyr:", "hgt:", "hcl:", "ecl:", "pid:"]
    valid = True
    for field in fields:
        if field not in passport:
            valid = False
    return valid


# part 1 asks to check the number of passports that have each of the prefixes
def part1(passports):
    count = 0
    for passport in passports:
        if isValid(passport):
            count += 1
    return count


# enter a string representing a passport entry
# removes the prefix and stores into class instance
def enterDataToDoc(parsedPassport):
    a = document()
    for item in parsedPassport:
        if "byr:" in item:
            a.byr = int(item.removeprefix("byr:"))
        elif "iyr:" in item:
            a.iyr = int(item.removeprefix("iyr:"))
        elif "eyr:" in item:
            a.eyr = int(item.removeprefix("eyr:"))
        elif "hgt:" in item:
            a.hgt = item.removeprefix("hgt:")
        elif "hcl:" in item:
            a.hcl = item.removeprefix("hcl:")
        elif "ecl:" in item:
            a.ecl = item.removeprefix("ecl:")
        elif "pid:" in item:
            a.pid = item.removeprefix("pid:")
    return a


# ok, is the data in a document class instance *valid*
def checkData(a):
    a.valid = True
    if a.byr > 2002 or a.byr < 1920:
        a.valid = False
    if a.iyr < 2010 or a.iyr > 2020:
        a.valid = False
    if a.eyr < 2020 or a.eyr > 2030:
        a.valid = False
    if "cm" in a.hgt:
        cm = int(a.hgt.removesuffix("cm"))
        if cm < 150 or cm > 193:
            a.valid = False
    elif "in" in a.hgt:
        inches = int(a.hgt.removesuffix("in"))
        if inches < 59 or inches > 76:
            a.valid = False
    else:
        a.valid = False
    # a # followed by exactly six characters 0-9 or a-f
    if a.hcl.find("#") != 0:
        a.valid = False
    if len(a.hcl) == 7:
        for i in range(1,6):
            if not a.hcl[i].isdigit() and (a.hcl[i] < 'a' or a.hcl[i] > 'f'):
                a.valid = False
    else:
        a.valid = False
    if not(a.ecl == "amb" or a.ecl == "blu" or a.ecl == "brn" or a.ecl == "gry" or a.ecl == "grn" or a.ecl == "hzl" or a.ecl == "oth"):
        a.valid = False
    if len(a.pid) != 9 or a.pid.isdigit() is False:
        a.valid = False
    return a.valid

# part 2! starts with a list of strings, one for each passport
# breaks strings into tuples, one element for each field: eyc,hgt,etc
# enters data into a doc class instance, checks if data is valid, counts
def part2(passports):
    count = 0
    pstuples = []
    psobjects = []

    for passport in passports:
        if isValid(passport):
            # adds to a list of tuples the line split at spaces into strings
            # one string for each entry field, ex) "eyc:brn"
            pstuples.append(passport.split(' '))
    for pst in pstuples:
        psobj = enterDataToDoc(pst)
        if checkData(psobj) is True:
            psobjects.append(psobj)
            count += 1
    return count







passports = readin()
#printPassports(passports)
#print(part1(passports))
print(part2(passports))
