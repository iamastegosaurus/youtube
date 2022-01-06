from selenium import webdriver
from PIL import Image
from io import BytesIO
from flask import Flask, render_template, url_for, request
import time

app = Flask(__name__)

def get_site(url):

    driver = webdriver.Firefox()
    driver.set_window_position(0, 0)
    driver.set_window_size(1920, 1080)
    driver.get(url)
    png = driver.get_screenshot_as_png() 
    driver.quit()

    im = Image.open(BytesIO(png))
    im.save('Q:\\thievery\\static\\shot.png') 

    return url

# {{url_for('static', filename='shot.png')}}

@app.route('/', methods=['GET', 'POST'])
def home():

    if request.method == 'POST':
        url = request.form['content']
        print(url)
        moo = get_site(url)
        return render_template('img.html')

    else:    
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
