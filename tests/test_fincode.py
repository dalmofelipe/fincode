import fincode as fc


def test_search_petro_rio_by_cvm_code():
    results = fc.search_by_name('PETRO RIO')
    for r in results:
        print(r)


def test_search_petro_rio_by_cvm_code():
    df_petro_rio = fc.search_by_cvm_code(22187)
    assert df_petro_rio['DENOM_SOCIAL']\
        .to_string(index = False, header = False) == 'PETRO RIO S.A.'
    assert df_petro_rio['DENOM_SOCIAL']\
        .to_string(index = False, header = False).__eq__('PETRO RIO S.A.')
