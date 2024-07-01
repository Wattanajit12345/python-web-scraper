import requests


class HtmlHandler:

    def get_html_by_url(self, url):
        # Get the HTML content of the URL
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            return response.text
        else:
            return f"Error: Unable to fetch the URL. Status code: {response.status_code}"

handler = HtmlHandler()
html_content = handler.get_html_by_url("https://blogs.ancientfaith.com/wholecounsel/author/frstevedeyoung/")
print(html_content)
