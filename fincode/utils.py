
from abc import ABC


URL_RAD_SEARCH = 'https://www.rad.cvm.gov.br/ENET/frmConsultaExternaCVM.aspx/ListarDocumentos'
URL_DADOS_CADASTRAIS = 'https://dados.cvm.gov.br/dados/CIA_ABERTA/CAD/DADOS/cad_cia_aberta.csv'
USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.91 Safari/537.36',
    'Mozilla/5.0 (iPad; U; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/50.0.125 Chrome/44.0.2403.125 Safari/537.36',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; SLCC2; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E)',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; MAARJS; rv:11.0) like Gecko',
    'Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-N900T Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 8_4 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) GSA/7.0.55539 Mobile/12H143 Safari/600.1.4'
]
HEADERS = {
    'user-agent': "",
    'referrer': 'https://google.com',
    'Accept-Language': 'en-US,en;q=0.9',
    'Pragma': 'no-cache',
}
OBJ_SEARCH = {
    "dataDe": '01/01/2022',
    "dataAte": '30/12/2022',
    "empresa": ',022187',
    "setorAtividade": '-1',
    "categoriaEmissor": '-1',
    "situacaoEmissor": '-1',
    "tipoParticipante": '-1',
    "dataReferencia": '',
    "categoria": 'EST_3',
    "periodo": '2',
    "horaIni": '',
    "horaFim": '',
    "palavraChave": '',
    "ultimaDtRef": 'false',
    "tipoEmpresa": '0',
    "token": '',
    "versaoCaptcha": ''
}
RGX_PARSER_DADOS_EMPRESAS = r'(\$&[a-zA-Z1-9.\- ]+\$&ITR|\d{2}/\d{2}/\d{4}|NumeroSequencialDocumento=\d+|CodigoTipoInstituicao=\d+)'


class ItrDocs:

    DADOS_DA_EMPRESA:int = 1
    DFS_INDIVIDUAIS:int = 78
    DFS_CONSOLIDADAS:int = 135
