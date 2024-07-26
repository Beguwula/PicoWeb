import re

def clean_html(html_text):
    # Convert <br> to newline
    clean_text = html_text.replace('<br>', '\n')
    # Remove everything inside <>
    clean_text = re.sub(r'<.*?>', '', clean_text)
    return clean_text

# Example usage:
html_code = "<!DOCTYPE html><html><head></head><body>Hello<br>World!</body></html>"
cleaned_text = clean_html(html_code)
print(cleaned_text)  # Output: "Hello\nWorld!"

