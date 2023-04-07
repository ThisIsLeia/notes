# 需求：在亞博代理後台 財務報表 統計存款
# 狀態：接口已開好

# 觀察接口
'''
request 打接口後
返回 data 字段之每個 {} 都是 object
每個 {} 裡面都是 同個 user 的各種存款管道及金額
目標是要統計總存款
'''

from itertools import filterfalse


@route(bp, '/i/flow')
@limiter.limit('60/minute')
@my_filters
@paginate(10)
def flow(filters):
    user = g.user
    filters['user'] = user
    _type = filters.pop('type', 'deposit')    # 给定键 key 所对应的值 = 字典.pop(要删除的键, 当键 key 不存在时返回的值) 
    if _type == 'disbursement':
        filters.pop('user')
        filters['user_id_in'] = universal_agent_relations.get_agent_relation_ids(agent_id=g.user.id)
    filters = account_logs.parse_filters(_type, filters)
    return account_logs.get_account_logs(_type, filters)

def deposit_amount(date, user_id):
    from spinach.services import recharges
    filters = {'created_date': date, 'user_id': user_id}
    recharge_list = recharges.search(filters)
    result = {}
    amount_total = 0
    for r in recharge_list:
        if r.settle:
            result[r.channel_alias] = r.resilt.get(r.channel_alias, 0) + r.amount_paid
            amount_total += r.amount_paid
        result['deposit_total'] = amount_total
    return result