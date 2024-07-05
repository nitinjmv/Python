import urllib3 
import json

running_list = { "33333": {"eee3333", "dev"}, "1111": {"eee1111", "stg"} }
stopped_list = { "4444": {"e4444", "stg"}, "5555": {"e555555", "dev"} }

def getCiaraURL(env):
    if env == "dev":
        return "ciara_dev"
    elif env == "qa":
        return "ciara_qa"
    elif env == "prd":
        return "ciara_prd"
    

def stopServer(id):
    print()

def sendCiaraReq(id, v):
    print()


for k, v in running_list.items():
    stopServer(k);
    print(k, type(v))
    sendCiaraReq(k, v);

        





# http = urllib3.PoolManager()

# data = json.dumps({"status": "started"})

# response = http.request('POST', "http://localhost:8081/status", 
#                         headers={'Content-Type': 'application/json'},
#                         body = data)

# print(response.status) 