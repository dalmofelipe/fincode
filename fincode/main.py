""" Finance Code """
import asyncio
import random
from datetime import datetime
from io import StringIO
from typing import Optional

import aiohttp
import pandas as pd

from fincode.utils import (
    HEADERS, OBJ_SEARCH, URL_DADOS_CADASTRAIS, URL_RAD_SEARCH, USER_AGENTS
)
from fincode.core import parser_data_companies, normalize_cvm_code


async def __run_search_companies_by_name(name_cia:str, only_actives:bool): 
    name_cia = name_cia.upper()
    HEADERS['user-agent'] = random.choice(USER_AGENTS)
    async with aiohttp.ClientSession(headers=HEADERS) as session:
        async with session.get(URL_DADOS_CADASTRAIS) as response:
            # global __DataFrame
            csv_text = await response.text(encoding='latin-1')
            csv_io = StringIO(csv_text)
            __dataframe = pd.read_csv(csv_io, sep=';', header=0, index_col=False)
            __dataframe = __dataframe[ (__dataframe['DENOM_SOCIAL'].str.contains(name_cia, na = False)) ]
            if only_actives:
                __dataframe = __dataframe[ (__dataframe['SIT'].str.contains('ATIVO', na = False)) ]
            __dataframe = __dataframe[['CNPJ_CIA', 'DENOM_SOCIAL', 'CD_CVM', 'SIT']].reset_index(drop=True)
            return __dataframe

def search_companies_by_name(name_cia: str, only_actives = True):
    """
    Busca os dados cadastrais de companhias pelo nome;
    
    @Params: String 'name_cia' - será comparado com os nomes das Cia.
    @Params: Boolean 'only_actives' - filtra companhias com registro ativo. Este o comportamento padrão.
    
    @Return: pandas.Dataframe de companhias em que houve casamento de padrão com texto de entrada
    """
    return asyncio.run(__run_search_companies_by_name(name_cia, only_actives))



async def __run_search_company_by_cvm_code(cod_cvm: int):
    HEADERS['user-agent'] = random.choice(USER_AGENTS)
    async with aiohttp.ClientSession(headers=HEADERS) as session:
        async with session.get(URL_DADOS_CADASTRAIS) as response:
            csv_text = await response.text(encoding='latin-1')
            csv_io = StringIO(csv_text)
            __dataframe = pd.read_csv(csv_io, sep=';', header=0, index_col=False)
            __dataframe = __dataframe[ __dataframe['CD_CVM'] == cod_cvm ]
            __dataframe = __dataframe[['CNPJ_CIA', 'DENOM_SOCIAL', 'CD_CVM', 'SIT']].reset_index(drop=True)
            return __dataframe

def search_company_by_cvm_code(cod_cvm: int):
    """
    Busca os dados cadastrais de companhias pelo código CVM.
    
    @Params: um texto (string) será comparado com os codigos das companhias.
    
    @Return: pandas.Dataframe contendo os dados cadastrais de uma Cia
    """
    return asyncio.run(__run_search_company_by_cvm_code(cod_cvm))


async def __run_search_itr_docs(cvm_code:int, start_date_param:str, final_date_param:str):
    HEADERS['user-agent'] = random.choice(USER_AGENTS)
    HEADERS['content-type'] = 'application/json'
    form_search = OBJ_SEARCH
    form_search['dataDe'] = start_date_param
    form_search['dataAte'] = final_date_param
    form_search['empresa'] = normalize_cvm_code(cvm_code)
    async with aiohttp.ClientSession(headers=HEADERS) as session:
        async with session.post(URL_RAD_SEARCH, json=form_search) as response:
            __dataframe = await response.json(encoding='utf-8')
            # apos a requisição, apenas os dados da resposta sera analisado
            data = __dataframe['d']['dados']
            __dataframe = parser_data_companies(data)
            return __dataframe

def search_itr_docs(cvm_code:int, start_date_param:str, final_date_param:str):
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
    
    return asyncio.run(__run_search_itr_docs(cvm_code, start_date, final_date))
