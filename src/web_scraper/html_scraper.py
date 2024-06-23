from bs4 import BeautifulSoup


class HtmlScraper:

    def __init__(self, html_body: str):
        self.html_body = html_body

    def get_text(self):
        html_body = self.html_body
        soup = BeautifulSoup(html_body, 'html.parser')
        # You should get information by P tag "How get information from P tag by using BeautifulSoup"
        result_text = ""
        return result_text
