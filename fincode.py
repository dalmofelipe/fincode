"""
Finance Code
"""
import aiohttp
import asyncio
import random
import pandas as pd

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

__DataFrame = None


def run_event_loop(
    function, *args
):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(function(*args))
    return __DataFrame


def normalize_code_cvm(
    code_cvm:int
):
    """ 
    Padroniza formato do código CVM para dados de consulta no RAD 

    Deve conter 7 caracteres, sendo o primeiro o simbolo de virgula. 

    Deve-se completar com zeros a esquerda, case o código CVM com menos de 6 digitos 
    """
    code_txt = str(code_cvm)

    while len(code_txt) < 6:
        code_txt = '0' + code_txt

    code_txt = ',' + code_txt
    return code_txt


async def __run_search_by_name(
    name_cia, ativos
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
            if ativos:
                __DataFrame = __DataFrame[ (__DataFrame['SIT'].str.contains('ATIVO', na = False)) ]
            __DataFrame = __DataFrame[['CNPJ_CIA', 'DENOM_SOCIAL', 'CD_CVM', 'SIT']].reset_index(drop=True)


def search_by_name(
    name_cia: str, ativos: Optional[bool] = False
):
    """
    Busca os dados cadastrais de companhias pelo nome;
    
    @Params: Um texto (string) será comparado com os nomes das Cia.  
    
    @Return: pandas.Dataframe de companhias em que houve casamento de padrão com texto de entrada
    """
    run_event_loop(__run_search_by_name, name_cia, ativos)
    return __DataFrame


async def __run_search_by_cvm_code(
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


def search_by_cvm_code(
    cod_cvm: int
):
    """
    Busca os dados cadastrais de companhias pelo código CVM.
    
    @Params: um texto (string) será comparado com os codigos das companhias.
    
    @Return: pandas.Dataframe contendo os dados cadastrais de uma Cia
    """
    run_event_loop(__run_search_by_cvm_code, cod_cvm)
    return __DataFrame


async def __run_get_documents_by_code_cvm(
    code_cvm:int, 
    start_date_param:str,
    final_date_param:str
):
    HEADERS['user-agent'] = random.choice(USER_AGENTS)
    HEADERS['content-type'] = 'application/json'
    form_search = OBJ_SEARCH
    form_search['dataDe'] = start_date_param
    form_search['dataAte'] = final_date_param
    form_search['empresa'] = normalize_code_cvm(code_cvm)
    global __DataFrame
    async with aiohttp.ClientSession(headers=HEADERS) as session:
        async with session.post(URL_RAD_SEARCH, json=form_search) as response:
            __DataFrame = await response.json(encoding='utf-8')
            __DataFrame = __DataFrame['d']['dados']
            #with open('saida.txt', 'w', encoding='latin-1') as file:
                #file.write(str(__DataFrame))


def get_documents_by_code_cvm(
    code_cvm:int, 
    start_date_param:str,
    final_date_param:str
)   -> Union[List, None]:
    """
    Pesquisa documentos de uma empresa pelo código CVM, incluso num intervalo determinado.

    @Param: código CVM, data de inicio e data fim do intervalo. Todos obrigatórios.

    @Return: Lista de documentos encontrados | None se intervalo incorreto 
    """
    start_date = datetime.strptime(start_date_param, '%d/%m/%Y')
    start_date = str(start_date.date().strftime("%d/%m/%Y"))

    final_date = datetime.strptime(final_date_param, '%d/%m/%Y')
    final_date = str(final_date.date().strftime("%d/%m/%Y"))

    if start_date > final_date:
        return None
    
    run_event_loop(__run_get_documents_by_code_cvm, code_cvm, start_date, final_date)
    return __DataFrame
