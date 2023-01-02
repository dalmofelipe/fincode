"""
"""
import rich
import fincode as fc

df_cias_com_banco_no_nome = fc.search_by_name('banco', ativos=True)
df_petro_rio = fc.search_by_cvm_code(22187)

rich.print(df_cias_com_banco_no_nome)
rich.print(df_petro_rio)
