from flask import Flask, render_template, request, send_file
from pytubefix import YouTube
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        file_path = stream.download(output_path="downloads")
        return send_file(file_path, as_attachment=True)
    
    # Esto solo se ejecuta si el método es GET
    return render_template('index.html')

if __name__ == '__main__':
    if not os.path.exists('downloads'):
        os.makedirs('downloads')
    # Cambiamos host a '0.0.0.0' para que sea accesible desde otros dispositivos
    app.run(debug=True, host='0.0.0.0', port=5000)