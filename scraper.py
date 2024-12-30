import requests
from bs4 import BeautifulSoup
from weasyprint import HTML

# Extract the content from a single part
def extract_part_content(url):
    try:
        # Get the webpage
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # Remove all ul, img, and a tags from the html body
        for tag in soup.find_all(['ul', 'img', 'a']):
            tag.decompose()

        # Add in the letter coloring
        for u in soup.find_all('u'):
            u['style'] = 'color: red;'
        for b in soup.find_all('b'):
            b['style'] = 'color: green;'

        # Add the heading color
        for h in soup.find_all(class_='ghatta'):
            h['style'] = 'color: green;'

        # Extract the relevant content
        parts = soup.find_all(class_=['pitem', 'skanda'])

        # Remove irrelevant html attributes
        for tag in soup.find_all(True):
            attrs_to_remove = [attr for attr in tag.attrs if attr != 'style']
            for attr in attrs_to_remove:
                del tag.attrs[attr]

        # Return the parts
        return [str(part) for part in parts]
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return []

# Save all parts to a single file
def save_to_file(filename, contents):
    try:
        with open(filename, 'a', encoding='utf-8') as f:
            for i, content in enumerate(contents, start=1):
                f.write(content + '\n\n\n')
        print(f"Saved all parts to {filename}")
    except IOError as e:
        print(f"Error writing to file: {e}")

# Input variables
skanda = 12
part_count = 13
base_url = f"https://telugubhagavatam.org/?tebha&Skanda={skanda}&Ghatta="
output_file = "html/chapter12.html"
pdf_file = "pdf/chapter12.pdf"

# Write the initial html output
with open(output_file, 'w', encoding='utf-8') as f:
    f.write('<!DOCTYPE html>\n<html lang="te">\n')
    f.write(f'<head>\n\t<meta charset="utf8">\n\t<title>Chapter {skanda}</title>\n</head>\n')
    f.write('<body>\n\n')

# Scrape each part
all_part_contents = []
for page_number in range(1, part_count + 1):
    url = f"{base_url}{page_number}"
    print(f"Scraping {url}...")
    parts = extract_part_content(url)
    all_part_contents.extend(parts)

# Save the combined contents of all parts as an html file
save_to_file(output_file, all_part_contents)

# Finish writing the html file and write to pdf
with open(output_file, 'a+', encoding='utf-8') as f:
    f.write('</body>\n</html>\n')
    f.seek(0)
    HTML(string=f.read()).write_pdf(pdf_file)
    print(f"PDF saved as {pdf_file}")
