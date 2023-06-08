""" Finance Code """
import asyncio
import random
from datetime import datetime
from io import StringIO
from typing import List, Optional, Union

import aiohttp
import pandas as pd

from fincode.utils import (HEADERS, OBJ_SEARCH, URL_DADOS_CADASTRAIS, 
    URL_RAD_SEARCH, USER_AGENTS)
from fincode.core import parser_data_companies, normalize_cvm_code

__DataFrame = None


def run_event_loop(function, *args):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(function(*args))
    return __DataFrame





async def __run_search_companies_by_name(name_cia:str, active:bool): 
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


async def __run_search_companies_by_cvm_code(cod_cvm: int):
    HEADERS['user-agent'] = random.choice(USER_AGENTS)
    async with aiohttp.ClientSession(headers=HEADERS) as session:
        async with session.get(URL_DADOS_CADASTRAIS) as response:
            global __DataFrame
            csv_text = await response.text(encoding='latin-1')
            csv_io = StringIO(csv_text)
            __DataFrame = pd.read_csv(csv_io, sep=';', header=0, index_col=False)
            __DataFrame = __DataFrame[ __DataFrame['CD_CVM'] == cod_cvm ]
            __DataFrame = __DataFrame[['CNPJ_CIA', 'DENOM_SOCIAL', 'CD_CVM', 'SIT']].reset_index(drop=True)


async def __run_search_itr_docs(cvm_code:int, start_date_param:str, final_date_param:str):
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





def search_companies_by_name(name_cia: str, active: Optional[bool] = False) \
    -> pd.DataFrame:
    """
    Busca os dados cadastrais de companhias pelo nome;
    
    @Params: Um texto (string) será comparado com os nomes das Cia.  
    
    @Return: pandas.Dataframe de companhias em que houve casamento de padrão com texto de entrada
    """
    run_event_loop(__run_search_companies_by_name, name_cia, active)
    return __DataFrame



def search_companies_by_cvm_code(cod_cvm: int) -> pd.DataFrame:
    """
    Busca os dados cadastrais de companhias pelo código CVM.
    
    @Params: um texto (string) será comparado com os codigos das companhias.
    
    @Return: pandas.Dataframe contendo os dados cadastrais de uma Cia
    """
    run_event_loop(__run_search_companies_by_cvm_code, cod_cvm)
    return __DataFrame



def search_itr_docs(cvm_code:int, start_date_param:str, final_date_param:str) \
    -> Union[List, None]:
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
