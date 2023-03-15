from PyPDF2 import PdfReader
import re

reader = PdfReader("test_paper.pdf")
#page = reader.pages[0]
#page_content = page.extract_text()
#print(page_content)

page_num = 0
unwanted_txt = ("GUJARAT", "UNIVERSITY")
while page_num < len(reader.pages):
    page = reader.pages[page_num]
    page_content = page.extract_text()
    #print(f"Page {page_num}:")
    #print(page_content)

    #file1 = open('test.txt', "a", encoding=' utf-8 ')
    #final_content = re.sub('[GUJARAT]','x',page_content)
    #file1.write(final_content)

    with open('test.txt','a',encoding=' utf-8 ') as f:
        final_content = page_content.replace   (unwanted_txt,"X")
        f.write(final_content)

    page_num += 1
    #file1.close()

