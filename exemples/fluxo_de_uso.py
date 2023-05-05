#!/bin/bash python3
""" Exemplo de Uso """
import fincode as fc
import rich


# Pesquisando informações de empresas
df_cias_com_petro_no_nome = fc.search_companies_by_name('petro', active=True)
rich.print(df_cias_com_petro_no_nome)

# Vamos analisar dados da PETRO RIO - PRIO3
# Códiog CVM da PRIO3 = 22187
df_petro_rio = fc.search_companies_by_cvm_code(22187)
rich.print(df_petro_rio)

# Obs: Dados numericos já são convertidos
rich.print(df_petro_rio['CD_CVM'] * 2)

# Pesquisa numeros de documentos ITR da PRIO3 divulgados em 2022. 
# Obs: o quarto trimestre é divulgado nos primeiros mêses do ano seguinte
records = fc.search_itr_docs(22187, '01/01/2022', '31/12/2022')
rich.print(records)
