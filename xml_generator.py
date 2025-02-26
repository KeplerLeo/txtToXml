import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def processar_linha(linha):
    """Process a line and extract the account code and formatted balance"""
    codigo_conta = linha[:10].strip()
    saldo = int(linha[14:32].strip() or '0')
    saldo_formatado = f"{saldo / 100:.2f}"
    return codigo_conta, saldo_formatado

def gerar_xml(linhas, caminho_saida):
    """Generate an XML file from a list of lines and save it to the specified path"""
    try:
        cabecalho = linhas[0]
        codigo_documento = cabecalho[3:7]
        cnpj = cabecalho[7:15]
        database = f"{cabecalho[31:35]}-{cabecalho[29:31]}"
        tipo_remessa = cabecalho[35]

        xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<documento codigoDocumento="{codigo_documento}" cnpj="{cnpj}" dataBase="{database}" tipoRemessa="{tipo_remessa}">
    <contas>
"""

        for linha in linhas[1:]:
            linha = linha.strip()
            if not linha or linha.startswith('@'):
                continue

            codigo_conta, saldo_formatado = processar_linha(linha)
            xml += f'        <conta codigoConta="{codigo_conta}" saldo="{saldo_formatado}" />\n'

        xml += """    </contas>
</documento>
"""

        os.makedirs(os.path.dirname(caminho_saida), exist_ok=True)
        with open(caminho_saida, 'w', encoding='utf-8') as arquivo_xml:
            arquivo_xml.write(xml)

        logging.info(f"Arquivo XML salvo com sucesso em: {caminho_saida}")
    except IOError:
        logging.error("Erro ao escrever o arquivo XML.")
    except Exception as e:
        logging.error(f"Ocorreu um erro ao gerar o XML: {e}")