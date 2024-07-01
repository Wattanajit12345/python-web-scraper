from src.web_scraper.html_handler import HtmlHandler
from src.web_scraper.html_scraper import HtmlScraper
from web_scraper.fetch import TableStatics

if __name__ == '__main__':
    html_handler = HtmlHandler().get_html_by_url(url="https://en.wikipedia.org/wiki/Thailand")
    text = HtmlScraper(html_body=html_handler).get_text()

    table = TableStatics(data=text)
    table.save_to_excel("result.xlsx")

    print(text)
