'''
Created on Nov 5, 2024

@author: fraidoon
'''
def print_state_details(state_code, state_name):
    # Outputs the state details in the specified format
    print(f"{state_code} is {state_name}'s state code.")

state_code1 = input()
my_state1 = input()
state_code2 = input()
my_state2 = input()

print_state_details(state_code1, my_state1)
print_state_details(state_code2, my_state2)