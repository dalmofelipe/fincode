#!/bin/bash python3
import fincode as fc
import rich


def test_get_documents_by_code_cvm() -> None:
    """
    Busca documentos ITR de um intervalo de tempo
    
    @Params: Codigo CVM da empresa, data de inicio e fim do intervalo

    @Return: Lista de dataframes dos documentos
    """
    documents = fc.get_documents_by_code_cvm(22187, '01/01/2022', '31/12/2022')
    rich.print(documents)
    assert True


def test_normalize_code_cvm() -> None:
    """
    """
    cvm_code = 22187
    assert fc.normalize_code_cvm(cvm_code) == ',022187'
    cvm_code = 7
    assert fc.normalize_code_cvm(cvm_code) == ',000007'
    cvm_code = 1234567890
    assert fc.normalize_code_cvm(cvm_code) == ',1234567890'
