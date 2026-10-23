def format_name(first_name, last_name):
    """Format a name to return the title case version of the name."""
    formatted_first_name = first_name.title()
    formatted_last_name = last_name.title()
    return f"{formatted_first_name} {formatted_last_name}"

print(format_name("john", "doe"))

def function_1(text):
    return text.upper()

def function_2(text):
    return text.lower()

output_1 = function_1("hello")

print(output_1)

output_2 = function_2(output_1)
print(output_2)
