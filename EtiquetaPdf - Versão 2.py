import os
import time
import psutil
import pygetwindow as gw
from PyPDF2 import PdfReader
import subprocess
import msvcrt 

def fechar_leitor_pdf(janelas_pdf):
    for janela in janelas_pdf:
        janela.close()

def imprimir_pdf(caminho_pdf):
    print(f"Tentando imprimir o arquivo: {caminho_pdf}")

    try:
        # Chamar o comando externo para imprimir o PDF
        comando = rf'"C:\Program Files\Adobe\Acrobat DC\Acrobat\Acrobat.exe" /t "{caminho_pdf}"'
        subprocess.Popen(comando, shell=True)

        # Aguardar 3 segundos antes de fechar o leitor de PDF
        time.sleep(3)

        fechar_leitor_pdf(gw.getWindowsWithTitle("Adobe Acrobat Reader"))

    except Exception as e:
        print(f"Erro ao imprimir o PDF: {e}")

if __name__ == "__main__":
    pasta_downloads = "C:/Users/douglas/Downloads"

    try:
        while not msvcrt.kbhit():  # Continue até que uma tecla seja pressionada
            arquivos_downloads = os.listdir(pasta_downloads)
            pdfs_etiqueta = [arquivo for arquivo in arquivos_downloads if arquivo.lower().endswith(".pdf") and "etiqueta" in arquivo.lower()]  #Condição de Nome do arquivo conter etiqueta

            processos_anteriores = set(psutil.process_iter(['pid']))
            for pdf_etiqueta in pdfs_etiqueta:
                caminho_pdf_etiqueta = os.path.join(pasta_downloads, pdf_etiqueta)
                print(f"Novo arquivo PDF de etiqueta encontrado: {caminho_pdf_etiqueta}")

                # Adicione aqui o código para verificar se o arquivo já foi processado antes

                imprimir_pdf(caminho_pdf_etiqueta)

                try:
                    os.remove(caminho_pdf_etiqueta)
                    print(f"Arquivo excluído: {caminho_pdf_etiqueta}")
                except FileNotFoundError:
                    print(f"Arquivo não encontrado: {caminho_pdf_etiqueta}")
                except Exception as e:
                    print(f"Erro ao excluir o arquivo: {e}")

            time.sleep(5)

    except KeyboardInterrupt:
        pass
