# Module Imports
import json, random, time, re

# Variable Assignment
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'   
names = json.loads(open('Z:\coding\Python\Generating emails\mes.json').read())
email_domain_list = json.loads(open('Z:\coding\Python\Generating emails\domain.json').read())
email = 'example@email.com'
iterations = 1000

# FUNCTIONS 
def check(email: str) -> bool:   
    # Takes an email string and checks against local regex. Returns True if conforms. 
    if(re.search(regex,email)):   
        return True
    else: 
        return False

def genmail() -> str:
    #Takes a JSON of first names, adds a random int and a domain. Returns a random email (str)
    name = random.choice(names)
    name_extra = str(random.randint(1,9))
    email_domain = (random.choice(email_domain_list))
    email = (name.lower() + name_extra + email_domain)
    return email

# Runner of the code (Main Boi)
def printmail(iterations: int) -> None:
    # Prints random emails 1000 times. Returns None.
    for i in range(iterations):
        time.sleep(0.001)
        new_email = genmail()
        if check(new_email):
            print(new_email)
        else:
            continue
    return new_email
printmail(iterations)
 