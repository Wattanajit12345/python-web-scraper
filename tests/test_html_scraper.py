from src.web_scraper import HtmlScraper


html_body = """
<html>
  <body>
    <p>This is the first paragraph.</p>
    <p>This is the second paragraph.</p>
  </body>
</html>
"""


def test_html_scraper():
    scraper = HtmlScraper(html_body)
    texts = scraper.get_text()
    result_list = ['This is the first paragraph.', 'This is the second paragraph.']
    assert texts == result_list
