#!/bin/bash python3
""" Exemplo de Uso """
import fincode as fc
import rich

# Pesquisando informações cadastrais de empresas, para obter o codigo CVM, por exemplo
df_result = fc.search_companies_by_name('rio', only_actives = True)
rich.print("---------------------------------------------------------------")
rich.print("\tConsultando empresas que contem 'RIO' no nome, para obter o codigo CVM\n")
rich.print(df_result)

# Código CVM da PRIO3 = 22187
df_prio = fc.search_company_by_cvm_code(22187)
rich.print("---------------------------------------------------------------")
rich.print("\tConsulta pelo codigo CVM 22187\n")
rich.print(df_prio)

# Consulta de documentos ITR da PRIO3 dos ultimos 5 anos. 
# Obs: o quarto trimestre pode aparecer nos primeiros meses do ano seguinte
df_itrdocs = fc.search_itr_docs(22187, '01/01/2019', '31/12/2024')
rich.print("---------------------------------------------------------------")
rich.print("\tListando ITRs dos utimos 5 anos da PRIO\n")
rich.print(df_itrdocs)