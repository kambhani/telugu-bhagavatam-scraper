from bs4 import BeautifulSoup

# HTML files to merge
html_files = [
    'html/chapter1.html',
    'html/chapter2.html',
    'html/chapter3.html',
    'html/chapter4.html',
    'html/chapter5-1.html',
    'html/chapter5-2.html',
    'html/chapter6.html',
    'html/chapter7.html',
    'html/chapter8.html',
    'html/chapter9.html',
    'html/chapter10-1.html',
    'html/chapter10-2.html',
    'html/chapter11.html',
    'html/chapter12.html'
]

# Variable to hold the combined body contents
combined_body = ""

# Loop through each HTML file
for file_name in html_files:
    with open(file_name, 'r', encoding='utf-8') as f:
        # Parse the HTML content
        soup = BeautifulSoup(f, 'html.parser')

        # Find the body tag and extract its content
        body_content = soup.find('body')

        # Add the body content to the combined_body
        if body_content:
            combined_body += str(body_content)

# Write the combined content into a new HTML file
with open('bhagavatam.html', 'w', encoding='utf-8') as f:
    f.write('<!DOCTYPE html>\n<html lang="te">\n')
    f.write(f'<head>\n\t<meta charset="utf8">\n\t<title>Bhagavatam</title>\n</head>\n')
    f.write('<body>\n\n')
    f.write(combined_body)
    f.write('</body>\n</html>\n')

print("HTML bodies have been combined successfully!")