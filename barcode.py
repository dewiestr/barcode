try:
    from reportlab.graphics.barcode import code39
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.units import mm
    from reportlab.pdfgen import canvas

except Exception as e:
    print("You are missing reportlab library, run \" pip install reportlab\" ")
    raise e

# Script to generate code38 barcodes on a page, change the variables below to adjust accordingly.
fileName = "barcodes.pdf"
numberOnPage=24
firstBarCode=1235073

#HIERONDER KAN JE DE NAAM INVULLEN VAN HET GEGENEREERDE BESTAND
c = canvas.Canvas(fileName, pagesize=A4)

code_list = range(firstBarCode,firstBarCode+numberOnPage)
for i in range(0,len(code_list)):
    code_list[i]=str(code_list[i])


#barWidth IS DE BREEDTE VAN DE KLEINE BAR
barWidth= 0.45*mm
#barHeight IS DE HOOGTE VAN DE BARCODE
barHeight= 11*mm

barcodelen= barWidth*8*len(str(firstbarcode))+25

# x IS DE MARGE LINKS OP DE PAGINA
x = 1 * mm
# y IS DE PAGINA HOOGTE - VERTICALE MARGE - BARCODEHOOGTE ( 297 - 8 - 11 )
y1 = 268 * mm
y=y1
# p1 IS DE POSITIE VAN DE GEPRINTE STRING HORIZONTAAL TOV HOEK BARCODE 
p1 = 35 * mm
# y2 IS DE HOOGTE TUSSEN DE ONDERKANT BARCODE EN ONDERKANT VAN GEPRINTE NUMMERS
y2= 5 * mm
# y3 IS DE HOOGTE TUSSEN DE GEPRINTE NUMMERS EN DE VOLGENDE BARCODE 
y3= 17 * mm

for code in code_list:
    barcode = code39.Extended39(code,barWidth=barWidth,barHeight=barHeight)
    barcode.drawOn(c, x, y)
    x1 = x + p1
    y = y - y2
    c.drawString(x1, y, code)
    x = x
    y = y - y3

    if int(y) <= y3+y2:
        x = x + barcodelen *mm
        y = y1

c.showPage()
c.save()
