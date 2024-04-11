#!/bin/bash python3
""" Exemplo de Uso """
import fincode as fc
import rich

# Pesquisando informações cadastrais de empresas, para obter o codigo CVM, por exemplo
df_companies = fc.search_companies_by_name('prio', active=True)
rich.print(df_companies)

# Tambem é possível diretamente pelo CVM Code
df_prio = fc.search_company_by_cvm_code(22187)
rich.print(df_prio)

# Pesquisa numeros de documentos ITR da PRIO3 divulgados em 2022. 
# Obs: o quarto trimestre pode aparecer nos primeiros meses do ano seguinte
df_list_itr_docs = fc.search_itr_docs(22187, '01/01/2021', '31/12/2023')
rich.print(df_list_itr_docs)
