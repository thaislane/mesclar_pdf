from PyPDF4 import PdfFileMerger
import os

# inserir caminho de origem dos pdfs que devem estar em uma pasta

pasta = 'C:\\Users\\...\\...\\...'


pdfs = [os.path.join(pasta, nome) for nome in os.listdir(pasta)]

merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(pdf)

# nome do arquivo pdf que será unificado

merger.write('C:\\Users\\...\\...\\"nomeDoArquivo".pdf')
merger.close()
