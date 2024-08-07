from bs4 import BeautifulSoup

def getSiteContents(url):
    with open(url) as fp:
        soup = BeautifulSoup(fp)

    soup = BeautifulSoup("<html>data</html>")
