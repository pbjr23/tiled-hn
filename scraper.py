from lxml import etree
import requests

URL = 'https://news.ycombinator.com/'

def get_data(url=URL):
    """Gets all relevant data from input url"""

    data = []
    raw = requests.get(url).text.encode('utf-8')

    # Sets up parser
    utf_parser = etree.HTMLParser(encoding="utf-8")
    tree = etree.HTML(raw, parser=utf_parser)
    base = '//*[@id="hnmain"]/tr[3]/td/table/tr['

    # Determines which page we are scraping and sets up variables for xpath accordingly
    x = 1
    newest = 0
    if 'jobs' in url or 'show' in url:
        x = 4
    if 'newest' in url:
        newest = 2

    # Finds the number of items in the page
    number_values = len(tree.xpath("//tr[@class='athing']"))

    for i in range(number_values):
        title = tree.xpath(base + '{}]/td[@class="title"]/a'.format(x+3*i))[0].text

        try:
            comments = tree.xpath(base + '{}]/td[2]/a[{}]'.format(x+3*i+1, 2+newest))[0].text.split(' ')[0]
            if comments == 'discuss':
                comments = None
        except IndexError:
            comments = None

        try:
            comments_url = URL + tree.xpath(base + '{}]/td[2]/a[2]'.format(x+3*i+1))[0].attrib['href']
        except IndexError:
            comments_url = None

        try:
            points = tree.xpath(base + '{}]/td[2]/span[@class="score"]'.format(x+3*i+1))[0].text.split(' ')[0]
        except IndexError, AttributeError:
            points = None

        try:
            author = tree.xpath(base + '{}]/td[2]/a[1]'.format(x+3*i+1))[0].text.split(' ')[0]
        except IndexError:
            author = None

        try:
            mini_url = tree.xpath(base + '{}]/td[3]/span[2]/a/span'.format(x+3*i))[0].text
        except IndexError:
            mini_url = None

        # For jobs page and elements with only age attribute
        if 'jobs' in url or (author == None and points == None):
            try:
                age = tree.xpath(base + '{}]/td[2]/span/a'.format(x+3*i+1))[0].text.strip().replace('minutes', 'min').replace(' ago', '')
            except IndexError:
                age = None
        elif newest:
            try:
                age = tree.xpath(base + '{}]/td[2]/span[2]/a'.format(x+3*i+1))[0].text.strip().replace('minutes', 'min').replace(' ago', '')
            except IndexError:
                age = None
        else:
            try:
                age = tree.xpath(base + '{}]/td[2]/span[@class="age"]/a'.format(x+3*i+1))[0].text.strip().replace('minutes', 'min').replace(' ago', '')
            except IndexError:
                age = None

        try:
            title_url = tree.xpath(base + '{}]/td[3]/a'.format(x+3*i))[0].attrib['href']
            if title_url[:7] == "item?id":
                title_url = URL + title_url
        except IndexError:
            title_url = None

        current = (title, mini_url, title_url, comments_url, author, age, points, comments)
        data.append(current)

    # Gets the link to the next page if applicable
    try:
        next = tree.xpath(base + '{}]/td[2]/a'.format(91+x))[0].attrib['href'].replace('?', ':')
    except IndexError:
        next = False

    return data, next
