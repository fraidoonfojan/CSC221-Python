'''
Created on Oct 9, 2024

@author: fraidoon
'''

'''
Three integer and string pairs are read from input, each pair representing an authentication code sent to an email address. Create a dictionary named one_time_login containing the following key-value pairs:

Key authentication_code1 with the value email_address1
Key authentication_code2 with the value email_address2
Key authentication_code3 with the value email_address3
'''

# Input: Read three authentication codes and email addresses
authentication_code1 = int(input())
email_address1 = input()

authentication_code2 = int(input())
email_address2 = input()

authentication_code3 = int(input())
email_address3 = input()

# Define the dictionary with the authentication codes as keys and the email addresses as values
one_time_login = {
    authentication_code1: email_address1,
    authentication_code2: email_address2,
    authentication_code3: email_address3
}

# Output the values for the respective authentication codes
print(f'{authentication_code1}: {one_time_login[authentication_code1]}')
print(f'{authentication_code2}: {one_time_login[authentication_code2]}')
print(f'{authentication_code3}: {one_time_login[authentication_code3]}')