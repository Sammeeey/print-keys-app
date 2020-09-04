# print_keys.py - get keys from project directory and print them

import time
import my_keys

key1 = my_keys.key1
key2 = my_keys.key2

while True:
    print('Your first key: ' + key1)
    print('Your second key: ' + key2)
    print('waiting 5 seconds...', end='\n\n')
    time.sleep(5)
