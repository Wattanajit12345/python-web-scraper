from bs4 import BeautifulSoup

class HtmlScraper:

    def __init__(self, html_body: str):
        self.html_body = html_body

    def get_text(self):
        html_body = self.html_body
        soup = BeautifulSoup(html_body, 'html.parser')
        p_tags = soup.find_all('p')
        p_texts = [p.get_text() for p in p_tags]
        return p_texts
html_body = """
<html>
  <body>
    <p>This is the first paragraph.</p>
    <p>This is the second paragraph.</p>
  </body>
</html>
"""

scraper = HtmlScraper(html_body)
texts = scraper.get_text()
print(texts)





