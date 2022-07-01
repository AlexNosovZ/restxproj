import requests
uri = 'http://127.0.0.1:5000/echo'
datamsg = {'message':'test1'}
def test_myapp():
    ret =  requests.post(uri, data=datamsg)
    str1 = ret.text
    print(str1.strip())
    assert ('"echo ' + datamsg['message'] + '"') == str1.strip()

