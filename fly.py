class PaymentService:

    def __init__(self, live=True, name=None, **kwargs):
        self.live = live
        self.name = name

    def __str__(self):
        return self.name

    @classmethod
    def get_service(cls, name, **kwargs):
        name = name.lower()
        print('name===>', name)
        for klass in cls.__subclasses__():
            print('klass===>', klass)
            if klass.__name__.lower() == name:
                return klass(**kwargs)
        print("无效的支付网关 %s" % name)

    @classmethod
    def from_gateway(cls, gateway, **kwargs):
        return cls.get_service(gateway.type, **dict(gateway.extra or (), **kwargs))

    def pay_v2(self, recharge, payee, channel, **kwargs):
        """
        credential -> {
            'type': payee.pay_method,
        }
        :param recharge:
        :param payee:
        :param channel:
        :param kwargs:
        :return:
        """
        user = recharge.user
        data = self.prepare_charge(recharge=recharge, payee=payee, channel=channel, **kwargs)
        RechargeValidator.add_fail_times(user_id=user.id, recharge=recharge, times=1)
        credential = self.platform_pay_v2(recharge=recharge,
                                          channel=channel,
                                          payload=data)
        logger.info('payment.pay',
                    data=data,
                    provider=self.__class__.__name__,
                    user=user,
                    amount=recharge.amount,
                    credential=credential,
                    channel=channel)
        RechargeValidator.add_fail_times(user_id=user.id, recharge=recharge, times=-1)

    def platform_pay_v2(self, recharge, channel, payload, **kwargs):
        """
        :param recharge: 支付对象
        :param channel: 渠道对象
        :param payload: 支付所需要的参数
        :return:
        """
        raise exceptions.ValidationError("v2 not supported")


class LeiaZf(PaymentService):

    def __str__(self):
        return 'leiazf'

    def __init__(self,
                 mch_id='12345',
                 pay_api='http://leiazf',
                 key='goi3npogijapowi3jmfs',
                 sign_type='md5',
                 notify_url='localhost/notify',
                 callback_url='localhost/callback',
                 type='leiazf',
                 extra={},
                 **kwargs):
        self.mch_id = mch_id
        self.sign_type = sign_type
        self.pay_api = pay_api
        self.api_key = key
        self.notify_url = notify_url
        self.callback_url = callback_url
        self.type = type
        self.extra = extra
        super(LeiaZf, self).__init__(**kwargs)

    def platform_pay_v2(self, recharge, channel, payload, **kwargs):
        """
        :param recharge: 支付对象
        :param channel: 渠道对象
        :param payload: 支付所需要的参数
        :return:
        """
        raise exceptions.ValidationError("v2 not supported")


if __name__ == '__main__':
    gateway = LeiaZf()
    payment = PaymentService.from_gateway(gateway)
    print(payment.pay_v2())
