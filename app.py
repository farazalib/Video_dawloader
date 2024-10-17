from flask import Flask, render_template, request, flash, redirect, url_for
from downloader import VideoDownloader


app = Flask(__name__)
app.secret_key = 'your_secret_key'
downloader = VideoDownloader()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        links = [url.strip() for url in url.split('\n') if url.strip()]
        summary_message = downloader.download_videos(links)
        flash(summary_message)
        return redirect(url_for('index'))
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)