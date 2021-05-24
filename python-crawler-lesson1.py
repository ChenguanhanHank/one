import requests
r = requests.get("http://httpbin.org/get")
r = requests.head("http://httpbin.org/get")
r = requests.post('http://httpbin.org/post', data ={'key':'value'})
r= requests.put("http://httpbin.org/put")
r = requests. delete("http://httpbin.org/delete")
r= requests.options("http://httpbin.org/get")