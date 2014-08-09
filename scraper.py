from lxml import etree
import requests

URL = 'https://news.ycombinator.com/'

def get_data(url):
    """Gets all relevant data from input url"""

    data = []
    raw = requests.get(url).text.encode('utf-8')

    # Sets up parser
    utf_parser = etree.HTMLParser(encoding="utf-8")
    tree = etree.HTML(raw, parser=utf_parser)
    base = '/html/body/center/table/tr[3]/td/table/tr['

    # Determines which page we are scraping and sets up variables for xpath accordingly
    x = 1
    if url == 'https://news.ycombinator.com/jobs':
        x = 3
    if url == 'https://news.ycombinator.com/show':
        x = 4

    # Finds the number of items in the page
    number_values = len(tree.xpath("//td[@valign='top']"))

    for i in range(number_values):
        title = tree.xpath(base + str(x + 3*i) + ']/td[3]/a')[0].text

        try:
            comments = tree.xpath(base + str(x + 1 + 3*i) + ']/td[2]/a[2]')[0].text.split(' ')[0]
            if comments == 'discuss':
                comments = None
        except IndexError:
            comments = None

        try:
            comments_url = URL + tree.xpath(base + str(x + 1 + 3*i) + ']/td[2]/a[2]')[0].attrib['href']
        except IndexError:
            comments_url = None

        try:
            points = tree.xpath(base + str(x + 1 + 3*i) + ']/td[2]/span')[0].text.split(' ')[0]
        except IndexError:
            points = None

        try:
            author = tree.xpath(base + str(x + 1 + 3*i) + ']/td[2]/a[1]')[0].text
        except IndexError:
            author = None

        try:
            mini_url = tree.xpath(base + str(x + 3*i) + ']/td[3]/span')[0].text.strip()
        except IndexError:
            mini_url = None

        # For jobs page and elements with only age attribute
        if x == 3 or (author == None and points == None):
            try:
                age = tree.xpath(base + str(x + 1 + 3*i) + ']/td[2]')[0].text.replace('minutes', 'min')
            except IndexError:
                age = None
        else:
            try:
                age = tree.xpath(base + str(x + 1 + 3*i) + ']/td[2]/a[1]')[0].tail[1:-4].replace(' ago', '')
            except IndexError:
                age = None

        try:
            title_url = tree.xpath(base + str(x + 3*i) + ']/td[3]/a')[0].attrib['href']
            if title_url[:7] == "item?id":
                title_url = URL + title_url
        except IndexError:
            title_url = None

        current = (title, mini_url, title_url, comments_url, author, age, points, comments)
        data.append(current)

    # Gets the link to the next page if applicable
    try:
        next = tree.xpath(base + str(91 + x) + ']/td[2]/a')[0].attrib['href'].replace('?', ':')
    except IndexError:
        next = False

    return data, next
