import random
import string

def generate_opt_code():
    rand = random.SystemRandom()
    code = rand.choices(string.digits, k=6)
    result = ''.join(code)
    return result

