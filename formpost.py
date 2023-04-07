host = 'http://0.0.0.0:5001/payment/redirect'

data = {
       "amount": "200.00",
                "apiVersion": "2",
                "asyncUrl": "https://d10e-18-163-217-66.ap.ngrok.io/payment/zfthv2/notify",
                "attach": "",
                "merchno": "2ae7ab5a64",
                "orderId": "12303311449017270340637",
                "payType": "1",
                "post_url": "https://api.zftapple.com/api/order/placeOrder",
                "requestCurrency": 1,
                "requestTime": "20230331224901",
                "sign": "7a39cb5f2cf1d855b559ced9ab430bfd",
                "syncUrl": "https://d10e-18-163-217-66.ap.ngrok.io/payment/zfthv2/callback"
        }

if __name__ == '__main__':
    api = '?'+'&'.join([f'{k}={v}' for k, v in data.items()])
    url = host + api
    print('url:',  url)