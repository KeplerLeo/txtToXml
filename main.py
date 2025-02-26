import os
import logging
from tkinter import Tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from xml_generator import gerar_xml

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def solicitar_arquivo_txt():
    """Opens a file dialog for selecting a .txt file"""
    Tk().withdraw()
    return askopenfilename(title="Selecione o arquivo .txt", filetypes=[("Arquivos de texto", "*.txt")])

def solicitar_local_para_salvar(nome_sugerido):
    """Opens a file dialog for saving an XML file"""
    Tk().withdraw()
    return asksaveasfilename(title="Salvar arquivo XML como", defaultextension=".xml", initialfile=nome_sugerido, filetypes=[("Arquivo XML", "*.xml")])

def main():
    try:
        caminho_txt = solicitar_arquivo_txt()
        if not caminho_txt:
            logging.error("Nenhum arquivo selecionado. O programa será encerrado.")
            exit()

        with open(caminho_txt, 'r', encoding='utf-8') as arquivo_txt:
            linhas = arquivo_txt.readlines()

        nome_arquivo_sugerido = os.path.splitext(os.path.basename(caminho_txt))[0] + '.xml'
        caminho_saida = solicitar_local_para_salvar(nome_arquivo_sugerido)

        if not caminho_saida:
            logging.error("Nenhum local de salvamento selecionado. O programa será encerrado.")
            exit()

        gerar_xml(linhas, caminho_saida)
    except FileNotFoundError:
        logging.error("Arquivo não encontrado.")
    except IOError:
        logging.error("Erro ao ler o arquivo.")
    except Exception as e:
        logging.error(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    main()