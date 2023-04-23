#!/bin/bash python3
""" Exemplo de Uso """
import fincode as fc
import rich


# pesquisando informações de empresas
df_cias_com_banco_no_nome = fc.search_by_name('petro')
rich.print(df_cias_com_banco_no_nome)

# vamos analisar dados da PETRO RIO - PRIO3
# Códiog CVM da PRIO3 = 22187
df_petro_rio = fc.search_by_cvm_code(22187)
rich.print(df_petro_rio)

# obs: dados numericos já são convertidos
rich.print(df_petro_rio['CD_CVM'] * 2)

# Pesquisa numeros de documentos ITR da PRIO3 divulgados em 2022. 
# Obs: o quarto trimestre é divulgado nos primeiros mêses do ano seguinte
records = fc.get_documents_by_code_cvm(22187, '01/01/2022', '31/12/2022')
print(records)
