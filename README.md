# Conversor de Arquivos TXT para XML

Este projeto consiste em um script Python que converte arquivos de texto (.txt) estruturados em um formato específico para arquivos XML. O script foi desenvolvido para atender a necessidades de processamento de dados financeiros, onde os arquivos de texto contêm informações como códigos de contas, saldos e outros detalhes relevantes.

## Funcionalidades

- **Leitura de Arquivos TXT**: O script lê arquivos de texto com um layout pré-definido.
- **Processamento de Dados**: Extrai informações como código do documento, CNPJ, data-base, tipo de remessa e saldos.
- **Geração de XML**: Converte os dados processados em um arquivo XML estruturado.
- **Interface Amigável**: Utiliza uma caixa de diálogo para seleção do arquivo de entrada e para o salvamento do arquivo de saída.

## Como Usar

1. **Executável**: Baixe o executável mais recente na seção [Releases](https://github.com/KeplerLeo/txtToXml/releases).
2. Execute o arquivo `.exe`.
3. Selecione o arquivo `.txt` desejado.
4. Selecione onde o arquivo XML será salvo.

## Requisitos

- **Executável**: Nenhum requisito adicional, basta baixar e executar.
- **Desenvolvimento**: Python 3.x e a biblioteca `tkinter` (já incluída no Python padrão).
- 
