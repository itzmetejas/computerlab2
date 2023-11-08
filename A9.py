import http.client , urllib.request,urllib.parse
key = ' ' # copy the write API key

t=int(22)

while True:
    t=t+1
    print ("temperature",t)
    params=urllib.parse.urlencode({'field1':t,'key':key})
    headers={"Content-type":"application/x-www-form-urlencoded","Accept":"text/plain"}
    con=http.client.HTTPConnection("api.thingspeak.com")
    con.request("POST","/update",params,headers)
    response=con.getresponse()
    print (response.status,response.reason)
    data=response.read()
    con.close()
