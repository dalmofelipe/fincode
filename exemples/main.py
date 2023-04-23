"""
Exemplo de Uso
"""
import rich

import fincode as fc

"""
df_cias_com_banco_no_nome = fc.search_by_name('INTER', ativos=True)
rich.print(df_cias_com_banco_no_nome)

df_petro_rio = fc.search_by_cvm_code(22187)
rich.print(df_petro_rio)
rich.print(df_petro_rio['CD_CVM'] * 2)

df_banestes = fc.search_by_cvm_code(1155)
rich.print(df_banestes)
"""
records = fc.get_documents_by_code_cvm(22187, '01/01/2022', '31/12/2022')
print(records)