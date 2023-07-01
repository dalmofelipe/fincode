# CVM

### ITR

Lib para consultas de tabelas de informações trimestrais de empresas via sistema RAD

<br>

### 0. Consultar código CVM da empresa

https://cvmweb.cvm.gov.br/SWB/Sistemas/SCW/CPublica/CiaAb/FormBuscaCiaAbOrdAlf.aspx?LetraInicial=**P**
    
Código CVM da Petro Rio 22187


<br>

### 1. consultar documentos pelo formulário RAD

```http
POST https://www.rad.cvm.gov.br/ENET/frmConsultaExternaCVM.aspx/ListarDocumentos HTTP/1.1
Content-type: application/json

// Objeto do formulário de consulta do sistema RAD
{
    dataDe: '01/01/2022',
    dataAte: '30/12/2022',
    empresa: ',022187',
    setorAtividade: '-1',
    categoriaEmissor: '-1',
    situacaoEmissor: '-1',
    tipoParticipante: '-1',
    dataReferencia: '',
    categoria: 'EST_3',
    periodo: '2',
    horaIni: '',
    horaFim: '',
    palavraChave: '',
    ultimaDtRef: 'false',
    tipoEmpresa: '0',
    token: '',
    versaoCaptcha: ''
}
```

**RESPOSTA**

```json
{
    "d": {
        "__type": "frmConsultaExternaCVM+RetornoTelaConsultaExterna",
        "temErro": false,
        "expirouSessao": false,
        "msgErro": "",
        "dados": "02218-7$&PETRO RIO S.A.$&ITR - Informações Trimestrais$& - $&<spanOrder></spanOrder> - $&<spanOrder>20220331</spanOrder> 31/03/2022$&<spanOrder>20220504</spanOrder> 04/05/2022 18:59$&Ativo$&1$&AP$&<i class='fi-page-search' id='VisualizarDocumento' style='font-size: 18px;cursor:pointer;color:#0C7766;' onclick=OpenPopUpVer('frmGerenciaPaginaFRE.aspx?NumeroSequencialDocumento=114282&CodigoTipoInstituicao=1') title='Visualizar o Documento'> </i><i class='fi-download' style='font-size: 18px;cursor:pointer;color:#0C7766;' title='Download' onclick=OpenDownloadDocumentos('114282','1','022187ITR310320220100114282-66','ITR')> </i><i class='fi-info' style='font-size: 18px;cursor:pointer;color:#696969;' title='Documento não possui local de publicação.'> </i><i class='fi-clipboard-notes' style='font-size: 18px;cursor:pointer;color:#0C7766;' title='Exibir Protocolo de Entrega' onclick='exibirProtocoloPDF(114282, \"ENET\")'</i>$&$&&*02218-7$&PETRO RIO S.A.$&ITR - Informações Trimestrais$& - $&<spanOrder></spanOrder> - $&<spanOrder>20220630</spanOrder> 30/06/2022$&<spanOrder>20220803</spanOrder> 03/08/2022 19:38$&Ativo$&1$&AP$&<i class='fi-page-search' id='VisualizarDocumento' style='font-size: 18px;cursor:pointer;color:#0C7766;' onclick=OpenPopUpVer('frmGerenciaPaginaFRE.aspx?NumeroSequencialDocumento=119205&CodigoTipoInstituicao=1') title='Visualizar o Documento'> </i><i class='fi-download' style='font-size: 18px;cursor:pointer;color:#0C7766;' title='Download' onclick=OpenDownloadDocumentos('119205','1','022187ITR300620220100119205-77','ITR')> </i><i class='fi-info' style='font-size: 18px;cursor:pointer;color:#696969;' title='Documento não possui local de publicação.'> </i><i class='fi-clipboard-notes' style='font-size: 18px;cursor:pointer;color:#0C7766;' title='Exibir Protocolo de Entrega' onclick='exibirProtocoloPDF(119205, \"ENET\")'</i>$&$&&*02218-7$&PETRO RIO S.A.$&ITR - Informações Trimestrais$& - $&<spanOrder></spanOrder> - $&<spanOrder>20220930</spanOrder> 30/09/2022$&<spanOrder>20221031</spanOrder> 31/10/2022 19:25$&Ativo$&1$&AP$&<i class='fi-page-search' id='VisualizarDocumento' style='font-size: 18px;cursor:pointer;color:#0C7766;' onclick=OpenPopUpVer('frmGerenciaPaginaFRE.aspx?NumeroSequencialDocumento=121259&CodigoTipoInstituicao=1') title='Visualizar o Documento'> </i><i class='fi-download' style='font-size: 18px;cursor:pointer;color:#0C7766;' title='Download' onclick=OpenDownloadDocumentos('121259','1','022187ITR300920220100121259-72','ITR')> </i><i class='fi-info' style='font-size: 18px;cursor:pointer;color:#696969;' title='Documento não possui local de publicação.'> </i><i class='fi-clipboard-notes' style='font-size: 18px;cursor:pointer;color:#0C7766;' title='Exibir Protocolo de Entrega' onclick='exibirProtocoloPDF(121259, \"ENET\")'</i>$&$&&*",
        "SolicitarCaptcha": "N"
    }
}
```


<br>

### 2. Parse da resposta, extraindo dados dos documentos - NumeroSequencialDocumento e CodigoTipoInstituicao

```md
02218-7$&PETRO RIO S.A.$&ITR - Informações Trimestrais$& - $&<spanOrder></spanOrder> - $&<spanOrder>20220331</spanOrder> **31/03/2022**$&<spanOrder>20220504</spanOrder> 04/05/2022 18:59$&Ativo$&1$&AP$&<i class='fi-page-search' id='VisualizarDocumento' style='font-size: 18px;cursor:pointer;color:#0C7766;' onclick=

**OpenPopUpVer('frmGerenciaPaginaFRE.aspx?NumeroSequencialDocumento=114282&CodigoTipoInstituicao=1')**

 title='Visualizar o Documento'> </i><i class='fi-download' style='font-size: 18px;cursor:pointer;color:#0C7766;' title='Download' onclick=OpenDownloadDocumentos('114282','1','022187ITR310320220100114282-66','ITR')> </i><i class='fi-info' style='font-size: 18px;cursor:pointer;color:#696969;' title='Documento não possui local de publicação.'> </i><i class='fi-clipboard-notes' style='font-size: 18px;cursor:pointer;color:#0C7766;' title='Exibir Protocolo de Entrega' onclick='exibirProtocoloPDF(114282, \"ENET\")'</i>

$&$&&*02218-7$&PETRO RIO S.A.$&ITR - Informações Trimestrais$& - $&<spanOrder></spanOrder> - $&<spanOrder>20220630</spanOrder> **30/06/2022**$&<spanOrder>20220803</spanOrder> 03/08/2022 19:38$&Ativo$&1$&AP$&<i class='fi-page-search' id='VisualizarDocumento' style='font-size: 18px;cursor:pointer;color:#0C7766;' onclick=

**OpenPopUpVer('frmGerenciaPaginaFRE.aspx?NumeroSequencialDocumento=119205&CodigoTipoInstituicao=1')**

 title='Visualizar o Documento'> </i><i class='fi-download' style='font-size: 18px;cursor:pointer;color:#0C7766;' title='Download' onclick=OpenDownloadDocumentos('119205','1','022187ITR300620220100119205-77','ITR')> </i><i class='fi-info' style='font-size: 18px;cursor:pointer;color:#696969;' title='Documento não possui local de publicação.'> </i><i class='fi-clipboard-notes' style='font-size: 18px;cursor:pointer;color:#0C7766;' title='Exibir Protocolo de Entrega' onclick='exibirProtocoloPDF(119205, \"ENET\")'</i>

$&$&&*02218-7$&PETRO RIO S.A.$&ITR - Informações Trimestrais$& - $&<spanOrder></spanOrder> - $&<spanOrder>20220930</spanOrder> **30/09/2022** $&<spanOrder>20221031</spanOrder> 31/10/2022 19:25$&Ativo$&1$&AP$&<i class='fi-page-search' id='VisualizarDocumento' style='font-size: 18px;cursor:pointer;color:#0C7766;' onclick=

**OpenPopUpVer('frmGerenciaPaginaFRE.aspx?NumeroSequencialDocumento=121259&CodigoTipoInstituicao=1')**

 title='Visualizar o Documento'> </i><i class='fi-download' style='font-size: 18px;cursor:pointer;color:#0C7766;' title='Download' onclick=OpenDownloadDocumentos('121259','1','022187ITR300920220100121259-72','ITR')> </i><i class='fi-info' style='font-size: 18px;cursor:pointer;color:#696969;' title='Documento não possui local de publicação.'> </i><i class='fi-clipboard-notes' style='font-size: 18px;cursor:pointer;color:#0C7766;' title='Exibir Protocolo de Entrega' onclick='exibirProtocoloPDF(121259, \"ENET\")'</i>$&$&&*
```

**Informações extraídas**

| Data | Num Doc | Link completo |
| --- | --- | --- |
| 31/03/2022 | 114282 | https://www.rad.cvm.gov.br/ENET/frmGerenciaPaginaFRE.aspx?NumeroSequencialDocumento=114282&CodigoTipoInstituicao=1 |
| 30/06/2022 | 119205 | https://www.rad.cvm.gov.br/ENET/frmGerenciaPaginaFRE.aspx?NumeroSequencialDocumento=119205&CodigoTipoInstituicao=1 |
| 30/09/2022 | 121259 | https://www.rad.cvm.gov.br/ENET/frmGerenciaPaginaFRE.aspx?NumeroSequencialDocumento=121259&CodigoTipoInstituicao=1 |

Com link acima, é possível consultar o código da resposta do RAD. Nele contem o link do **DFs Consolidadas / Demonstração do Resultado - (Reais Mil)** na tag script bem no final do arquivo e também a HASH que necessária para as demais consultas.


<br>

### 3. GET no link de visualizar documento com os dados - NumeroSequencialDocumento e CodigoTipoInstituicao

Acessar essa rota é obrigatória, para liberar acessos as outras rotas de documentos

```http
### abrir documento
GET https://www.rad.cvm.gov.br/ENET/frmGerenciaPaginaFRE.aspx?NumeroSequencialDocumento=121259&CodigoTipoInstituicao=1 HTTP/1.1
```

**RESPOSTA**

A requisão responde com links do select dos documentos

```
<select name="cmbQuadro" id="cmbQuadro" ShowLabel="true">

<option value="frmDemonstracaoFinanceiraITR.aspx?Informacao=2&amp;Demonstracao=2&amp;Periodo=0&amp;Grupo=DFs+Consolidadas&amp;Quadro=Balan%c3%a7o+Patrimonial+Ativo&amp;NomeTipoDocumento=ITR&amp;Empresa=PETRO RIO S.A.&amp;DataReferencia=2022-09-30&amp;Versao=1">Balan&#231;o Patrimonial Ativo</option>

<option value="frmDemonstracaoFinanceiraITR.aspx?Informacao=2&amp;Demonstracao=3&amp;Periodo=0&amp;Grupo=DFs+Consolidadas&amp;Quadro=Balan%c3%a7o+Patrimonial+Passivo&amp;NomeTipoDocumento=ITR&amp;Empresa=PETRO RIO S.A.&amp;DataReferencia=2022-09-30&amp;Versao=1">Balan&#231;o Patrimonial Passivo</option>

<option selected="selected" value="frmDemonstracaoFinanceiraITR.aspx?Informacao=2&amp;Demonstracao=4&amp;Periodo=0&amp;Grupo=DFs+Consolidadas&amp;Quadro=Demonstra%c3%a7%c3%a3o+do+Resultado&amp;NomeTipoDocumento=ITR&amp;Empresa=PETRO RIO S.A.&amp;DataReferencia=2022-09-30&amp;Versao=1">Demonstra&#231;&#227;o do Resultado</option>

<option value="frmDemonstracaoFinanceiraITR.aspx?Informacao=2&amp;Demonstracao=5&amp;Periodo=0&amp;Grupo=DFs+Consolidadas&amp;Quadro=Demonstra%c3%a7%c3%a3o+do+Resultado+Abrangente&amp;NomeTipoDocumento=ITR&amp;Empresa=PETRO RIO S.A.&amp;DataReferencia=2022-09-30&amp;Versao=1">Demonstra&#231;&#227;o do Resultado Abrangente</option>

<option value="frmDemonstracaoFinanceiraITR.aspx?Informacao=2&amp;Demonstracao=99&amp;Periodo=0&amp;Grupo=DFs+Consolidadas&amp;Quadro=Demonstra%c3%a7%c3%a3o+do+Fluxo+de+Caixa&amp;NomeTipoDocumento=ITR&amp;Empresa=PETRO RIO S.A.&amp;DataReferencia=2022-09-30&amp;Versao=1">Demonstra&#231;&#227;o do Fluxo de Caixa</option>

<option value="frmDemonstracaoFinanceiraITR.aspx?Informacao=200&amp;Demonstracao=8&amp;Periodo=4|6&amp;Grupo=DFs+Consolidadas&amp;Quadro=Demonstra%c3%a7%c3%a3o+das+Muta%c3%a7%c3%b5es+do+Patrim%c3%b4nio+L%c3%adquido&amp;NomeTipoDocumento=ITR&amp;Empresa=PETRO RIO S.A.&amp;DataReferencia=2022-09-30&amp;Versao=1">Demonstra&#231;&#227;o das Muta&#231;&#245;es do Patrim&#244;nio L&#237;quido</option>

<option value="frmDemonstracaoFinanceiraITR.aspx?Informacao=2&amp;Demonstracao=9&amp;Periodo=0&amp;Grupo=DFs+Consolidadas&amp;Quadro=Demonstra%c3%a7%c3%a3o+de+Valor+Adicionado&amp;NomeTipoDocumento=ITR&amp;Empresa=PETRO RIO S.A.&amp;DataReferencia=2022-09-30&amp;Versao=1">Demonstra&#231;&#227;o de Valor Adicionado</option>

</select>
```

E principalmente o link do "documento de entrada" no sistema RAD e uma HASH na tag script

```javascript
<script type="text/javascript">
//<![CDATA[
window.frames[0].location='frmDemonstracaoFinanceiraITR.aspx?Informacao=2&Demonstracao=4&Periodo=0&Grupo=DFs+Consolidadas&Quadro=Demonstra%c3%a7%c3%a3o+do+Resultado&NomeTipoDocumento=ITR&Empresa=PETRO RIO S.A.&DataReferencia=2022-09-30&Versao=1&CodTipoDocumento=3&NumeroSequencialDocumento=121259&NumeroSequencialRegistroCvm=2047&CodigoTipoInstituicao=1&Hash=s5XZ7sJHHMWDxgaVgx5bfhLSspwAaHc9JgSLQuhDszQ';//]]>
</script>
```

**Hash=s5XZ7sJHHMWDxgaVgx5bfhLSspwAaHc9JgSLQuhDszQ**

Importante: a HASH é atualizada a cada hora!.


<br>

### 4. Parse da response visando a tag script extraindo link de acesso da tabela e principalmente a HASH

Os links do select / option estão incompletos:

```
frmDemonstracaoFinanceiraITR.aspx?Informacao=2&amp;Demonstracao=3&amp;Periodo=0&amp;Grupo=DFs+Consolidadas&amp;Quadro=Balan%c3%a7o+Patrimonial+Passivo&amp;NomeTipoDocumento=ITR&amp;Empresa=PETRO RIO S.A.&amp;DataReferencia=2022-09-30&amp;Versao=1
```

Primeiro deve substituir os caracteres ```&amp;``` por ```&```. E também deve adicionar dados do documento **CodTipoDocumento, NumeroSequencialDocumento, NumeroSequencialRegistroCvm, CodigoTipoInstituicao e Hash**

```
frmDemonstracaoFinanceiraITR.aspx?Informacao=2&Demonstracao=4&Periodo=0&Grupo=DFs+Consolidadas&Quadro=Demonstra%c3%a7%c3%a3o+do+Resultado&NomeTipoDocumento=ITR&Empresa=PRIO S.A.&DataReferencia=2022-09-30&Versao=1&CodTipoDocumento=3&NumeroSequencialDocumento=121259&NumeroSequencialRegistroCvm=2047&CodigoTipoInstituicao=1&Hash=kD4NPAqQszIAmV4rIMIPOLJzyVo2juPg5uCQHO2QQ
```

<br>

### DFs Consolidadas

DFs Consolidadas / Demonstração do Resultado - (Reais Mil)

```http
GET https://www.rad.cvm.gov.br/ENET/frmDemonstracaoFinanceiraITR.aspx?Informacao=2&Demonstracao=4&Periodo=0&Grupo=DFs+Consolidadas&Quadro=Demonstra%c3%a7%c3%a3o+do+Resultado&NomeTipoDocumento=ITR&Empresa=PETRO RIO S.A.&DataReferencia=2022-09-30&Versao=1&CodTipoDocumento=3&NumeroSequencialDocumento=121259&NumeroSequencialRegistroCvm=2047&CodigoTipoInstituicao=1&Hash=y3IyKxBke2XIX7QxbQAOb4C8na7GDQuHnlBeTaV73Rg
```

DFs Consolidadas / Balanço Patrimonial Ativo - (Reais Mil)

```http
GET https://www.rad.cvm.gov.br/ENET/frmDemonstracaoFinanceiraITR.aspx?Informacao=2&Demonstracao=2&Periodo=0&Grupo=DFs+Consolidadas&Quadro=Balan%c3%a7o+Patrimonial+Ativo&NomeTipoDocumento=ITR&Empresa=PETRO RIO S.A.&DataReferencia=2022-09-30&Versao=1&CodTipoDocumento=3&NumeroSequencialDocumento=121259&NumeroSequencialRegistroCvm=2047&CodigoTipoInstituicao=1&Hash=y3IyKxBke2XIX7QxbQAOb4C8na7GDQuHnlBeTaV73Rg
```

DFs Consolidadas / Balanço Patrimonial Passivo - (Reais Mil)

```http
GET https://www.rad.cvm.gov.br/ENET/frmDemonstracaoFinanceiraITR.aspx?Informacao=2&Demonstracao=3&Periodo=0&Grupo=DFs+Consolidadas&Quadro=Balan%c3%a7o+Patrimonial+Passivo&NomeTipoDocumento=ITR&Empresa=PETRO RIO S.A.&DataReferencia=2022-09-30&Versao=1&CodTipoDocumento=3&NumeroSequencialDocumento=121259&NumeroSequencialRegistroCvm=2047&CodigoTipoInstituicao=1&Hash=s5XZ7sJHHMWDxgaVgx5bfhLSspwAaHc9JgSLQuhDszQ
```

DFs Consolidadas / Demonstração do Resultado Abrangente - (Reais Mil)

```http
GET https://www.rad.cvm.gov.br/ENET/frmDemonstracaoFinanceiraITR.aspx?Informacao=2&Demonstracao=5&Periodo=0&Grupo=DFs+Consolidadas&Quadro=Demonstra%c3%a7%c3%a3o+do+Resultado+Abrangente&NomeTipoDocumento=ITR&Empresa=PETRO RIO S.A.&DataReferencia=2022-09-30&Versao=1&CodTipoDocumento=3&NumeroSequencialDocumento=121259&NumeroSequencialRegistroCvm=2047&CodigoTipoInstituicao=1&Hash=s5XZ7sJHHMWDxgaVgx5bfhLSspwAaHc9JgSLQuhDszQ
```


DFs Consolidadas / Demonstração do Fluxo de Caixa - (Reais Mil) - Método Indireto

```http
GET https://www.rad.cvm.gov.br/ENET/frmDemonstracaoFinanceiraITR.aspx?Informacao=2&Demonstracao=99&Periodo=0&Grupo=DFs+Consolidadas&Quadro=Demonstra%c3%a7%c3%a3o+do+Fluxo+de+Caixa&NomeTipoDocumento=ITR&Empresa=PETRO RIO S.A.&DataReferencia=2022-09-30&Versao=1&CodTipoDocumento=3&NumeroSequencialDocumento=121259&NumeroSequencialRegistroCvm=2047&CodigoTipoInstituicao=1&Hash=s5XZ7sJHHMWDxgaVgx5bfhLSspwAaHc9JgSLQuhDszQ
```


DFs Consolidadas / Demonstração das Mutações do Patrimônio Líquido - (Reais Mil)

```http
GET https://www.rad.cvm.gov.br/ENET/frmDemonstracaoFinanceiraITR.aspx?Informacao=200&Demonstracao=8&Periodo=4|6&Grupo=DFs+Consolidadas&Quadro=Demonstra%c3%a7%c3%a3o+das+Muta%c3%a7%c3%b5es+do+Patrim%c3%b4nio+L%c3%adquido&NomeTipoDocumento=ITR&Empresa=PETRO RIO S.A.&DataReferencia=2022-09-30&Versao=1&CodTipoDocumento=3&NumeroSequencialDocumento=121259&NumeroSequencialRegistroCvm=2047&CodigoTipoInstituicao=1&Hash=s5XZ7sJHHMWDxgaVgx5bfhLSspwAaHc9JgSLQuhDszQ
```

DFs Consolidadas / Demonstração de Valor Adicionado - (Reais Mil)

```http
GET https://www.rad.cvm.gov.br/ENET/frmDemonstracaoFinanceiraITR.aspx?Informacao=2&Demonstracao=9&Periodo=0&Grupo=DFs+Consolidadas&Quadro=Demonstra%c3%a7%c3%a3o+de+Valor+Adicionado&NomeTipoDocumento=ITR&Empresa=PETRO RIO S.A.&DataReferencia=2022-09-30&Versao=1&CodTipoDocumento=3&NumeroSequencialDocumento=121259&NumeroSequencialRegistroCvm=2047&CodigoTipoInstituicao=1&Hash=s5XZ7sJHHMWDxgaVgx5bfhLSspwAaHc9JgSLQuhDszQ
```

<br>

### DFs Individuais

DFs Individuais / Balanço Patrimonial Ativo - (Reais Mil)

```http
GET https://www.rad.cvm.gov.br/ENET/frmDemonstracaoFinanceiraITR.aspx?Informacao=1&Demonstracao=2&Periodo=0&Grupo=DFs+Individuais&Quadro=Balanço+Patrimonial+Ativo&NomeTipoDocumento=ITR&Empresa=PETRO RIO S.A.&DataReferencia=2022-09-30&Versao=1&CodTipoDocumento=3&NumeroSequencialDocumento=121259&NumeroSequencialRegistroCvm=2047&CodigoTipoInstituicao=1&Hash=s5XZ7sJHHMWDxgaVgx5bfhLSspwAaHc9JgSLQuhDszQ
```

DFs Individuais / Balanço Patrimonial Passivo - (Reais Mil)

```http
GET https://www.rad.cvm.gov.br/ENET/frmDemonstracaoFinanceiraITR.aspx?Informacao=1&Demonstracao=3&Periodo=0&Grupo=DFs+Individuais&Quadro=Balanço+Patrimonial+Passivo&NomeTipoDocumento=ITR&Empresa=PETRO RIO S.A.&DataReferencia=2022-09-30&Versao=1&CodTipoDocumento=3&NumeroSequencialDocumento=121259&NumeroSequencialRegistroCvm=2047&CodigoTipoInstituicao=1&Hash=s5XZ7sJHHMWDxgaVgx5bfhLSspwAaHc9JgSLQuhDszQ
```

DFs Individuais / Demonstração do Resultado - (Reais Mil)

```http
GET https://www.rad.cvm.gov.br/ENET/frmDemonstracaoFinanceiraITR.aspx?Informacao=1&Demonstracao=4&Periodo=0&Grupo=DFs+Individuais&Quadro=Demonstração+do+Resultado&NomeTipoDocumento=ITR&Empresa=PETRO RIO S.A.&DataReferencia=2022-09-30&Versao=1&CodTipoDocumento=3&NumeroSequencialDocumento=121259&NumeroSequencialRegistroCvm=2047&CodigoTipoInstituicao=1&Hash=s5XZ7sJHHMWDxgaVgx5bfhLSspwAaHc9JgSLQuhDszQ
```

DFs Individuais / Demonstração do Resultado Abrangente - (Reais Mil)

```http
GET https://www.rad.cvm.gov.br/ENET/frmDemonstracaoFinanceiraITR.aspx?Informacao=1&Demonstracao=5&Periodo=0&Grupo=DFs+Individuais&Quadro=Demonstração+do+Resultado+Abrangente&NomeTipoDocumento=ITR&Empresa=PETRO RIO S.A.&DataReferencia=2022-09-30&Versao=1&CodTipoDocumento=3&NumeroSequencialDocumento=121259&NumeroSequencialRegistroCvm=2047&CodigoTipoInstituicao=1&Hash=s5XZ7sJHHMWDxgaVgx5bfhLSspwAaHc9JgSLQuhDszQ
```

DFs Individuais / Demonstração do Fluxo de Caixa - (Reais Mil) - Método Indireto

```http
GET https://www.rad.cvm.gov.br/ENET/frmDemonstracaoFinanceiraITR.aspx?Informacao=1&Demonstracao=99&Periodo=0&Grupo=DFs+Individuais&Quadro=Demonstração+do+Fluxo+de+Caixa&NomeTipoDocumento=ITR&Empresa=PETRO RIO S.A.&DataReferencia=2022-09-30&Versao=1&CodTipoDocumento=3&NumeroSequencialDocumento=121259&NumeroSequencialRegistroCvm=2047&CodigoTipoInstituicao=1&Hash=s5XZ7sJHHMWDxgaVgx5bfhLSspwAaHc9JgSLQuhDszQ
```

DFs Individuais / Demonstração das Mutações do Patrimônio Líquido - (Reais Mil)

```http
GET https://www.rad.cvm.gov.br/ENET/frmDemonstracaoFinanceiraITR.aspx?Informacao=100&Demonstracao=8&Periodo=4|6&Grupo=DFs+Individuais&Quadro=Demonstração+das+Mutações+do+Patrimônio+Líquido&NomeTipoDocumento=ITR&Empresa=PETRO RIO S.A.&DataReferencia=2022-09-30&Versao=1&CodTipoDocumento=3&NumeroSequencialDocumento=121259&NumeroSequencialRegistroCvm=2047&CodigoTipoInstituicao=1&Hash=s5XZ7sJHHMWDxgaVgx5bfhLSspwAaHc9JgSLQuhDszQ
```

DFs Individuais / Demonstração de Valor Adicionado - (Reais Mil)

```http
GET https://www.rad.cvm.gov.br/ENET/frmDemonstracaoFinanceiraITR.aspx?Informacao=1&Demonstracao=9&Periodo=0&Grupo=DFs+Individuais&Quadro=Demonstração+de+Valor+Adicionado&NomeTipoDocumento=ITR&Empresa=PETRO RIO S.A.&DataReferencia=2022-09-30&Versao=1&CodTipoDocumento=3&NumeroSequencialDocumento=121259&NumeroSequencialRegistroCvm=2047&CodigoTipoInstituicao=1&Hash=s5XZ7sJHHMWDxgaVgx5bfhLSspwAaHc9JgSLQuhDszQ
```
