from selenium import webdriver
from PIL import Image
from io import BytesIO
from flask import Flask, render_template, request
import os
import time


app = Flask(__name__)
path = os.path.dirname(os.path.abspath(__file__))

def get_site(url):

    driver = webdriver.Firefox()
    driver.set_window_position(0, 0)
    driver.set_window_size(1920, 1080)
    driver.get(url)
    time.sleep(2)
    png = driver.get_screenshot_as_png() 
    driver.quit()

    im = Image.open(BytesIO(png))
    im.save(path + '/static/better_website.png') 

    return url
@app.route('/', methods=['GET', 'POST'])
def home():

    if request.method == 'POST':
        url = request.form['content']
        _ = get_site(url)
        return render_template('image.html')

    else:    
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)

