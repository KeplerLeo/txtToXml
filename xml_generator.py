import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def gerar_xml(linhas, caminho_saida):
    try:
        cabecalho = linhas[0]
        
        # Extrai o código do documento (4 dígitos após "A1")
        codigo_documento = cabecalho[3:7]
        
        # Extrai o CNPJ (restante da sequência após os 4 dígitos do código do documento)
        cnpj = cabecalho[7:15]
        
        # Extrai a data-base e o tipo de remessa
        database = f"{cabecalho[31:35]}-{cabecalho[29:31]}"
        tipo_remessa = cabecalho[35]

        xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
        xml += f'<documento codigoDocumento="{codigo_documento}" cnpj="{cnpj}" dataBase="{database}" tipoRemessa="{tipo_remessa}">\n'
        xml += '    <contas>\n'

        # Processa as linhas
        for linha in linhas[1:]:
            linha = linha.strip()
            if not linha or linha.startswith('@'):
                continue

            codigo_conta, saldo_formatado = processar_linha(linha)
            xml += f'        <conta codigoConta="{codigo_conta}" saldo="{saldo_formatado}" />\n'

        xml += '    </contas>\n'
        xml += '</documento>'

        # Salva o XML na pasta script/xmls
        os.makedirs(os.path.dirname(caminho_saida), exist_ok=True)
        with open(caminho_saida, 'w', encoding='utf-8') as arquivo_xml:
            arquivo_xml.write(xml)

        logging.info(f"Arquivo XML salvo com sucesso em: {caminho_saida}")
    except IOError:
        logging.error("Erro ao escrever o arquivo XML.")
    except Exception as e:
        logging.error(f"Ocorreu um erro ao gerar o XML: {e}")

def processar_linha(linha):
    codigo_conta = linha[:10].strip()
    
    # Extrai o valor da primeira coluna (ignora o sinal)
    saldo = int(linha[14:32].strip() or '0')  # Converte para inteiro

    # Formata o saldo no padrão internacional (99.99)
    saldo_formatado = f"{saldo / 100:.2f}"

    return codigo_conta, saldo_formatado
