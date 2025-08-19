# 02.封装
# 封装
# 将数据和方法捆绑在对象内部，仅通过暴露的接口与外界交互，保护数据安全并简化使用。
#
# 案例解析
# 第一步：将内容封装到类中，并且实例化对象
#
# class Foo:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def detail(self):
#         print(self.name)
#         print(self.age)
#
# obj1 = Foo('xiaohong',18)
# obj2 = Foo('xiaoming',16)
# 第二步：通过对象调用被封装的内容
#
# class Foo:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def detail(self):
#         print(self.name)
#         print(self.age)
#
# obj1 = Foo('chensong',18)
# obj2 = Foo('aaron',16)
#
# # 通过对象直接调用被封装的内容
# print(obj1.name)
# print(obj2.age)
#
# # 通过 self 间接调用被封装的内容
# obj1.detail()
# obj2.detail()
# 案例一：摆放家具
# 需求
#
# 房子（House）有户型、总面积和家具名称列表
# 家具（HouseItem）有名字和占地面积，其中
# 床（bed）占地 4 平米
# 衣柜（chest）占地 2 平米
# 餐桌（table） 占地 1.5 平米
# 将以上三件家具添加到房子中
# 打印房子时，要求输出：户型、总面积、剩余面积、家具名称列表
# img-摆放家具类图
#
# 剩余面积
#
# 在创建房子对象时，定义一个 剩余面积的属性，初始值和总面积相等
# 当调用 add_item 方法，向房间 添加家具 时，让 剩余面积 -= 家具面积
# 思考：应该先开发哪一个类？家具类
#
# 家具简单
# 房子要使用到家具，被使用的类，通常应该先开发
# 第一步：创建家具类并且实例化家具对象
#
# class HouseItem:
#
#     def __init__(self, name, area):
#         """
#         :param name: 家具名称
#         :param area: 占地面积
#         """
#         self.name = name
#         self.area = area
#
#     def __str__(self):
#         return "[%s] 占地面积 %.2f" % (self.name, self.area)
#
#
# # 1. 创建家具
# bed = HouseItem("床", 4)
# chest = HouseItem("衣柜", 2)
# table = HouseItem("餐桌", 1.5)
#
# print(bed)
# print(chest)
# print(table)
# 第二步：创建房间类并且实例化房间对象
#
# class House:
#
#     def __init__(self, house_type, area):
#         """
#         house_type: 户型
#         area: 总面积
#         """
#         self.house_type = house_type
#         self.area = area
#
#         # 剩余面积默认和总面积一致
#         self.free_area = area
#         # 默认没有任何的家具
#         self.item_list = []
#
#     def __str__(self):
#         # Python 能够自动的将一对括号内部的代码连接在一起
#         return ("户型：%s\n总面积：%.2f[剩余：%.2f]\n家具：%s"
#                 % (self.house_type, self.area,
#                    self.free_area, self.item_list))
#
#     def add_item(self, item):
#         print("要添加 %s" % item)
#
#
# # 2. 创建房子对象
# my_home = House("汤成一品两室一厅", 60)
#
# print(my_home)
# 第三步：在House中完善添加家具的方法
#
#     def add_item(self, item):
#         print("要添加 %s" % item)
#         # 1. 判断家具面积是否大于剩余面积
#         if item.area > self.free_area:
#             print("%s 的面积太大，不能添加到房子中" % item.name)
#             return
#         # 2. 将家具的名称追加到名称列表中
#         self.item_list.append(item.name)
#         # 3. 计算剩余面积
#         self.free_area -= item.area
# 完整案例：
#
# class HouseItem:
#
#     def __init__(self, name, area):
#         """
#
#         :param name: 家具名称
#         :param area: 占地面积
#         """
#         self.name = name
#         self.area = area
#
#     def __str__(self):
#         return "[%s] 占地面积 %.2f" % (self.name, self.area)
#
#
# # 1. 创建家具
# bed = HouseItem("席梦思", 4)
# chest = HouseItem("衣柜", 2)
# table = HouseItem("餐桌", 1.5)
# class House:
#
#     def __init__(self, house_type, area):
#         """
#         house_type: 户型
#         area: 总面积
#         """
#         self.house_type = house_type
#         self.area = area
#
#         # 剩余面积默认和总面积一致
#         self.free_area = area
#         # 默认没有任何的家具
#         self.item_list = []
#
#     def __str__(self):
#         # Python 能够自动的将一对括号内部的代码连接在一起
#         return ("户型：%s\n总面积：%.2f[剩余：%.2f]\n家具：%s"
#                 % (self.house_type, self.area,
#                    self.free_area, self.item_list))
#
#     def add_item(self, item):
#         print("要添加 %s" % item)
#         # 1. 判断家具面积是否大于剩余面积
#         if item.area > self.free_area:
#             print("%s 的面积太大，不能添加到房子中" % item.name)
#             return
#         # 2. 将家具的名称追加到名称列表中
#         self.item_list.append(item.name)
#         # 3. 计算剩余面积
#         self.free_area -= item.area
#
#
# # 2. 创建房子对象
# my_home = House("汤成一品两室一厅", 60)
#
# my_home.add_item(bed)
# my_home.add_item(chest)
# my_home.add_item(table)
# print(my_home)
# 小结：
#
# 主程序只负责创建房子对象和家具对象
# 让房子对象调用 add_item 方法将家具添加到房子中
# 面积计算、剩余面积、家具列表等处理都被封装到房子类的内部
# 案例二：士兵突击
# 需求：
#
# 士兵许三多有一把AK47
# 士兵可以开火
# 枪能够发射子弹
# 枪装填装填子弹
# img-士兵突击类图
#
# 先开发枪类
#
# shoot 方法需求
#
# 判断是否有子弹，没有子弹无法射击
# 使用 print 提示射击，并且输出子弹数量
# class Gun:
#
#     def __init__(self, model):
#         # 枪的型号
#         self.model = model
#         # 子弹数量,初始为0
#         self.bullet_count = 0
#
#     def add_bullet(self, count):
#         self.bullet_count += count
#
#     def shoot(self):
#         # 判断是否还有子弹
#         if self.bullet_count <= 0:
#             print("没有子弹了...")
#
#             return
#
#         # 发射一颗子弹
#         self.bullet_count -= 1
#
#         print("%s 发射子弹[%d]...突突突" % (self.model, self.bullet_count))
#
#
# # 创建枪对象
# ak47 = Gun("ak47")
# ak47.add_bullet(50)
# ak47.shoot()
# 开发士兵类：
#
# fire 方法需求：
#
# 判断是否有枪，没有枪没法冲锋
# 喊一声口号
# 装填子弹
# 射击
# class Soldier:
#     def __init__(self, name, gun=None):
#         # 姓名
#         self.name = name
#         # 枪，士兵初始没有枪 None 关键字表示什么都没有
#         self.gun = gun
#
#     def fire(self):
#         # 1. 判断士兵是否有枪
#         if self.gun is None:
#             print("[%s] 还没有枪..." % self.name)
#         else:
#             # 2. 高喊口号
#             print("冲啊...[%s]" % self.name)
#             if self.gun.bullet_count <= 0:
#                 print("没子弹了，快换弹夹...")
#                 # 3. 让枪装填子弹
#                 self.gun.add_bullet(50)
#                 # 4. 让枪发射子弹
#                 self.gun.shoot()
#
# xsd = Soldier("xsd",ak47)
# xsd.fire()

