def init(context):
    logger.info("init")
    context.s1 = "000001.XSHE"
    update_universe(context.s1)
    context.fired = False


def before_trading(context):
    pass


def handle_bar(context, bar_dict):
    if not context.fired:
        # order_percent���Ҵ���1��������ù�Ʊ����ʹ��ռ��Ͷ����ϵ�100%
        order_percent(context.s1, 1)
        context.fired = True