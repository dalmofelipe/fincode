## fincode

Biblioteca para consultas de informações trimestrais - ITR - de empresas no sistema RAD CVM. 

Todos resultados retornam dataframes do pandas.

--- 

### Consultando Dados de Empresas

Exemplo de busca de informações cadastrais de empresas com termo 'PRIO' contida em sua denominação social

```py
import fincode as fc

df = fc.search_companies_by_name('prio')
print(df)
```

**RESULTADO**

```sh
             CNPJ_CIA DENOM_SOCIAL  CD_CVM    SIT
0  10.629.105/0001-68    PRIO S.A.   22187  ATIVO
```


<br>

### Busca de Documentos Trimestrais ITR da PRIO 22187

```py
import fincode as fc

# . . . 

docs = fc.search_itr_docs(22187, '01/01/2021', '31/12/2022')
print(docs)
```

**RESULTADO**

```sh
     company dt_referencia  dt_entrega num_documento type_doc
0  PRIO S.A.    30/09/2022  31/10/2022        121259        1
1  PRIO S.A.    30/06/2022  03/08/2022        119205        1
2  PRIO S.A.    31/03/2022  04/05/2022        114282        1
3  PRIO S.A.    30/09/2021  05/11/2021        109478        1
4  PRIO S.A.    30/09/2021  03/11/2021        109400        1
5  PRIO S.A.    30/06/2021  02/08/2021        107171        1
6  PRIO S.A.    31/03/2021  03/05/2021        103325        1
```


### WIP

Acessando dados dos relatórios trimestrais...

