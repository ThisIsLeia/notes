import requests

tencent_errors = {
    'OK': '验证通过',
    'cmd no match': '验证码系统命令号不匹配',
    'user code len error': '验证码长度不匹配',
    'uin no match': '号码不匹配',
    'captcha no match': '验证码答案不匹配/Randstr参数不匹配',
    'seq redirect': '重定向验证',
    'verify timeout': '验证码签名超时',
    'opt no vcode': '操作使用pt免验证码校验错误',
    'Sequnce repeat': '验证码签名重放',
    'diff': '差别，验证错误',
    'Sequnce invalid': '验证码签名序列',
    'captcha type not match': '验证码类型与拉取时不一致',
    'Cookie invalid': '验证码cookie信息不合法',
    'verify type error': '验证类型错误',
    'verify ip no match': 'ip不匹配',
    'invalid pkg': '非法请求包',
    'decrypt fail': '验证码签名解密失败',
    'bad visitor': '策略拦截',
    'appid no match': '验证码强校验appid错误',
    'system busy': '系统内部错误',
    'param err': 'AppSecretKey参数校验错误'
}


class CaptchaBase:
    TIMEOUT = 30

    @property
    def _client(self):
        s = requests.Session()
        return s

    @staticmethod
    def parse_resp(resp):
        try:
            return resp.json()
        except ValueError:
            print('error.tencent.verify')
            raise print("无效的json数据")

    def verify(self, *args):
        """第三方校验請求"""

    def _request(self, url, params=None, data=None, json=None, method='GET'):
        print('verify_ticket.request', url, params)
        try:
            # 设置超时时间为30秒
            resp = self._client.request(method, url, params=params, data=data, json=json,
                                        timeout=self.TIMEOUT)
            print('resp===>', resp.content)
        except ConnectionError as e:
            raise print(str(e), payload={
                'failure_msg': str(e),
                'failure_code': 'network'
            })
        

        payload = self.parse_resp(resp)
        print('captcha.response',url, payload)
        return self.verify_payload(payload, params=params)

    def verify_payload(self, payload, params, **kwargs):
        """第三方校驗結果"""



class TencentCaptcha(CaptchaBase):
    URL = 'https://ssl.captcha.qq.com/ticket/verify'
    # URL = 'https://captcha.tencentcloudapi.com/ticket/verify'
    TIMEOUT = 30
    EXPIRE = 60 * 5

    @staticmethod
    def verify_params(params):
        # schema = Schema({Required('ticket'): str, Required('rand_str'): str})
        # try:
        #     schema(params)
        # except Invalid as e:
        #     raise ValidationError("%s (path %s)" % (e.msg, '.'.join(
        #         [str(x) for x in e.path])))

        return params

    def verify(self, params, **kwargs):
        """第三方校验請求"""
        # params -> {"ticket": "terror_1006_2069578364_1682046231", "rand_str": "@3z2w25eh4ov"}
        user_ip = kwargs.get('user_ip')
        verified = self.verify_params(params)
        params = {'Ticket': verified['ticket'], 'Randstr': verified['rand_str'],
                  'UserIP': user_ip, 'aid': "2069578364",
                  'AppSecretKey': "0SWsu5yRf6aDLgzGT0R1SaQ**"}

        return self._request(url=self.URL, method='GET', params=params)

    def verify_payload(self, payload, params, *args):
        """
        {
            "response": "100",  # required
            "evil_level": "0",  # optional
            "err_msg": "SecretKeyCheck Error"  # optional
        }
        """
        code = payload.get('response')
        err_msg = payload.get('err_msg')
        if code == '1':
            key = self.gen_hash_key(params)
            return key, 'OK'
        elif code == '100':
            raise print('AppSecretKey参数校验错误')
        else:
            raise print(tencent_errors.get(err_msg, '不明错误'))

    

if __name__ == '__main__':
    
    params = {"ticket": "terror_1006_2069578364_1682069347", "rand_str": "@910a3q32hmm"}
    
    user_ip = '18.163.217.66'
    s = TencentCaptcha()
    result, msg = s.verify(params, user_ip=user_ip)
    print({'result': result, 'msg': msg})