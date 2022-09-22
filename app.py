from flask import Flask, render_template, request
from bs4 import BeautifulSoup
import time
import undetected_chromedriver


app = Flask(__name__)


@app.route('/', methods=["POST", "GET"])
def login():
    if request.method == 'POST':
        results = []
        for page_num in range(1, 4):
            user_subject = request.form['user_subject']
            user_grade = request.form['user_grade']
            user_question = request.form['user_question']
            driver = undetected_chromedriver.Chrome()
            url = f'https://naurok.com.ua/test/{user_subject}/klas-{user_grade}?storinka={page_num}'
            driver.get(url)
            time.sleep(5)
            results.append(page_num - 1)
            results.extend(scrap_one_page(driver.page_source, int(user_question)))

        return render_template('results.html', content=results)
    else:
        return render_template('index.html')


def scrap_one_page(page_content, number_of_questions):
    soup = BeautifulSoup(page_content, 'html.parser')
    results = soup.find_all("div", class_="file-item test-item")    # collect all div_blocks that contain test info
    links = []
    for block in results:
        if block.text[1:].startswith(str(number_of_questions)):   # startswith from first element because first is \n
            links.append(get_question_links(block))
    return links


def get_question_links(block):
    all_links = block.find_all('a', href=True)
    res_link = None
    for link in all_links:
        if link['href'].startswith('/test/'):    # check that the link is not the profile link
            res_link = 'https://naurok.com.ua' + link['href']   # add matched link to result links list
            break
    return res_link


if __name__ == '__main__':
    app.run(debug=True)
