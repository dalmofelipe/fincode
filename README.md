# CVM

Consultar código CVM por letra inicial do nome da CIA

https://cvmweb.cvm.gov.br/SWB/Sistemas/SCW/CPublica/CiaAb/FormBuscaCiaAbOrdAlf.aspx?LetraInicial=**P**
    
Código CVM da Petro Rio 22187

### Requisição de consulta de ITRs da Petrobras

```json

POST https://www.rad.cvm.gov.br/ENET/frmConsultaExternaCVM.aspx/ListarDocumentos HTTP/1.1
Content-type: application/json

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

    

- Requisição POST no RAD

```json
POST https://www.rad.cvm.gov.br/ENET/frmConsultaExternaCVM.aspx/ListarDocumentos HTTP/1.1
Content-type: application/json

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

RESPONSE

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

PARSER da response, obtendo os códigos de documentos e datas, contidos na função `OpenPopUpVer`

```md
02218-7$&PETRO RIO S.A.$&ITR - Informações Trimestrais$& - $&<spanOrder></spanOrder> - $&<spanOrder>20220331</spanOrder> 31/03/2022$&<spanOrder>20220504</spanOrder> 04/05/2022 18:59$&Ativo$&1$&AP$&<i class='fi-page-search' id='VisualizarDocumento' style='font-size: 18px;cursor:pointer;color:#0C7766;' onclick=

**OpenPopUpVer('frmGerenciaPaginaFRE.aspx?NumeroSequencialDocumento=114282&CodigoTipoInstituicao=1')**

 title='Visualizar o Documento'> </i><i class='fi-download' style='font-size: 18px;cursor:pointer;color:#0C7766;' title='Download' onclick=OpenDownloadDocumentos('114282','1','022187ITR310320220100114282-66','ITR')> </i><i class='fi-info' style='font-size: 18px;cursor:pointer;color:#696969;' title='Documento não possui local de publicação.'> </i><i class='fi-clipboard-notes' style='font-size: 18px;cursor:pointer;color:#0C7766;' title='Exibir Protocolo de Entrega' onclick='exibirProtocoloPDF(114282, \"ENET\")'</i>

$&$&&*02218-7$&PETRO RIO S.A.$&ITR - Informações Trimestrais$& - $&<spanOrder></spanOrder> - $&<spanOrder>20220630</spanOrder> 30/06/2022$&<spanOrder>20220803</spanOrder> 03/08/2022 19:38$&Ativo$&1$&AP$&<i class='fi-page-search' id='VisualizarDocumento' style='font-size: 18px;cursor:pointer;color:#0C7766;' onclick=

OpenPopUpVer('frmGerenciaPaginaFRE.aspx?NumeroSequencialDocumento=119205&CodigoTipoInstituicao=1')

 title='Visualizar o Documento'> </i><i class='fi-download' style='font-size: 18px;cursor:pointer;color:#0C7766;' title='Download' onclick=OpenDownloadDocumentos('119205','1','022187ITR300620220100119205-77','ITR')> </i><i class='fi-info' style='font-size: 18px;cursor:pointer;color:#696969;' title='Documento não possui local de publicação.'> </i><i class='fi-clipboard-notes' style='font-size: 18px;cursor:pointer;color:#0C7766;' title='Exibir Protocolo de Entrega' onclick='exibirProtocoloPDF(119205, \"ENET\")'</i>

$&$&&*02218-7$&PETRO RIO S.A.$&ITR - Informações Trimestrais$& - $&<spanOrder></spanOrder> - $&<spanOrder>20220930</spanOrder> 30/09/2022$&<spanOrder>20221031</spanOrder> 31/10/2022 19:25$&Ativo$&1$&AP$&<i class='fi-page-search' id='VisualizarDocumento' style='font-size: 18px;cursor:pointer;color:#0C7766;' onclick=

OpenPopUpVer('frmGerenciaPaginaFRE.aspx?NumeroSequencialDocumento=121259&CodigoTipoInstituicao=1')

 title='Visualizar o Documento'> </i><i class='fi-download' style='font-size: 18px;cursor:pointer;color:#0C7766;' title='Download' onclick=OpenDownloadDocumentos('121259','1','022187ITR300920220100121259-72','ITR')> </i><i class='fi-info' style='font-size: 18px;cursor:pointer;color:#696969;' title='Documento não possui local de publicação.'> </i><i class='fi-clipboard-notes' style='font-size: 18px;cursor:pointer;color:#0C7766;' title='Exibir Protocolo de Entrega' onclick='exibirProtocoloPDF(121259, \"ENET\")'</i>$&$&&*
```

Informações extraídas:

| Data | Num Doc | Link completo |
| --- | --- | --- |
| 31/03/2022 | 114282 | https://www.rad.cvm.gov.br/ENET/frmGerenciaPaginaFRE.aspx?NumeroSequencialDocumento=114282&CodigoTipoInstituicao=1 |
| 30/06/2022 | 119205 | https://www.rad.cvm.gov.br/ENET/frmGerenciaPaginaFRE.aspx?NumeroSequencialDocumento=119205&CodigoTipoInstituicao=1 |
| 30/09/2022 | 121259 | https://www.rad.cvm.gov.br/ENET/frmGerenciaPaginaFRE.aspx?NumeroSequencialDocumento=121259&CodigoTipoInstituicao=1 |


- LINK para visualizar o documento no sistema RAD. O código acima pode ser obtido pela reposta da consulta

https://www.rad.cvm.gov.br/ENET/frmGerenciaPaginaFRE.aspx?NumeroSequencialDocumento=**121259**&CodigoTipoInstituicao=1

Link completo do demonstrativo de resultados acima. Importe a HASH gerado por ele.

https://www.rad.cvm.gov.br/ENET/frmDemonstracaoFinanceiraITR.aspx?Informacao=2&Demonstracao=4&Periodo=0&Grupo=DFs+Consolidadas&Quadro=Demonstração+do+Resultado&NomeTipoDocumento=ITR&Empresa=PETRO RIO S.A.&DataReferencia=2022-09-30&Versao=1&CodTipoDocumento=3&NumeroSequencialDocumento=121259&NumeroSequencialRegistroCvm=2047&CodigoTipoInstituicao=1&Hash=aMlOcgOPWDmi3B1uJhqbZYeSVnmJ1SLUlJ2d8RfVs

Hash=aMlOcgOPWDmi3B1uJhqbZYeSVnmJ1SLUlJ2d8RfVs

| Balanço Patrimonial Ativo |  |
| --- | --- |
| Balanço Patrimonial Passivo |  |
| Demonstração do Resultado |  |
| Demonstração do Resultado Abrangente |  |
| Demonstração do Fluxo de Caixa |  |
| Demonstração das Mutações do Patrimônio Líquido |  |
| Demonstração de Valor Adicionado |  |






ROE = (Lucro/Prejuízo Consolidado do Período / Patrimônio Líquido Consolidado) * 100

46.236.000 / 374.105.000 = 12,3590%
31.224.000 / 389.581.000 = 8,0147%




- URL para **DOWNLOAD** do documento acima, dados obtidos dos parâmetros da função **OpenDownload**

https://www.rad.cvm.gov.br/ENET/frmDownloadDocumento.aspx?Tela=ext&numSequencia=**121328**&numVersao=**1**&numProtocolo=**009512ITR300920220100121328**&descTipo=**ITR**&CodigoInstituicao=**1**
