import requests
import hashlib
import sys

input_args = sys.argv[1:]

#Get password information from PWNED API giving the first 5 characters of the password's hashcode (SHA-1)
def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/'+ query_char
    res = requests.get(url)

    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code} check API')

    return res

#Return number of leaks given a hashed password
def get_leaks_count(hashes, hash_to_check):
    hashes = (h.split(':') for h in hashes.text.splitlines())

    for h,count in hashes:
        if(h == hash_to_check):
            return count 
    return 0

#Check how many time a password has been leaked
def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first_5, tail = sha1password[:5], sha1password[5:]
    res = request_api_data(first_5)
    return get_leaks_count(res, tail)

def main(passwords):
    for password in passwords:
        count = pwned_api_check(password)
        print(f'{password} has been leaked {count} times')


if __name__=='__main__':
    main(input_args)