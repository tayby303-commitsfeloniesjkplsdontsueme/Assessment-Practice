# Example list
items = ["apple", "banana", "cherry", "date"]

# Example variable that changes over time
variable_values = ["apple", "apple", "banana", "banana", "date", "date"]

# Track the current index in the list
current_index = 0

for var in variable_values:
    # If the variable matches the current item, move to the next
    if var == items[current_index]:
        current_index += 1
        # Wrap around if we reach the end of the list
        if current_index >= len(items):
            current_index = 0
    
    print(f"Variable: {var} -> Current item: {items[current_index]}")
