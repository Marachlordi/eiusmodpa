# Sample list of elements
elements = [1, 2, 2, 3, 4, 4, 5]

# Initialize a variable to store the previous element
prev_element = None

# Iterate through the elements
for element in elements:
    # Compare the current element with the previous one
    if element == prev_element:
        print(f"Duplicate found: {element}")
    # Update the previous element with the current one for the next iteration
    prev_element = element
