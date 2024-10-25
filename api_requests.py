import requests

url = "https://transparencia.sns.gov.pt/api/explore/v2.1/catalog/datasets?limit=10&offset=0"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

res=response.json()
print(res["total_count"])

datasets=res["results"]
dic={}
for dataset in datasets:
    dic[dataset["dataset_id"]]=dataset["has_records"]
print(dic)

all_results = []
all_results.extend(res.get('results', []))

