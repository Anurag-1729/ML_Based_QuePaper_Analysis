import PyPDF2
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

filename = 'test_paper.pdf'
pdfFileObj = open(filename, 'rb')
reader = PyPDF2.PdfReader(pdfFileObj)
num_pages = len(reader.pages)
count = 0
text = ""
while count < num_pages:
    pageObj = reader.pages[count]
    count += 1
    text += pageObj.extract_text()

#tokens = word_tokenize(text)
punctuations = ('(', ')', ';', ':', '[', ']', ',', 'a', 'and', 'the', '**********',
                'Seat', 'No._','Enrolment', 'No.','GUJARAT', 'TECHNOLOGICAL', 'UNIVERSITY',
                'BE', 'SEMESTER–VII(NEW)', 'EXAMINATION','PM', 'AM' ,'Time', '02:30', 'TO',
                '05:00', 'Total', 'Marks', '70' ,'Instructions','Attempt', 'questions','Make', 'suitable',
                ' assumptions', 'wherever', 'necessary', 'Figures' ,'right', 'indicate', 'full', 'marks',
                'MARKS', '* * * * * * * * * *')
#stop_words = stopwords.words('english')
#keywords = [word for word in tokens if not word in stop_words and not word in punctuations]
#clean_text = ' '.join([word for word in tokens if not word in stop_words and not word in punctuations])
clean_text = ' '.join([word for word in tokens if not word in stop_words and not word in punctuations])

with open("extracted_test_paper1.txt", "w", encoding=' utf-8 ') as f:
    f.write(clean_text)
