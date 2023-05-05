#!/bin/bash python3
import fincode as fc


def test_normalize_code_cvm() -> None:
    """
    """
    cvm_code = 22187
    assert fc.normalize_cvm_code(cvm_code) == ',022187'
    cvm_code = 7
    assert fc.normalize_cvm_code(cvm_code) == ',000007'
    cvm_code = 1234567890
    assert fc.normalize_cvm_code(cvm_code) == ',1234567890'
