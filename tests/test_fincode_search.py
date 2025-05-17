#!/bin/bash python3
import pytest
import pandas as pd
import fincode as fc
import rich


# @pytest.mark.skip(reason="no way of currently testing this")
def test_search_companies_by_name():
    df_res = fc.search_companies_by_name('PRIO')
    # captura lista de valores da coluna CD_CVM
    cvm_codes = list(df_res.loc[:,'CD_CVM'].values)    
    assert 22187 in cvm_codes


def test_search_company_by_cvm_code():
    df_petro_rio:pd.DataFrame = fc.search_company_by_cvm_code(22187)
    assert df_petro_rio['DENOM_SOCIAL']\
        .to_string(index = False, header = False) == 'PRIO S.A.'
    assert df_petro_rio['DENOM_SOCIAL']\
        .to_string(index = False, header = False).__eq__('PRIO S.A.')


def test_search_companies_contains_banco_in_name():
    df_res = fc.search_companies_by_name('BANCO', only_actives=True)
    assert isinstance(df_res, pd.DataFrame)
    assert 'BANCO DO BRASIL S.A.' in df_res['DENOM_SOCIAL'].values
    assert 'ITAÚ UNIBANCO HOLDING S.A.' in df_res['DENOM_SOCIAL'].values
    assert len(df_res) == 21


def test_search_itr_documents() -> None:    
    df_res = fc.search_itr_docs(22187, '01/01/2022', '31/12/2022')
    assert isinstance(df_res, pd.DataFrame) and len(df_res.index) == 3
