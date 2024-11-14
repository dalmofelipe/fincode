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

PRIO S.A.    30/06/2024  06/08/2024        140433        1




[1] criar função para request deste link
@param cvm_code
https://www.rad.cvm.gov.br/ENET/frmGerenciaPaginaFRE.aspx?NumeroSequencialDocumento=140433&CodigoTipoInstituicao=1


acessar entry point Este entry pointer

[2] definir uma dict para select option de documentos
 <select name="cmbGrupo" id="cmbGrupo" Label="Você esta vendo:" ShowLabel="true">
	<option value="1">Dados da Empresa</option>
	<option value="78">DFs Individuais</option>
	<option selected="selected" value="135">DFs Consolidadas</option>
	<option value="PDF|192">Coment&#225;rio do Desempenho</option>
	<option value="PDF|193">Notas Explicativas</option>
	<option value="PDF|194">Coment&#225;rio Sobre o Comportamento das Proje&#231;&#245;es Empresariais</option>
	<option value="PDF|199">Outras Informa&#231;&#245;es que a Companhia Entenda Relevantes</option>
	<option value="207">Pareceres e Declara&#231;&#245;es</option>
</select>

IRT_DOCS = {
	'DADOS_DA_EMPRESA': 1,
	'DFS_INDIVIDUAIS': 78,
	'DFS_CONSOLIDADAS': 135
}

ITR_DOCS.DADOS_DA_EMPRESA




[3] parser ou beautiful soup ou parsel 

pegar value dos options
<select name="cmbQuadro" id="cmbQuadro" ShowLabel="true">
<option value="frmDemonstracaoFinanceiraITR.aspx?Informacao=2&amp;Demonstracao=2&amp;Periodo=0&amp;Grupo=DFs+Consolidadas&amp;Quadro=Balan%c3%a7o+Patrimonial+Ativo&amp;NomeTipoDocumento=ITR&amp;Empresa=PRIO S.A.&amp;DataReferencia=2022-09-30&amp;Versao=1">Balan&#231;o Patrimonial Ativo</option>
<option value="frmDemonstracaoFinanceiraITR.aspx?Informacao=2&amp;Demonstracao=3&amp;Periodo=0&amp;Grupo=DFs+Consolidadas&amp;Quadro=Balan%c3%a7o+Patrimonial+Passivo&amp;NomeTipoDocumento=ITR&amp;Empresa=PRIO S.A.&amp;DataReferencia=2022-09-30&amp;Versao=1">Balan&#231;o Patrimonial Passivo</option>
<option selected="selected" value="frmDemonstracaoFinanceiraITR.aspx?Informacao=2&amp;Demonstracao=4&amp;Periodo=0&amp;Grupo=DFs+Consolidadas&amp;Quadro=Demonstra%c3%a7%c3%a3o+do+Resultado&amp;NomeTipoDocumento=ITR&amp;Empresa=PRIO S.A.&amp;DataReferencia=2022-09-30&amp;Versao=1">Demonstra&#231;&#227;o do Resultado</option>
<option value="frmDemonstracaoFinanceiraITR.aspx?Informacao=2&amp;Demonstracao=5&amp;Periodo=0&amp;Grupo=DFs+Consolidadas&amp;Quadro=Demonstra%c3%a7%c3%a3o+do+Resultado+Abrangente&amp;NomeTipoDocumento=ITR&amp;Empresa=PRIO S.A.&amp;DataReferencia=2022-09-30&amp;Versao=1">Demonstra&#231;&#227;o do Resultado Abrangente</option>
<option value="frmDemonstracaoFinanceiraITR.aspx?Informacao=2&amp;Demonstracao=99&amp;Periodo=0&amp;Grupo=DFs+Consolidadas&amp;Quadro=Demonstra%c3%a7%c3%a3o+do+Fluxo+de+Caixa&amp;NomeTipoDocumento=ITR&amp;Empresa=PRIO S.A.&amp;DataReferencia=2022-09-30&amp;Versao=1">Demonstra&#231;&#227;o do Fluxo de Caixa</option>
<option value="frmDemonstracaoFinanceiraITR.aspx?Informacao=200&amp;Demonstracao=8&amp;Periodo=4|6&amp;Grupo=DFs+Consolidadas&amp;Quadro=Demonstra%c3%a7%c3%a3o+das+Muta%c3%a7%c3%b5es+do+Patrim%c3%b4nio+L%c3%adquido&amp;NomeTipoDocumento=ITR&amp;Empresa=PRIO S.A.&amp;DataReferencia=2022-09-30&amp;Versao=1">Demonstra&#231;&#227;o das Muta&#231;&#245;es do Patrim&#244;nio L&#237;quido</option>
<option value="frmDemonstracaoFinanceiraITR.aspx?Informacao=2&amp;Demonstracao=9&amp;Periodo=0&amp;Grupo=DFs+Consolidadas&amp;Quadro=Demonstra%c3%a7%c3%a3o+de+Valor+Adicionado&amp;NomeTipoDocumento=ITR&amp;Empresa=PRIO S.A.&amp;DataReferencia=2022-09-30&amp;Versao=1">Demonstra&#231;&#227;o de Valor Adicionado</option>
</select>


[4] parsel tag script
<script type="text/javascript">
//<![CDATA[
window.frames[0].location='frmDemonstracaoFinanceiraITR.aspx?Informacao=2&Demonstracao=4&Periodo=0&Grupo=DFs+Consolidadas&Quadro=Demonstra%c3%a7%c3%a3o+do+Resultado&NomeTipoDocumento=ITR&Empresa=PRIO S.A.&DataReferencia=2022-09-30&Versao=1&CodTipoDocumento=3&NumeroSequencialDocumento=121259&NumeroSequencialRegistroCvm=2047&CodigoTipoInstituicao=1&Hash=TPJcymsReAUxJNokbLHcgQ8BpWbfGhgn1vkeO5lUOA';//]]>
</script>