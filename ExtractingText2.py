from PyPDF2 import PdfReader
import csv

reader = PdfReader("test_paper2.pdf")
page_num = 0

with open('unwanted_txt.csv', newline='') as f:
    unwanted_txt_csv = csv.reader(f)
    unwanted_txt = [row[0] for row in unwanted_txt_csv]


while page_num < len(reader.pages):
    page = reader.pages[page_num]
    page_content = page.extract_text()

    with open('test2.txt','a',encoding=' utf-8 ') as f:
        final_content = page_content
        for txt in unwanted_txt :
            final_content = final_content.replace(txt,"%")
        f.write(final_content)

    page_num += 1