def calculate_gas_needed(distance, efficiency):
    """
    Calculates the gas needed for a given distance based on efficiency.
    
    Args:
        distance (float): The distance to be traveled in miles.
        efficiency (float): The efficiency of the tractor trailer in miles per gallon.
    
    Returns:
        float: The amount of gas needed in gallons.
    """
    gas_needed = distance / efficiency
    return gas_needed

# Get user input
distance = float(input("Enter the distance to be traveled (in miles): "))
efficiency = float(input("Enter the efficiency of the tractor trailer (in miles per gallon): "))

# Calculate gas needed
gas_needed = calculate_gas_needed(distance, efficiency)

# Display the result
print("The tractor trailer will need", gas_needed, "gallons of gas for the trip.")
