import requests


class HtmlHandler:

    def get_html_by_url(self, url):
        # Get the HTML content of the URL
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            return response.text
        else:
            return ""
