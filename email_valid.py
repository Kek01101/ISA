# 7/10/2020, Blue, Nicolas Keck, Accepts an array of email addresses and returns array
# with true/false values for email address.
# Minor extension: Also catches some fake emails which weren't caught in the example


def validEmails(list):
    valids = []
    for email in list:
        if "@" in email and "." in email and "@." not in email and ".." not in email:
            count = 0
            for char in email:
                if char == "@":
                    count += 1
                elif char == "." and count == 0:
                    break
            if count == 1:
                valids.append(True)
            else:
                valids.append(False)
        else:
            valids.append(False)
    return valids

test_emails = ["abc@aol.com", "def@.com", "efg@abc", "sk@gmail.com"]
print(validEmails(test_emails))
test_emails_2 = ["a@aol.com", "d@.g.com", "e123g@abc.sg", "sk123@.abcgmail.com"]
print(validEmails(test_emails_2))
my_test = ["@@", "thing@abc..com", "bigG@this.is.a.long.email.com", "this.before@exists.com"]
print(validEmails(my_test))


# This function solves the issue with the intended solution, rather than with Python logic
def validEmailsTwo(emails):
    valids = []
    for email in emails:
        count = 0
        per_count = 0
        lastchar = ""
        for char in email:
            if char == "@":
                if lastchar == ".":
                    break
                else:
                    count += 1
            elif char == ".":
                if count == 0 or lastchar == "." or lastchar == "@":
                    count = 0
                    break
                else:
                    per_count += 1
            lastchar = char
        if count == 1 and per_count >= 1:
            valids.append(True)
        else:
            valids.append(False)
    return valids

print(validEmailsTwo(test_emails))
print(validEmailsTwo(test_emails_2))
print(validEmailsTwo(my_test))