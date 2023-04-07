import requests as requests


class APIError(Exception):
    status_code = 400
    type = 'invalid_request_error'
    message = ''
    code = '400'

    def __init__(self, msg=None):
        if msg is None:
            msg = self.message
        if 'Failed to establish a new connection' in msg or 'Read timed out' in msg:
            msg = '抱歉，银行卡获取失败，请更换金额或渠道重试。'
        self.message = msg
        super(APIError, self).__init__(self.message)


class ChannelConnectionError(APIError):
    # 如果沒有傳錯誤訊息進來 基類的__init__才會是這裡的 渠道通讯异常
    # 外面傳進來的錯誤訊息 會設置基類的__init__
    code = 40012
    message = "渠道通讯异常。"
    type = 'channel_connection_error'


if __name__ == '__main__':
    # try:
    #     resp = requests.get('http://api.79j71112233c.com')
    #     print(resp)
    # except Exception as e:
    #     print('--->', e)
    #     print('===>', ChannelConnectionError(str(e)))

    e = '2257'
    print('--->', e)
    print('===>', ChannelConnectionError(str(e)))

# {
#     "code": 40083,
#     "message": "code: -1, msg: ChannelRespCodeError: ClientError status: 404 url: https://bopay.iyes.dev/payments/orders fail_msg: {\"code\":404,\"message\":\"\u627e\u4e0d\u5230\u5bf9\u8c61\",\"err\":\"\u627e\u4e0d\u5230\u5bf9\u8c61\"}",
#     "payload": {
#         "failure_code": 40083,
#         "failure_msg": "code: -1, msg: ChannelRespCodeError: ClientError status: 404 url: https://bopay.iyes.dev/payments/orders fail_msg: {\"code\":404,\"message\":\"\u627e\u4e0d\u5230\u5bf9\u8c61\",\"err\":\"\u627e\u4e0d\u5230\u5bf9\u8c61\"}"
#     },
#     "type": "response_code_fail"
# }
