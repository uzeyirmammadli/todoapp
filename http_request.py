import http.client

import json

#
# host = "api.sendgrid.com"
#
# conn = http.client.HTTPSConnection(host)
#
# conn.request(
#     "POST", "/v3/mail/send", headers={"Host": host, "Authorization": "sehv_api_key"}
# )
#
# response = conn.getresponse()
#
# print(response.status, response.reason)

host = "localhost:5000"

conn = http.client.HTTPConnection(host)

conn.request("GET", "/api/data", headers={"Host": host})

resp = conn.getresponse()

print(resp.status, resp.reason)

data = resp.read()
decoded_data = json.loads(data.decode("utf-8"))

print(decoded_data["name"])

conn.close()
