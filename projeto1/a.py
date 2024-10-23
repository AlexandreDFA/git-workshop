import sys
import requests
import json

# Função para realizar a busca dos trabalhos
def search_jobs(location, company, num_jobs):
    # Substitua 'YOUR_API_KEY' pela sua chave de API obtida no ITJobs
    api_key = '22f572f4c8057d196327a8ce71c85bd7'
    base_url = 'https://api.itjobs.pt/job'

    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json',
        'User-Agent': 'PostmanRuntime/7.42.0'
    }

    # Parâmetros da busca
    params = {
        'location': location,
        'company': company,
        'job_type': 'full-time',  # Somente trabalhos full-time
        'limit': num_jobs  # Limita o número de resultados
    }

    url = f"{base_url}/list.json?api_key={api_key}"

    # Fazer a requisição GET
    response = requests.get(url, headers=headers, params=params)

    # Verificar o status da requisição
    if response.status_code == 200:
        # Retorna o resultado como JSON
        return response.json()
    else:
        print(f'Erro: {response.status_code}')
        return []

# Função principal que recebe argumentos da linha de comando
def main():
    # Verificar se os argumentos estão corretos
    if len(sys.argv) != 4:
        print("Uso: python jobscli.py <localidade> <empresa> <numero_de_trabalhos>")
        sys.exit(1)

    # Pegar os argumentos da linha de comando
    location = sys.argv[1]
    company = sys.argv[2]
    num_jobs = int(sys.argv[3])

    # Chamar a função de busca de trabalhos
    jobs = search_jobs(location, company, num_jobs)

    # Escrever o resultado em formato JSON
    print(json.dumps(jobs, indent=4))

if __name__ == "__main__":
    main()
