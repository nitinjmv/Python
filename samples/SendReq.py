import urllib3 
import json

ec2 = {
    "dev": {
        "running_servers": [
            {
                "1111": "eee1111"
            },
            {
                "33333": "eee3333"
            }
        ],
        "stopped_servers": [
            {
                "1111": "eee1111"
            },
            {
                "33333": "eee3333"
            }
        ]
    },
    "qa": {
        "running_servers": [
           {
                "1111": "eee1111"
            },
            {
                "33333": "eee3333"
            }
        ],
        "stopped_servers": [
            {
                "33333": "eee3333"
            }
        ]
    },
    "prd": {
        "running_servers": [
            {
                "33333": "eee3333"
            }
        ],
        "stopped_servers": [
            {
                "33333": "eee3333"
            }
        ]
    }
}

def getCiaraURL(env):
    if env == "dev":
        return "ciara_dev"
    elif env == "qa":
        return "ciara_qa"
    elif env == "prd":
        return "ciara_prd"
    

def startStopServer(serverStatus, server):
    if serverStatus ==  "running_servers":
        print("stopping {}".format(server))
    if serverStatus == "stopped_servers":
        print("ternimating {}".format(server))

def sendCiaraReq(id):
    print(id)


for k, v in ec2.items():
    ciara_url = getCiaraURL(k)
    for k1, v1 in v.items():
        for id in v1:
            startStopServer(k1, id)
            sendCiaraReq();
        





# http = urllib3.PoolManager()

# data = json.dumps({"status": "started"})

# response = http.request('POST', "http://localhost:8081/status", 
#                         headers={'Content-Type': 'application/json'},
#                         body = data)

# print(response.status) 