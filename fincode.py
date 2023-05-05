"""
Finance Code
"""
import aiohttp
import asyncio
import random
import pandas as pd
import re
from datetime import datetime
from io import StringIO
from typing import Optional, List, Union


URL_RAD_SEARCH = 'https://www.rad.cvm.gov.br/ENET/frmConsultaExternaCVM.aspx/ListarDocumentos'
URL_DADOS_CADASTRAIS = 'https://dados.cvm.gov.br/dados/CIA_ABERTA/CAD/DADOS/cad_cia_aberta.csv'
USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.91 Safari/537.36',
    'Mozilla/5.0 (iPad; U; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/50.0.125 Chrome/44.0.2403.125 Safari/537.36',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; SLCC2; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E)',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; MAARJS; rv:11.0) like Gecko',
    'Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-N900T Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 8_4 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) GSA/7.0.55539 Mobile/12H143 Safari/600.1.4'
]
HEADERS = {
    'user-agent': None,
    'referrer': 'https://google.com',
    'Accept-Language': 'en-US,en;q=0.9',
    'Pragma': 'no-cache',
}
OBJ_SEARCH = {
    "dataDe": '01/01/2022',
    "dataAte": '30/12/2022',
    "empresa": ',022187',
    "setorAtividade": '-1',
    "categoriaEmissor": '-1',
    "situacaoEmissor": '-1',
    "tipoParticipante": '-1',
    "dataReferencia": '',
    "categoria": 'EST_3',
    "periodo": '2',
    "horaIni": '',
    "horaFim": '',
    "palavraChave": '',
    "ultimaDtRef": 'false',
    "tipoEmpresa": '0',
    "token": '',
    "versaoCaptcha": ''
}
RGX_PARSER_DADOS_EMPRESAS = r'(\$&[a-zA-Z1-9.\- ]+\$&ITR|\d{2}/\d{2}/\d{4}|NumeroSequencialDocumento=\d+|CodigoTipoInstituicao=\d+)'


__DataFrame = None


def run_event_loop(
    function, *args
):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(function(*args))
    return __DataFrame


def normalize_cvm_code(
    cvm_code:int
):
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



def parser_data_companies(
    data_txt:str
):
    """
    O resultado da regex retorna todos os dados juntos numa lista. Esta lista sempre deve 
    conter uma quantidade de itens multiplo de 5. A cada 5 itens equivalem a um documento.

    Os dadoes estão na ordem:
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
    return documents_list



async def __run_search_companies_by_name(
    name_cia:str, 
    active:bool
): 
    """
    """
    name_cia = name_cia.upper()
    HEADERS['user-agent'] = random.choice(USER_AGENTS)

    async with aiohttp.ClientSession(headers=HEADERS) as session:
        async with session.get(URL_DADOS_CADASTRAIS) as response:
            global __DataFrame
            csv_text = await response.text(encoding='latin-1')
            csv_io = StringIO(csv_text)
            __DataFrame = pd.read_csv(csv_io, sep=';', header=0, index_col=False)
            __DataFrame = __DataFrame[ (__DataFrame['DENOM_SOCIAL'].str.contains(name_cia, na = False)) ]
            if active:
                __DataFrame = __DataFrame[ (__DataFrame['SIT'].str.contains('ATIVO', na = False)) ]
            __DataFrame = __DataFrame[['CNPJ_CIA', 'DENOM_SOCIAL', 'CD_CVM', 'SIT']].reset_index(drop=True)


def search_companies_by_name(
    name_cia: str, 
    active: Optional[bool] = False
)   -> pd.DataFrame:
    """
    Busca os dados cadastrais de companhias pelo nome;
    
    @Params: Um texto (string) será comparado com os nomes das Cia.  
    
    @Return: pandas.Dataframe de companhias em que houve casamento de padrão com texto de entrada
    """
    run_event_loop(__run_search_companies_by_name, name_cia, active)
    return __DataFrame


async def __run_search_companies_by_cvm_code(
    cod_cvm: int,
):
    HEADERS['user-agent'] = random.choice(USER_AGENTS)

    async with aiohttp.ClientSession(headers=HEADERS) as session:
        async with session.get(URL_DADOS_CADASTRAIS) as response:
            global __DataFrame
            csv_text = await response.text(encoding='latin-1')
            csv_io = StringIO(csv_text)
            __DataFrame = pd.read_csv(csv_io, sep=';', header=0, index_col=False)
            __DataFrame = __DataFrame[ __DataFrame['CD_CVM'] == cod_cvm ]
            __DataFrame = __DataFrame[['CNPJ_CIA', 'DENOM_SOCIAL', 'CD_CVM', 'SIT']].reset_index(drop=True)


def search_companies_by_cvm_code(
    cod_cvm: int
)   -> pd.DataFrame:
    """
    Busca os dados cadastrais de companhias pelo código CVM.
    
    @Params: um texto (string) será comparado com os codigos das companhias.
    
    @Return: pandas.Dataframe contendo os dados cadastrais de uma Cia
    """
    run_event_loop(__run_search_companies_by_cvm_code, cod_cvm)
    return __DataFrame


async def __run_search_itr_docs(
    cvm_code:int, 
    start_date_param:str,
    final_date_param:str
):
    HEADERS['user-agent'] = random.choice(USER_AGENTS)
    HEADERS['content-type'] = 'application/json'
    form_search = OBJ_SEARCH
    form_search['dataDe'] = start_date_param
    form_search['dataAte'] = final_date_param
    form_search['empresa'] = normalize_cvm_code(cvm_code)
    global __DataFrame
    async with aiohttp.ClientSession(headers=HEADERS) as session:
        async with session.post(URL_RAD_SEARCH, json=form_search) as response:
            __DataFrame = await response.json(encoding='utf-8')
            # apos a requisição, apenas os dados da resposta sera analisado
            data = __DataFrame['d']['dados']
            __DataFrame = parser_data_companies(data)



def search_itr_docs(
    cvm_code:int, 
    start_date_param:str,
    final_date_param:str
)   -> Union[List, None]:
    """
    Pesquisa documentos ITR num período específico
    
    @Params: Codigo CVM da empresa, data de inicio e fim do período

    @Return: Lista dos com dados dos documentos encontrados
    """
    start_date = datetime.strptime(start_date_param, '%d/%m/%Y')
    start_date = str(start_date.date().strftime("%d/%m/%Y"))

    final_date = datetime.strptime(final_date_param, '%d/%m/%Y')
    final_date = str(final_date.date().strftime("%d/%m/%Y"))

    if start_date > final_date:
        return None
    
    run_event_loop(__run_search_itr_docs, cvm_code, start_date, final_date)
    return __DataFrame
