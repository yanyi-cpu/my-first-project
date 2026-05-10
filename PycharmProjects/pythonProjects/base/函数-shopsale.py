def res (*args,coupon,score,express):
    """
    :param args:商品信息（name,price,number）(...)
    :param coupon:优惠卷
    :param score:积分
    :param express:运输费用
    :return:
    """
    total_list=[i[1]*i[2] for i in args]
    total=sum(total_list)
    if total>=coupon and total>=5000:
        total=total-coupon
    if total>=5000:
        if score>total*100:
            score=score-total*100
            total=0
        else:
            total=total-score//100
            score=score%100
    total+=express
    print(total,score)
res(("name1",288,23),coupon=500,score=800032,express=34)

