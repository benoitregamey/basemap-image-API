from BasemapExtractor import BasemapExtractor
from flask import Flask, jsonify, request, make_response
import os

app = Flask(__name__)

@app.route("/get/basemap-image")
def get_basemap():

    aoi = request.args.get("aoi")
    source = request.args.get("source")
    key = request.args.get("key")
    ext = request.args.get("ext")
    zoomlevel = request.args.get("zoomlevel")
    
    perimeter = tuple(map(int, aoi.split(',')))
    end_url = f'@2x.{ext}?key={key}'

    basemap = BasemapExtractor(perimeter, int(zoomlevel), source, end_url)
    
    if basemap.download_tiles() == False:
        return jsonify(Error="Number of tiles to download exeeds 500 !")
    
    basemap.mosaic_tiles()

    with open(os.path.dirname(__file__) + os.sep + "temp/Mosaic.jpg", "rb") as image:

        response = make_response(image.read())
        response.headers.set('Content-Type', 'image/jpg')
        response.headers.set('Content-Disposition', 'attachment', filename='basemap.jpg')

        for file in os.listdir(os.path.dirname(__file__) + os.sep + "temp"):
            os.remove(os.path.join(os.path.dirname(__file__) + os.sep + "temp", file))

        return response

if __name__ == '__main__':
    app.run(debug=True, threaded=True)
