import os
import time
from flask import Flask, render_template, redirect, abort, request, send_from_directory
from pytube import YouTube

app = Flask("DownTube by Dormaly")

_TEMP_SAVE_PATH = os.path.join(app.static_folder, "public")

@app.route("/", methods=["GET", "POST"])
def homePage():
    if request.method == "POST":
        _VIDEO_LINK = request.form.get("video_link")
        try:
            yt = YouTube(_VIDEO_LINK)
        except:
            return abort(400)
        video = yt.streams.filter(only_audio=True).first()

        out_file = video.download(output_path=_TEMP_SAVE_PATH)
        
        file_number = str(len(os.listdir(_TEMP_SAVE_PATH)))

        new_file = _TEMP_SAVE_PATH + "/" + file_number + ".mp3"
        
        os.rename(out_file, new_file)
        
        current_time = time.time()

        for i in os.listdir(_TEMP_SAVE_PATH):
            file_location = os.path.join(_TEMP_SAVE_PATH, i)
            file_time = os.stat(file_location).st_mtime
            if file_time < current_time - 300:
                os.remove(file_location)

        return redirect(f"/download/{file_number+'.mp3'}")
    return render_template("./index.html")

@app.route('/download/<filename>', methods=['GET', 'POST'])
def download(filename):
    return send_from_directory(_TEMP_SAVE_PATH, filename)

#implement file downloader page with options button in the next update

if __name__ == "__main__":
    app.run(debug=True)
