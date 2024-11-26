'''
Created on Nov 19, 2024

@author: fraidoon
'''
'''
List pressure_samples contains integers read from input, representing 
data samples from an experiment. Initialize variable all_passed with True. 
Then, for each element at an odd-numbered index of pressure_samples:

Output 'Sample at index ', followed by the element's index, ' is ', and 
the element's value.
If the element's value is less than or equal to 45, then assign variable 
all_passed with False.

'''
# Read input and split input into tokens
tokens = input().split()

pressure_samples = []
for token in tokens:
    pressure_samples.append(int(token))

print(f'All data: {pressure_samples}')

# Initialize variable all_passed to True
all_passed = True

# Iterate through odd-numbered indices in pressure_samples
for index in range(1, len(pressure_samples), 2):  # Odd indices
    value = pressure_samples[index]
    print(f'Sample at index {index} is {value}')
    
    # Check if the value is less than or equal to 45
    if value <= 45:
        all_passed = False

# Check if all_passed is still True or has been set to False
if all_passed:
    print('All integers at odd indices are greater than 45.')
else:
    print('At least one integer at an odd index is less than or equal to 45.')