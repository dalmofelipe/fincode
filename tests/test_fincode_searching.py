#!/bin/bash python3
import fincode as fc
import pandas as pd



def test_search_petro_rio_by_name():
    results = fc.search_by_name('PETRO RIO')
    assert results['CNPJ_CIA']\
        .to_string(index = False, header = False) == '10.629.105/0001-68'
    assert results.CD_CVM\
        .to_string(index = False, header = False) == '22187'


def test_search_petro_rio_by_cvm_code():
    df_petro_rio = fc.search_by_cvm_code(22187)
    assert df_petro_rio['DENOM_SOCIAL']\
        .to_string(index = False, header = False) == 'PETRO RIO S.A.'
    assert df_petro_rio['DENOM_SOCIAL']\
        .to_string(index = False, header = False).__eq__('PETRO RIO S.A.')


def test_search_companies_with_banco_in_name():
    results = fc.search_by_name('BANCO', active=True)
    assert isinstance(results, pd.DataFrame) 
    assert len(results) == 24
