import ansibleawx
import pprint

API_URL = "http://192.168.1.201/api/v2"

#client = ansibleawx.Api("Foofoo", "***********", api_url=API_URL)
client = ansibleawx.Api("hogehoge", "***********", api_url=API_URL)

#response = client.get_inventories()
# print(response)

response = client.get_jobs()
print('get_jobs = ')
pprint.pprint(response)

response = client.get_job_stdout(id=1959, resp_format='json')
print('get_job_stdout = ')
pprint.pprint(response)
