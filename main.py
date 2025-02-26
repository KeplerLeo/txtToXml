import os
import logging
from tkinter import Tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from xml_generator import gerar_xml  # Import the XML generation function from the new module

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def solicitar_arquivo_txt():
    # Oculta a janela root do Tkinter
    Tk().withdraw()
    
    # Abre a caixa de diálogo para seleção de arquivo
    caminho_txt = askopenfilename(
        title="Selecione o arquivo .txt",
        filetypes=[("Arquivos de texto", "*.txt")]  # Filtra apenas arquivos .txt
    )
    
    if caminho_txt:
        return caminho_txt
    else:
        logging.error("Nenhum arquivo selecionado. O programa será encerrado.")
        exit()

def solicitar_local_para_salvar(nome_sugerido):
    # Oculta a janela root do Tkinter
    Tk().withdraw()
    
    # Abre a caixa de diálogo para salvar o arquivo
    caminho_saida = asksaveasfilename(
        title="Salvar arquivo XML como",
        defaultextension=".xml",
        initialfile=nome_sugerido,
        filetypes=[("Arquivo XML", "*.xml")]  # Filtra apenas arquivos .xml
    )
    
    if caminho_saida:
        return caminho_saida
    else:
        logging.error("Nenhum local de salvamento selecionado. O programa será encerrado.")
        exit()

def processar_linha(linha):
    codigo_conta = linha[:10].strip()
    
    # Extrai o valor da primeira coluna (ignora o sinal)
    saldo = int(linha[14:32].strip() or '0')  # Converte para inteiro

    # Formata o saldo no padrão internacional (99.99)
    saldo_formatado = f"{saldo / 100:.2f}"

    return codigo_conta, saldo_formatado

def main():
    try:
        # Solicita o caminho do arquivo .txt usando uma caixa de diálogo
        caminho_txt = solicitar_arquivo_txt()

        # Lê o conteúdo do arquivo .txt
        with open(caminho_txt, 'r', encoding='utf-8') as arquivo_txt:
            linhas = arquivo_txt.readlines()

        # Sugere o nome do arquivo XML baseado no nome do arquivo .txt
        nome_arquivo_sugerido = os.path.splitext(os.path.basename(caminho_txt))[0] + '.xml'

        # Solicita o local para salvar o arquivo XML
        caminho_saida = solicitar_local_para_salvar(nome_arquivo_sugerido)

        # Gera e salva o XML
        gerar_xml(linhas, caminho_saida)
    except FileNotFoundError:
        logging.error("Arquivo não encontrado.")
    except IOError:
        logging.error("Erro ao ler o arquivo.")
    except Exception as e:
        logging.error(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    main()