import sys
import requests
from bs4 import BeautifulSoup
from selenium import webdriver


def download_from_group(url):
    # Get HTML
    path = "insert here the path to your browser driver"
    driver = webdriver.Chrome(path)
    driver.get(url)
    if driver.find_element_by_xpath("//button[@class='_54k8 _52jh _56bs _9y0r _56bt']") is not None:
        elem = driver.find_element_by_xpath("//button[@class='_54k8 _52jh _56bs _9y0r _56bt']")
        elem.click()
    elem = driver.find_element_by_xpath("//div[@class='_1o0y']")
    elem.click()
    elem = driver.find_element_by_xpath("//video")
    video_url = elem.get_attribute('src')
    driver.close()
    # Get source Link

    return video_url


def download_from_page(url):
    # Get HTML
    driver = webdriver.Chrome('C:\\Users\\ArcaiC\\Documents\\chromedriver.exe')
    driver.get(url)
    if driver.find_element_by_xpath("//button[@class='_54k8 _52jh _56bs _9y0r _56bt']") is not None:
        elem = driver.find_element_by_xpath("//button[@class='_54k8 _52jh _56bs _9y0r _56bt']")
        elem.click()
    elem = driver.find_element_by_xpath("//div[@class='_1o0y']")
    elem.click()
    elem = driver.find_element_by_xpath("//video")
    video_url = elem.get_attribute('src')
    driver.close()
    # Get source Link

    return video_url

def download_from_watch(url):
    # Get HTML
    rawdata = requests.get(url)
    html = rawdata.content
    soup = BeautifulSoup(html, 'html.parser')

    # Get source Link
    div = soup.find("head").find(property="og:video:url")
    video_url = div['content']
    return video_url


def downloader():

    # Get URL
    url = sys.argv[1]

    # Convert to mobile
    url = url.replace("https://www", "https://m")
    print("URL: " + url)

    video_url = ""

    if url.startswith("https://m.facebook.com/watch/"):
        print("Video from watch")
        video_url = download_from_watch(url)
    elif url.startswith("https://m.facebook.com/groups"):
        print("Video from a group")
        video_url = download_from_group(url)
    else:
        print("Video from a page")
        video_url = download_from_page(url)

    # Download video
    response = requests.get(video_url)
    print("Downloading")
    f = open(str(abs(hash(response.url))) + ".mp4", 'wb')
    for byte in response.iter_content(chunk_size=255):
        if byte:  # filter out keep-alive chunks
            f.write(byte)
    print("Done")

if __name__ == '__main__':
    downloader()

