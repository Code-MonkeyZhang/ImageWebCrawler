from bs4 import BeautifulSoup


def get_test():
    with open(
            '/Users/zhangyufeng/one/OneDrive - The Pennsylvania State University/WorkPlace/PyProject/savetextDemo/Crawler/test_page.html',
            'r') as f:
        test_html = f.read()
    return test_html


html_doc = get_test()
soup = BeautifulSoup(html_doc, 'html.parser')
for myimg in soup.find_all('a', class_='a'):
    img_src = myimg.find('img').get('src')
