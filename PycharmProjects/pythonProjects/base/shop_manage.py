shop_dict={}
while True:
    print("""
        1.添加购物车
        2.修改购物车
        3.删除购物车  
        4.查询购物车
        5.退出购物车
    """)
    shop=int(input("请输入操作选项(1-5)"))
    match shop :
        case 1:
            name=input("请输入商品名称：")
            price=input("请输入商品价格：")
            number=input("请输入商品数量：")
            if name in shop_dict:
                print("重复，重新输入")
            else:
                shop_dict[name]={"price":price,"number":number}
        case 2:
            name = input("请输入要修改的商品名称：")
            if name not in shop_dict:
                print("该商品不存在！重新输入")
            else:
                price = input("请输入要修改的商品价格：")
                number = input("请输入要修改的商品数量：")
                shop_dict[name]={"price":price,"number":number}
        case 3:
            name = input("请输入要删除的商品名称：")
            if name not in shop_dict:
                print("该商品不存在！重新输入")
            else:
                del shop_dict[name]
        case 4:
            for i in shop_dict.keys():
                print(f"name:{i},price:{shop_dict[i]['price']},number:{shop_dict[i]['number']}")
        case 5:
            print("已退出！")
            break
        case _:
            print("错误选项")