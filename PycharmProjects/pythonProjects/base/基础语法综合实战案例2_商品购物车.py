class Goods:
    def __init__(self,name,price,number):
        self.name=name
        self.price=float(price)
        self.number=int(number)
    def __str__(self):
        return f"商品名称：{self.name},商品价格：{self.price},商品数量：{self.number}"
    def update(self,price,number):
        if price is not None:
            self.price = float(price)
        if number is not None:
            self.number = int(number)

class ShoppingCart:
    def __init__(self):
        self.shop_dict = {}
    def add(self):
        name = input("请输入商品名称：")
        if name in self.shop_dict:
            print("重复，重新输入")
        else:
            price = float(input("请输入商品价格："))
            number = int(input("请输入商品数量："))
            if price>=0 and number>0:
                goods = Goods(name, price, number)
                self.shop_dict[name] = goods
                print("成功")
    def edit(self):
        name = input("请输入要修改的商品名称：")
        if name not in self.shop_dict:
            print("该商品不存在！重新输入")
        else:
            price = float(input("请输入商品价格："))
            number = int(input("请输入商品数量："))
            if price >= 0 and number > 0:
                self.shop_dict[name].update(name,price)
                print("成功")
    def delete(self):
        name = input("请输入要删除的商品名称：")
        if name not in self.shop_dict:
            print("该商品不存在！重新输入")
        else:
            del self.shop_dict[name]
            print("成功")
    def show(self):
        for i in self.shop_dict:
            print(self.shop_dict[i])

    def run(self):
        while True:
            try:
                print("""
                    1.添加购物车
                    2.修改购物车
                    3.删除购物车  
                    4.查询购物车
                    5.退出购物车
                """)
                shop = int(input("请输入操作选项(1-5)"))
                match shop:
                    case 1:
                        self.add()
                    case 2:
                        self.edit()
                    case 3:
                        self.delete()
                    case 4:
                        self.show()
                    case 5:
                        print("已退出！")
                        break
                    case _:
                        print("错误选项")
            except Exception:
                print("出现错误！请仔细检查重新输入！")
if __name__ == '__main__':
    shop1 = ShoppingCart()
    shop1.run()