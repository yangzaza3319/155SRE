# 03.类的空间问题及关系
# 类的空间问题
# 添加类和对象的属性
# 在 Python 中，对象属性（实例属性）和类属性的添加可以分别在类的内部（定义类时）和外部（运行时）进行。

# 对象属性
# 内部添加：在类的 __init__ 方法中定义的属性，属于对象（实例），每个实例有自己独立的属性。
# 外部添加：可以在实例化对象后，动态地为某个对象添加属性。
# 类属性
# 内部添加：在类的定义中直接定义的属性，属于类本身，所有实例共享。
# 外部添加：可以在类定义后，动态地添加类属性。
# class MyClass:
#     # 1. 类属性：内部添加
#     class_attr = "I am a class attribute"

#     def __init__(self, name):
#         # 2. 对象属性：内部添加
#         self.name = name

#     def add_instance_attr(self, age):
#         # 3. 对象属性：内部添加（通过方法动态添加）
#         self.age = age


# # 创建实例
# obj1 = MyClass("Object 1")

# # 访问类属性和对象属性
# print(obj1.name)           # 输出: Object 1
# print(MyClass.class_attr)  # 输出: I am a class attribute

# # 4. 对象属性：外部添加
# obj1.gender = "Male"  # 动态给 obj1 添加 gender 属性
# print(obj1.gender)    # 输出: Male

# # 5. 类属性：外部添加
# MyClass.new_class_attr = "I am a new class attribute"
# print(MyClass.new_class_attr)  # 输出: I am a new class attribute

# # 创建另一个实例，验证类属性的共享性
# obj2 = MyClass("Object 2")
# print(obj2.name)             # 输出: Object 2
# print(obj2.new_class_attr)   # 输出: I am a new class attribute

# # 6. 在内部通过方法添加对象属性
# obj1.add_instance_attr(25)
# print(obj1.age)  # 输出: 25

# # 注意：obj2 没有 age 属性，因为 age 是通过 obj1 的方法动态添加的
# # print(obj2.age)  # 访问时会报错，因为 obj2 没有 age 属性
# 对象如何找到类的属性
# 对象查找属性的顺序：

# 先从对象空间找
# 类空间找
# 父类空间找
# 基类空间
# 类名查找属性的顺序：

# 先从本类空间找
# 父类空间找
# 基类空间
# 上面的顺序都是单向不可逆，类名不可能找到对象的属性。

# 类之间关系
# 类与类中存在以下关系:

# 依赖关系
# 关联关系
# 组合关系
# 聚合关系
# 实现关系
# 继承关系(类的三大特性之一：继承)
# 依赖关系
# 例：将大象装进冰箱，需要两个类, ⼀个是⼤象类, ⼀个是冰箱类

# class Elphant:
#     def __init__(self, name):
#         self.name = name

#     def open(self):
#         '''
#         开门
#         '''
#         pass

#     def go(self):
#         # 大象进入冰箱
#         pass

#     def close(self):
#         '''
#         关门
#         '''
#         pass


# class Refrigerator:
#     def open_door(self):
#         print('冰箱门打开了')

#     def close_door(self):
#         print('冰箱门关上了')
# 将大象类和冰箱类进行依赖

# class Elphant:
#     def __init__(self,name):
#         self.name = name

#     def open(self,obj):
#         print(self.name + '开门')
#         obj.open_door()

#     def go(self):
#         print(f'{self.name}进到冰箱里')

#     def close(self,obj):
#         print(self.name + '关门')
#         obj.close_door()

# class Refrigerator:
#     def __init__(self,name):
#         self.name = name

#     def open_door(self):
#         print(self.name + '门被打开了')

#     def close_door(self):
#         print(self.name+'门被关上了')

# elphant = Elphant('小飞象')
# refrigerator = Refrigerator('格力冰箱')
# elphant.open(refrigerator)
# elphant.go()
# elphant.close(refrigerator)
# 关联-聚合-组合关系
# 其实这三个在代码上写法是⼀样的，但是从含义上是不⼀样的：

# 关联关系：两种事物必须是互相关联的，但是在某些特殊情况下是可以更改和更换的。
# 聚合关系：属于关联关系中的⼀种特例，侧重点是xxx和xxx聚合成xxx，各⾃有各⾃的声明周期，比如电脑，电脑⾥有 CPU, 硬盘, 内存等等。电脑挂了， CPU 还是好的，还是完整的个体。
# 组合关系：属于关联关系中的⼀种特例，写法上差不多，组合关系比聚合还要紧密。比如⼈的⼤脑，⼼脏，各个器官，这些器官组合成⼀个⼈。这时，⼈如果挂了，其他的东⻄也跟着挂了。
# 关联关系

# class Boy:
#     def __init__(self,name, girlfriend = None):
#         self.name = name
#         self.girlfriend = girlfriend

#     def dinner(self):
#         if self.girlfriend:
#             print('%s 和 %s 一起共进晚餐' % (self.name, self.girlfriend.name))
#         else:
#             print('连女朋友都没有，还有心情吃饭')

# class Girl:
#     def __init__(self, name):
#         self.name = name

# boy = Boy('张三')
# boy.dinner()
# girl = Girl('如花')

# boy2 = Boy('李四', girl)
# boy2.dinner()
# 注意， 此时 Boy 和 Girl 两个类之间就是关联关系，两个类的对象紧密联系着，其中⼀个没有了，另⼀个就孤单的不得了，关联关系，其实就是，我需要你，你也属于我。

# 学校和老师之间的关系

# class School:

#     def __init__(self,name,address):
#         self.name = name
#         self.address = address


# class Teacher:

#     def __init__(self,name,school):
#         self.name = name
#         self.school = school

# s1 = School('镇江校区','北京')
# s2 = School('常州校区','上海')
# s3 = School('南京校区','深圳')

# t1 = Teacher('T1',s1)
# t2 = Teacher('T2',s2)
# t3 = Teacher('T3',s3)

# print(t1.school.name)
# print(t2.school.name)
# print(t3.school.name)
# 但是学校也是依赖于老师的，所以老师学校应该互相依赖。

# class School:

#     def __init__(self,name,address):
#         self.name = name
#         self.address = address
#         self.teacher_list = []
#     def append_teacher(self,teacher):
#         self.teacher_list.append(teacher)


# class Teacher:

#     def __init__(self,name,school):
#         self.name = name
#         self.school = school #s1

# s1 = School('北京校区','北京')
# s2 = School('上海校区','上海')
# s3 = School('深圳校区','深圳')

# t1 = Teacher('T1',s1)
# t2 = Teacher('T2',s2)
# t3 = Teacher('T3',s3)

# s1.append_teacher(t1.name) #t1.school.name->name
# s1.append_teacher(t2.name)
# s1.append_teacher(t3.name)

# print(s1.teacher_list)
# 组合：将一个类的对象封装到另一个类的对象的属性中，就叫组合。

# 例：设计一个游戏，让游戏里面的人物互殴，加上一个武器类，让人使用武器攻击。

# class Gamerole:
#     def __init__(self,name,ad,hp,wea=None):
#         self.name = name
#         self.ad = ad
#         self.hp = hp
#         self.wea = wea

#     def attack(self,obj):
#         obj.hp -= self.ad
#         print('%s攻击%s,%s掉了%s血,还剩%s'%(self.name,p1.name,p1.name,self.ad,p1.hp))

#     def equip_weapon(self,wea_obj):
#         self.wea = wea_obj  #wea_obj作为gamerole的属性
#         wea.ad += self.ad   #gamerole ad属性赋予给wea_obj
#         wea.owner_name = self.name  #gamerole name属性 赋予给wea_obj

# class Weapon:
#     def __init__(self,name,ad,owner_name = None):
#         self.name = name
#         self.owner_name = owner_name
#         self.ad = ad
#     def weapon_attack(self,p2):
#         p2.hp = p2.hp - self.ad
#         print('%s利用%s攻击了%s，%s还剩%s血'%(self.owner_name,self.name,p2.name,p2.name,p2.hp))


# man = Gamerole('人',10,100)
# dog = Gamerole('狗',50,100)
# stick = Weapon('木棍',40)

# man.equip_weapon(stick)
# print(man.wea)
# print(stick.name,stick.owner_name,stick.ad)
# man.wea.weapon_attack(dog)
# 人利用木棍攻击了狗，狗还剩50血
# 案例：王者荣耀3V3
# import time
# import random
# class Gamerole:
#     def __init__(self,name,ad,hp):
#         self.name = name
#         self.ad = ad
#         self.hp = hp

#     def attack(self,p1):
#         p1.hp -= self.ad
#         print('%s攻击%s,%s掉了%s血,还剩%s'%(self.name,p1.name,p1.name,self.ad,p1.hp))

#     def equip_weapon(self,wea):
#         self.wea = wea
#         wea.ad += self.ad
#         wea.owner_name = self.name

# class Weapon:
#     def __init__(self,name,ad,owner_name = None):
#         self.name = name
#         self.owner_name = owner_name
#         self.ad = ad
#     def weapon_attack(self,p2):
#         p2.hp = p2.hp - self.ad
#         print('%s利用%s攻击了%s，%s还剩%s血'%(self.owner_name,self.name,p2.name,p2.name,p2.hp))

# sunwukong = Gamerole("孙悟空", 20, 500)
# caocao = Gamerole("曹操", 20, 100)
# anqila = Gamerole("安琪拉", 50, 80)

# zhaoyun = Gamerole("赵云", 30, 450)
# guanyu = Gamerole("关羽", 80, 200)
# diaochan = Gamerole("貂蝉", 60, 150)

# blue_list = [sunwukong, caocao, anqila]
# red_list = [zhaoyun, guanyu, diaochan]

# if __name__ == '__main__':
#     print("游戏开始加载")
#     # 打印一个菜单
#     for i in range(0, 101, 2):
#         time.sleep(0.1)
#         char_num = i // 2
#         per_str = '\r%s%% : %s\n' % (i, '*' * char_num) \
#             if i == 100 else '\r%s%% : %s' % (i, '*' * char_num)
#         print(per_str, end='', flush=True)

#     info = input("游戏加载完毕，输入任意字符开始！")
#     # 输出东邪吸毒阵营里的任务角色
#     print("蓝方阵营".center(20, '*'))
#     for i in blue_list:
#         print(i.name.center(20))
#     print("红方阵营".center(20, '*'))
#     for i in red_list:
#         print(i.name.center(20))

#     while True:
#         # 判断游戏结束的条件是某一方全部阵亡
#         if len(blue_list) == 0:
#             print("红方阵营胜利！！！")
#             break
#         if  len(red_list) == 0:
#             print("蓝方阵营胜利！")
#             break


#         # 游戏逻辑，每次随机选择一名角色出击
#         index1 = random.randint(0, len(blue_list) - 1)
#         index2 = random.randint(0, len(red_list) - 1)

#         # 开始攻击
#         time.sleep(1)
#         role1 = blue_list[index1]
#         time.sleep(1)
#         role2 = red_list[index2]
#         time.sleep(1)
#         role1.attack(role2)
#         role2.attack(role1)

#         # 判断是否有英雄阵亡
#         if role1.hp <= 0:
#             print("%s阵亡！" % role1.name)
#             blue_list.remove(role1)
#         if role2.hp <= 0:
#             print("%s阵亡！" % role2.name)
#             red_list.remove(role2)

