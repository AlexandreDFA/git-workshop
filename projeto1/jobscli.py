import typer
import requests

url = "https://api.itjobs.pt/job"
api_key = "22f572f4c8057d196327a8ce71c85bd7"
headers = {
    'User-Agent': ''
}
payload = {}

app=typer.Typer()

#e)Para cada uma das funcionalidades (a), (b) e (d) deve poder exportar para CSV a informacao com os seguintes campo:
#titulo;empresa;descricao;data_de_publicacao;salario;localizacao.
def cria_csv(dados):
    df=pd.DataFrame(dados['results'])
    df.to_csv('a.csv', index=False)


#a)listar os n trabalhos mais recentes
#python jobscli.py top 10
@app.command()
def top(n: int, csv: bool=False):
    url_top = f"{url}/list.json?api_key={api_key}&limit={n}"
    response = requests.request("GET",url_top, headers=headers, data=payload)
    res=response.json()
    print(res.get('limit'))
    print(res['results'])
    if csv:
        cria_csv(res)

#b)Listar todos os trabalhos do tipo full-time, publicados por uma determinada empresa, numa determinada localidade e determinado numero.
#python jobscli.py search Braga EmpresaX 4
@app.command()
def search(localidade: str, empresa: str, limit: int):
    q = f"{localidade},{empresa}"
    url_search = f"{url}/search.json?api_key={api_key}&types=1&q={q}&limit={limit}"
    response = requests.get(url_search, headers=headers)
    res = response.json()
    print(res)

    
@app.command()
def a(n: int):
    for _ in range(n):
        print(1)

app()