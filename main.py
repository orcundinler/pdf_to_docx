from pdf2docx import Converter
import os.path

pathPDF = input("PDF Pile Path(example: Desktop/mypdf.pdf): ")

pdf_file = pathPDF
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
output_docx_path = os.path.join(desktop_path, "convertedPDF.docx")

cv = Converter(pdf_file)
cv.convert(output_docx_path, start=0, end=None)
cv.close()
input("DOCX file saved in Desktop successfully. Press ENTER to exit.")
