from google_images_search import GoogleImagesSearch

def buscadorIMG():
    gis = GoogleImagesSearch('AIzaSyASyFhCn34Mi3flfSdDvgrKdFwJfqs148g', '84c6f4443008041a5')

    search_params = {
        'q': 'werevertumorro',
        'num': 10,
        'fileType': 'jpg|gif|png',
    }

    gis.search(search_params = search_params, path_to_dir = 'imagenes')
