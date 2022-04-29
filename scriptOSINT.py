from requests import NullHandler
from requests.models import default_hooks
import urlResearcher
import txtResearcher
import webScraping
import imagesSearch
from openpyxl import Workbook
from openpyxl.drawing.image import Image

if __name__ == "__main__":
    imagesSearch.buscadorIMG ()
    urlResearcher.buscadorURL () 
    txtResearcher.buscadorTXT ()

    b = open("results.txt", "r")
    for linea in b:
        canales = webScraping.buscadorInfo(linea)
        results = open("canales.txt", "a")
        if canales != []:
            results.write(str(canales))
        results.close

        fechas = webScraping.buscadorInfo2(linea)
        fe_chas = open("fechas.txt", "a")
        if fechas != []:
            fe_chas.write(str(fechas))
        fe_chas.close

        redesSociales = webScraping.buscadorInfo3(linea)
        re_socia = open("redesSociales.txt", "a")
        if redesSociales != []:
            re_socia.write(str(redesSociales))
        re_socia.close

        libro = Workbook()
        hoja = libro.active

        re_socia = open("redesSociales.txt" ,"r")
        for linea in re_socia:
            hoja["A1"]= linea 
        re_socia.close

        fe_chas =  open("fechas.txt","r" )
        for linea in fe_chas: 
            hoja["A2"] = linea
        fe_chas.close

        results = open("canales.txt", "r")
        for linea in results:
            hoja["A3"] = linea
        results.close

        img1 = Image('imagenes/CL_0OZeWUAEW923.jpg')
        img2 = Image('imagenes/Werevertumorro-trollea-Nico-Castillo-instagram-780x470.jpg')
        img3 = Image('imagenes/yeah_im_angel__si_soy_un_angel__werevertumorro__by_amorsito13_db8d7wo-350t.jpg')

        hoja.add_image(img1, 'O7')
        hoja.add_image(img2, 'A7')
        hoja.add_image(img3, 'A32')

        libro.save('informacion.xlsx')