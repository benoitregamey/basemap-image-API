# basemap-image-API
Get full resolution, best quality basemap as a single image for any AOI and zoom level ! 

This service fetch basemap tiles from Maptiler XYZ service. You need an API key from Maptiler (create an account to get one).

Usage example : http://localhost:5000/get/basemap-image?aoi=2737020,5722885,2742854,5715473&source=https://api.maptiler.com/maps/topo/256&zoomlevel=14&key=your-maptiler-api-key

aoi must be in the following form : "aoi=west,north,east,south" in epsg:3857 (web-mercator)

source must be in the following form : "source=https://api.maptiler.com/maps/{layer-name}/256"

zoomlevel must be an integer between 0 and 20

key is your personal API Key provided by Maptiler

The API returns a basemap.jpg file, the max quality basemap that you required !

If you get the error "Number of tiles to download exeeds 500 !", try to reduce the AOI or the zoomlevel !
