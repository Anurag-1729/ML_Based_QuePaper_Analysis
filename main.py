from PyPDF2 import PdfReader, PdfWriter

file_path = 'test_paper.pdf'
pdf = PdfReader(file_path)

with open('test.txt','w') as f:
    for page_num in range(pdf.numPages):
        print('Page:{0}'.format(page_num))
        pageObj = pdf.getPage(page_num)

        try:
            txt = pageObj.extractText()
            print(''.center(100, '-'))
        except:
            pass
        else:
            f.write('Page {0}\n'.format(page_num+1))
            f.write(''.center(100,'-'))
            f.write(txt)

        f.close()