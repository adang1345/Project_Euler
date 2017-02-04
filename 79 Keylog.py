"""A common security method used for online banking is to ask the user for three random characters from a passcode. For
example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be:
317.

The text file, keylog.txt, contains fifty successful login attempts.

Given that the three characters are always asked for in order, analyse the file so as to determine the shortest possible
secret passcode of unknown length."""

def is_passcode(f):
    """Return true if int f is a possible password given the login attempts."""
    for login in logins:
        g = str(f)
        index1 = g.find(login[0])
        if index1 == -1:
            return False
        g = g[index1 + 1:]
        index2 = g.find(login[1])
        if index2 == -1:
            return False
        g = g[index2 + 1:]
        index3 = g.find(login[2])
        if index3 == -1:
            return False
    return True

# read file and put successful logins into a list
keylog_file = open("79 Keylog.txt")
logins = [line.strip() for line in keylog_file]
keylog_file.close()

potential_passcode = 73162890
while not is_passcode(potential_passcode):
    potential_passcode += 1

print(potential_passcode)
