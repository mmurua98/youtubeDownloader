from flask import Flask, render_template, request, send_file
# from downloader import downloadVideo
import downloader
import os

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
    global filename
    
    vidTitle = downloader.getTitle()
    vChannel = downloader.getChannel()
    vThumbnail = downloader.getThumbnail()
    vViews = downloader.getViews()
    vLength = downloader.getLength()

    filename =  str(vidTitle) + ".mp4"

    return render_template('index.html', title=vidTitle, channel=vChannel, thumbnail=vThumbnail, views=vViews, length=vLength)

@app.route("/download",  methods=['POST', 'GET'])
def download():
    if request.method == 'POST':
        global path, openFile
        path = downloader.downloadVideo()
        #return render_template('index.html')
        #openFile = open(filename, 'r')
        # return send_file(path, as_attachment=True, mimetype='video/mp4', attachment_filename=os.path.basename(filename))
        return send_file(path, as_attachment=True, attachment_filename=filename)
    
    return render_template('index.html')

@app.after_request
def deleteVideo(response):
    if request.endpoint=="download":
        #os.remove(filename)
        #openFile.close()
        videoName = filename.replace("'",'')
    
        pathDir = os.getcwd()
        pathFile = pathDir + '\\' + videoName
        #print("This is the path file: ", pathFile)

        if os.path.isfile(pathFile):
            # with open(pathFile, 'rb') as file:
            #     file.read()
            #os.remove(pathFile)
            #openFile.close()

            try:
                # with open(pathFile, 'rb') as file:
                #     file.read()
                os.remove(pathFile)
            except OSError as e: # name the Exception `e`
                print ("Failed with:", e.strerror)# look what it says
                print ("Error code:", e.errno )
            
            #print('file exist!!: ', pathFile) 
        # else:
        #     #print("The file does not exist")

        #     try:
        #         print("The file does not exist")
        #     except OSError as e: # name the Exception `e`
        #         print ("Failed with:", e.strerror)# look what it says
        #         print ("Error code:", e.errno )
        #             #print('THIS IS THE PATH: ', os.getcwd())
        #os.remove(path)
        #open(filename, 'r')
        #print(filename)
    return response

if __name__ == "__main__":
    app.run()