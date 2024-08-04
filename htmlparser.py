import re

def parse(html_text):
    # Convert <br> to newline
    clean_text = html_text.replace('<br>', '\n')
    # Remove everything inside <>
    clean_text = re.sub(r'<.*?>', '', clean_text)
    return clean_text

# Example usage:
'''
html_code = "<!DOCTYPE html><html><head></head><body>Hello<br>World!</body></html>"
parsed_text = parse_html(html_code)
print(parsed_text)  # Output: "Hello\nWorld!"
'''
