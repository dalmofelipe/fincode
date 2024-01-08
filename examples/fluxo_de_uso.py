#!/bin/bash python3
""" Exemplo de Uso """
import fincode as fc
import rich

# Pesquisando informações cadastrais de empresas, para obter o codigo CVM, por exemplo
df_cias_com_rio_no_nome = fc.search_companies_by_name('rio', active=False)
rich.print("---------------------------------------------------------------")
rich.print("\tBuscando empresas com 'RIO' no nome, para obter o codigo CVM\n")
rich.print(df_cias_com_rio_no_nome)


# Analisando dados da PETRO RIO - PRIO3
# Código CVM da PRIO3 = 22187
df_petro_rio = fc.search_companies_by_cvm_code(22187)
rich.print("---------------------------------------------------------------")
rich.print("\tBuscando empresas pelo codigo CVM 22187\n")
rich.print(df_petro_rio)


rich.print("---------------------------------------------------------------")
rich.print("\tConversão automática de dados numéricos\n")
# Obs: Dados numericos são convertidos
rich.print(f'22187 x 2 = {df_petro_rio["CD_CVM"].values[0] * 2}')


# Busque documentos ITR da PRIO3 dos ultimos 5 anos. 
# Obs: o quarto trimestre pode aparecer nos primeiros meses do ano seguinte
records = fc.search_itr_docs(22187, '01/01/2019', '31/12/2024')
rich.print("---------------------------------------------------------------")
rich.print("\tListando ITRs dos utimos 5 anos da PRIO\n")
rich.print(records)
