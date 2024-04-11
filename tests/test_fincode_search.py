#!/bin/bash python3
import pytest
import pandas as pd
import fincode as fc


# @pytest.mark.skip(reason="no way of currently testing this")
def test_search_companies_by_name():
    df_res = fc.search_companies_by_name('PRIO')
    # captura lista de valores da coluna CD_CVM
    cvm_codes = list(df_res.loc[:,'CD_CVM'].values)    
    assert 22187 in cvm_codes


def test_search_company_by_cvm_code():
    df_petro_rio = fc.search_company_by_cvm_code(22187)
    assert df_petro_rio['DENOM_SOCIAL']\
        .to_string(index = False, header = False) == 'PRIO S.A.'
    assert df_petro_rio['DENOM_SOCIAL']\
        .to_string(index = False, header = False).__eq__('PRIO S.A.')


def test_search_companies_with_banco_in_name():
    df_res = fc.search_companies_by_name('BANCO', active=True)
    assert isinstance(df_res, pd.DataFrame) 
    assert len(df_res) == 22


def test_search_itr_documents() -> None:    
    df_res = fc.search_itr_docs(22187, '01/01/2022', '31/12/2022')
    assert isinstance(df_res, pd.DataFrame) and len(df_res.index) == 3
