#!/bin/bash python3
import pandas as pd

import fincode as fc


DATA = "02218-7$&PETRO RIO S.A.$&ITR - Informações Trimestrais$& - $&<spanOrder></spanOrder> - $&<spanOrder>20220331</spanOrder> 31/03/2022$&<spanOrder>20220504</spanOrder> 04/05/2022 18:59$&Ativo$&1$&AP$&<i class='fi-page-search' id='VisualizarDocumento' style='font-size: 18px;cursor:pointer;color:#0C7766;' onclick=OpenPopUpVer('frmGerenciaPaginaFRE.aspx?NumeroSequencialDocumento=114282&CodigoTipoInstituicao=1') title='Visualizar o Documento'> </i><i class='fi-download' style='font-size: 18px;cursor:pointer;color:#0C7766;' title='Download' onclick=OpenDownloadDocumentos('114282','1','022187ITR310320220100114282-66','ITR')> </i><i class='fi-info' style='font-size: 18px;cursor:pointer;color:#696969;' title='Documento não possui local de publicação.'> </i><i class='fi-clipboard-notes' style='font-size: 18px;cursor:pointer;color:#0C7766;' title='Exibir Protocolo de Entrega' onclick='exibirProtocoloPDF(114282, \"ENET\")'</i>$&$&&*02218-7$&PETRO RIO S.A.$&ITR - Informações Trimestrais$& - $&<spanOrder></spanOrder> - $&<spanOrder>20220630</spanOrder> 30/06/2022$&<spanOrder>20220803</spanOrder> 03/08/2022 19:38$&Ativo$&1$&AP$&<i class='fi-page-search' id='VisualizarDocumento' style='font-size: 18px;cursor:pointer;color:#0C7766;' onclick=OpenPopUpVer('frmGerenciaPaginaFRE.aspx?NumeroSequencialDocumento=119205&CodigoTipoInstituicao=1') title='Visualizar o Documento'> </i><i class='fi-download' style='font-size: 18px;cursor:pointer;color:#0C7766;' title='Download' onclick=OpenDownloadDocumentos('119205','1','022187ITR300620220100119205-77','ITR')> </i><i class='fi-info' style='font-size: 18px;cursor:pointer;color:#696969;' title='Documento não possui local de publicação.'> </i><i class='fi-clipboard-notes' style='font-size: 18px;cursor:pointer;color:#0C7766;' title='Exibir Protocolo de Entrega' onclick='exibirProtocoloPDF(119205, \"ENET\")'</i>$&$&&*02218-7$&PETRO RIO S.A.$&ITR - Informações Trimestrais$& - $&<spanOrder></spanOrder> - $&<spanOrder>20220930</spanOrder> 30/09/2022$&<spanOrder>20221031</spanOrder> 31/10/2022 19:25$&Ativo$&1$&AP$&<i class='fi-page-search' id='VisualizarDocumento' style='font-size: 18px;cursor:pointer;color:#0C7766;' onclick=OpenPopUpVer('frmGerenciaPaginaFRE.aspx?NumeroSequencialDocumento=121259&CodigoTipoInstituicao=1') title='Visualizar o Documento'> </i><i class='fi-download' style='font-size: 18px;cursor:pointer;color:#0C7766;' title='Download' onclick=OpenDownloadDocumentos('121259','1','022187ITR300920220100121259-72','ITR')> </i><i class='fi-info' style='font-size: 18px;cursor:pointer;color:#696969;' title='Documento não possui local de publicação.'> </i><i class='fi-clipboard-notes' style='font-size: 18px;cursor:pointer;color:#0C7766;' title='Exibir Protocolo de Entrega' onclick='exibirProtocoloPDF(121259, \"ENET\")'</i>$&$&&*"


def test_get_data_companies():
    result = fc.parser_data_companies(DATA)
    # o resultado deve ser uma lista com 3 documentos
    assert isinstance(result, pd.DataFrame) and len(result.index) == 3
