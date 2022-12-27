import aiohttp
import asyncio
import pandas as pd
import rich
from io import StringIO
import fincode as fc 


url = 'https://dados.cvm.gov.br/dados/CIA_ABERTA/CAD/DADOS/cad_cia_aberta.csv'
filename = 'cad_cia_aberta.csv'
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'referrer': 'https://google.com',
    'Accept-Language': 'en-US,en;q=0.9',
    'Pragma': 'no-cache',
}
df = None

async def main():

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            global df
            #print("Status:", response.status)
            #print("Content-type:", response.headers['content-type'])
            csv_text = await response.text()
            #print("Body:", csv_text[:15], "...")
            csv_io = StringIO(csv_text)
            df = pd.read_csv(csv_io, sep=';', header=0, index_col=False)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())

#rich.print(df)

busca = df[
    (df['DENOM_SOCIAL'].str.contains('PETRO', na = False))
    & (df['SIT'].str.contains('ATIVO', na = False))
]


rich.print(busca[['CNPJ_CIA', 'DENOM_SOCIAL', 'CD_CVM', 'SIT']])
fc.ping()