from flask import Flask, render_template, request
# from downloader import downloadVideo
import downloader

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/search", methods=['POST'])
def search():
    ytlink = request.form['ytlink']
    downloader.getVideo(ytlink)
    # print("Title: ", downloader.getTitle() )
    # print("Channel: ", downloader.getChannel() )
    # print("Views: ", downloader.getViews() )
    # print("Thumbnail: ", downloader.getThumbnail() )
    vidTitle = downloader.getTitle()
    vChannel = downloader.getChannel()
    vThumbnail = downloader.getThumbnail()
    vViews = downloader.getViews()
    vLength = downloader.getLength()
    return render_template('index.html', title=vidTitle, channel=vChannel, thumbnail=vThumbnail, views=vViews, length=vLength)

@app.route("/download", methods=['POST', 'GET'])
def download():
    downloader.downloadVideo()
    return render_template('index.html')

if __name__ == "__main__":
    app.run()