from flask import Flask, render_template, request, redirect
import requests
import urllib.parse

app = Flask(__name__)

# Substitua pela sua chave da API do Giphy
GIPHY_API_KEY = "nMGInRGmrGiN4UHsghe7FPBDQkAdua33"

@app.route('/', methods=['GET', 'POST'])
def index():
    gifs = []
    if request.method == 'POST':
        query = request.form['query']
        url = f'https://api.giphy.com/v1/gifs/search?api_key={GIPHY_API_KEY}&q={urllib.parse.quote(query)}&limit=10&rating=g'
        response = requests.get(url)
        data = response.json()
        gifs = [item['images']['downsized']['url'] for item in data['data']]
    return render_template('index.html', gifs=gifs)

@app.route('/send', methods=['POST'])
def send():
    gif_url = request.form['gif_url']
    phone = request.form['phone']
    whatsapp_url = f"https://web.whatsapp.com/send?phone={phone}&text={urllib.parse.quote(gif_url)}"
    return redirect(whatsapp_url)

if __name__ == '__main__':
    app.run(debug=True)
