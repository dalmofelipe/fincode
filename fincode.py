"""
Finance Code

"""
import aiohttp
import asyncio
import random
import pandas as pd

from io import StringIO
from typing import Optional


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
__DF = None



def run_event_loop(function, *args):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(function(*args))
    return __DF


async def __run_search_by_name(name_cia, ativos):
    """
    """ 
    name_cia = name_cia.upper()
    HEADERS['user-agent'] = random.choice(USER_AGENTS)

    async with aiohttp.ClientSession(headers=HEADERS) as session:
        async with session.get(URL_DADOS_CADASTRAIS) as response:
            global __DF
            csv_text = await response.text(encoding='latin-1')
            csv_io = StringIO(csv_text)
            __DF = pd.read_csv(csv_io, sep=';', header=0, index_col=False)
            __DF = __DF[ (__DF['DENOM_SOCIAL'].str.contains(name_cia, na = False)) ]
            if ativos:
                __DF = __DF[ (__DF['SIT'].str.contains('ATIVO', na = False)) ]
            __DF = __DF[['CNPJ_CIA', 'DENOM_SOCIAL', 'CD_CVM', 'SIT']].reset_index(drop=True)


def search_by_name(
    name_cia: str, 
    ativos: Optional[bool] = False
):
    """
    Busca os dados cadastrais de compainhias pelo nome;
    
    Recebe um texto (string) será comparado com os nomes das Cia.  
    
    Retorna um pandas.Dataframe de Cias em que houve casamento de padrão 
    com texto de entrada
    """
    run_event_loop(__run_search_by_name, name_cia, ativos)
    return __DF


async def __run_search_by_cvm_code(
    cod_cvm: int,
):
    """
    """ 
    HEADERS['user-agent'] = random.choice(USER_AGENTS)

    async with aiohttp.ClientSession(headers=HEADERS) as session:
        async with session.get(URL_DADOS_CADASTRAIS) as response:
            global __DF
            csv_text = await response.text(encoding='latin-1')
            csv_io = StringIO(csv_text)
            __DF = pd.read_csv(csv_io, sep=';', header=0, index_col=False)
            __DF = __DF[ __DF['CD_CVM'] == cod_cvm ]
            __DF = __DF[['CNPJ_CIA', 'DENOM_SOCIAL', 'CD_CVM', 'SIT']].reset_index(drop=True)


def search_by_cvm_code(
    cod_cvm: int
):
    """
    Busca os dados cadastrais de Cias pelo código CVM.
    
    Recebe um texto (string) será comparado com os codigos das Cias.
    
    Retorna um pandas.Dataframe contendo os dados cadastrais de uma Cia
    """
    run_event_loop(__run_search_by_cvm_code, cod_cvm)
    return __DF
