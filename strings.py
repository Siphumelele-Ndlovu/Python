#Advanced concepts - strings

message = ' Hello, World! '

print(message.strip())  # Removes leading and trailing whitespace 
print(message.lower())  # Convert all to lowercase
print(message.upper())  # Convert all to uppercase
print(message.replace('World', 'Python'))  # Replace 'World' with 'Python'
print(message.split(','))  # Split the string by comma
print(message.find('World'))  # Find the index of 'World'
print(message.startswith(' Hello'))  # Check if the string starts with ' Hello' 
print(message.endswith('! '))  # Check if the string ends with '! '

