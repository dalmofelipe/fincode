import re

import pandas as pd

from fincode.utils import RGX_PARSER_DADOS_EMPRESAS


def normalize_cvm_code(cvm_code:int):
    """ 
    Padroniza formato do código CVM para o dicionario de consulta no RAD 

    Deve conter 7 caracteres, sendo que primeiro o simbolo deve ser uma virgula. 

    Deve-se completar com zeros a esquerda, caso o código CVM com menos de 6 digitos 
    """
    code_txt = str(cvm_code)

    while len(code_txt) < 6:
        code_txt = '0' + code_txt

    code_txt = ',' + code_txt
    return code_txt



def parser_data_companies(data_txt:str):
    """
    O resultado da regex retorna um dataframe com os dados validados pela regex. 
    Esta lista sempre deve conter uma quantidade de itens multiplo de 5. 
    A cada 5 itens equivalem a um documento.

    Os dados estão na ordem:
    - Nome da empresa
    - Data de Referencia
    - Date de Entrega
    - Numero Sequencial do Documento. Formato dd/MM/yyyy
    - Tipo de Empresa
    """
    regex = re.compile(RGX_PARSER_DADOS_EMPRESAS)
    result = regex.findall(data_txt)

    # a busca deve retornar quantidade de itens multiplos de 5
    if len(result) % 5 != 0: return {
        "msg": "erro ao pesquisar documentos",
        "erro": "dados insulficiente para processar documentos",
        "func": "parser_data_companies"
    }
    documents_list = []
    while len(result) > 0:
        # a cada iteração, os 5 primeiros dados são removidos da lista e agrupados
        # em um dicionário, representando um documento
        doc_data = result[:5]
        del result[:5]
        documents_list.append({
            "company": doc_data[0][2:len(doc_data[0]) -5],
            "dt_referencia": doc_data[1],
            "dt_entrega": doc_data[2], 
            "num_documento": doc_data[3].split('=')[1], 
            "type_doc": doc_data[4].split('=')[1]
        })
    dt = pd.DataFrame(
        data = [ list(doc.values()) for doc in documents_list ], 
        columns = [ 'company', 'dt_referencia', 'dt_entrega', 'num_documento', 'type_doc' ]
    )
    return dt
