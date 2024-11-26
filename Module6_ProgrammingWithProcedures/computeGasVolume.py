'''
Created on Nov 6, 2024

@author: fraidoon
'''
'''
Define a function compute_gas_volume that returns the volume of a gas given parameters pressure, temperature, and moles. Use the gas equation PV = nRT, where P is pressure in Pascals, V is volume in cubic meters, n is number of moles, R is the gas constant 8.3144621 ( J / (mol*K)), and T is temperature in Kelvin.

Sample output with inputs: 100.0 1.0 273.0
Gas volume: 22.698481533 m^3

'''

def compute_gas_volume(pressure, temperature, moles):
    # Gas constant in J/(mol*K)
    gas_const = 8.3144621
    # Calculate volume using the ideal gas law: V = nRT / P
    volume = (moles * gas_const * temperature) / pressure
    return volume

# Read inputs
gas_pressure = float(input())
gas_moles = float(input())
gas_temperature = float(input())

# Calculate gas volume
gas_volume = compute_gas_volume(gas_pressure, gas_temperature, gas_moles)
print(f'Gas volume: {gas_volume} m^3')