# 04.继承与多态
# 继承
# 子类可复用父类的属性和方法，并扩展新功能，实现代码复用和逻辑分层。例如，"电动车"类继承自"汽车"类，新增"充电"方法。

# 不用继承创建对象

class Person:
    def __init__(self,name,sex,age):
        self.name = name
        self.age = age
        self.sex = sex

class Cat:
    def __init__(self,name,sex,age):
        self.name = name
        self.age = age
        self.sex = sex

class Dog:
    def __init__(self,name,sex,age):
        self.name = name
        self.age = age
        self.sex = sex
# 使用继承的方式

class Animal(object):
    def __init__(self,name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name}吃东西..")

class Dog(Animal):
    pass

xiaotianquan = Dog("哮天犬",5)
xiaotianquan.eat()
# 继承概念：子类拥有父类的所有方法和属性。

# img-继承对比图示

# 继承的优点：

# 增加了类的耦合性（耦合性不宜多，宜精）。
# 减少了重复代码。
# 使得代码更加规范化，合理化。
# 继承分类
# 上面的那个例子，涉及到的专业术语：

# Dog 类是 Animal 类的子类，Animal 类是 Dog 类的父类，Dog 类从 Animal 类继承
# Dog 类是 Animal 类的派生类，Animal 类是 Dog 类的基类，Dog 类从 Animal 类派生
# 继承：可以分单继承，多继承。

# 这里需要补充一下 python 中类的种类（继承需要）：

# 在 python 2 版本中存在两种类.：

# ⼀个叫经典类. 在 Python2 中，经典类是指没有显式继承自 object 的类。它们使用旧的类定义方式。
# ⼀个叫新式类. 新式类是指显式继承自 object 或其他新式类的类。新式类在 Python 2.2 中引入，并在 Python 3 中成为默认。
# 单继承
# 对象执行父类方法
class Animal(object):
    type_name = '动物类'

    def __init__(self,name,sex,age):
        self.name = name
        self.age = age
        self.sex = sex

    def eat(self):
        print('吃',self)

class Person(Animal):
    pass
class Dog(Animal):

    def run(self):
        #执行父类方法
        
        print(f"dog running....")
    pass
class Cat(Animal):
    pass



print(Person.type_name)
Person.eat('东西')
print(Person.type_name)

p1 = Person('aaron','男',18)
print(p1.__dict__)
print(p1.type_name)
p1.type_name = '666'
print(p1)
p1.eat()
# 执行顺序
class Animal(object):
    def __init__(self,name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name}吃东西..")

class person(Animal):
    def eat(self):
        print('%s 用筷子吃饭' % self.name)

class Dog(Animal):
    pass

class Cat(Animal):
    pass


person1 = person('张三',18)
person1.eat()
# 同时执行类以及父类方法
# 方法一：如果想执行父类的 eat() 方法，可以在子类的方法中写上：父类.eat(对象,其他参数)

class Animal(object):
    type_name = '动物类'
    def __init__(self,name,sex,age):
            self.name = name
            self.age = age
            self.sex = sex

    def eat(self):
        print('吃东西')

class Person(Animal):
    def __init__(self,name,sex,age,mind):
        Animal.__init__(self,name,sex,age)
        self.mind = mind

    def eat(self):
        Animal.eat(self)
        print('%s 吃饭'%self.name)

class Cat(Animal):
    pass

class Dog(Animal):
    pass

p1 = Person('aaron','男',18,'想吃东西')
p1.eat()
# 方法二：利用 super().func(参数)

class Animal(object):
    type_name = '动物类'
    def __init__(self,name,sex,age):
            self.name = name
            self.age = age
            self.sex = sex

    def eat(self):
        print('吃东西')

class Person(Animal):
    def __init__(self,name,sex,age,mind):
        # super(Person,self).__init__(name,sex,age)
        super().__init__(name,sex,age)
        self.mind = mind

    def eat(self):
        super().eat()
        print('%s 吃饭' % self.name)

class Cat(Animal):
    pass

class Dog(Animal):
    pass

p1 = Person('aaron','男',18,'想吃东西')
p1.eat()
# 方法重写
# 如果在开发中，父类的方法实现和子类的方法实现，完全不同，可以使用覆盖的方式，在子类中重新编写父类的方法实现
# 具体的实现方式，就相当于在子类中定义了一个和父类同名的方法并且实现
# 重写之后，在运行时，只会调用子类中重写的方法，而不再会调用父类封装的方法
# 子类中扩展父类方法
# 如果在开发中，子类的方法实现中包含父类的方法实现
# 父类原本封装的方法实现 是 子类方法的一部分**
# 就可以使用扩展的方式
# 在子类中重写父类的方法
# 在需要的位置使用 super().父类方法 来调用父类方法的执行
# 代码其他的位置针对子类的需求，编写 子类特有的代码实现
# 关于 super

# 在 Python 中 super 是一个特殊的类
# super() 就是使用 super 类创建出来的对象
# 最常使用的场景就是在重写父类方法时，调用在父类中封装的方法实现
# 父类的私有属性和私有方法
# 子类对象不能在自己的方法内部，直接访问父类的私有属性或私有方法，但可以通过父类的公有方法间接访问

# 私有属性、方法 是对象的隐私，不对外公开，外界以及子类都不能直接访问
# 私有属性、方法 通常用于做一些内部的事情
# img-父类的私有属性和私有方法

# B 的对象不能直接访问 __num2 属性
# B 的对象不能在 demo 方法内访问 __num2 属性
# B 的对象可以在 demo 方法内，调用父类的 test 方法
# 父类的 test 方法内部，能够访问 __num2 属性和 __test 方法
class Animal:
    def __init__(self,name):
        self.__name = name

    def __eat(self):
        print(self.__name + "Eating...")

    def eat2(self):
        self.__eat()

class Dog(Animal):
    pass

a = Dog('哮天犬')
print(a.name)
a.__eat()
a.eat2()
# 多继承
# 概念

# 子类 可以拥有 多个父类，并且具有 所有父类 的 属性 和 方法
# 例如：孩子 会继承自己 父亲 和 母亲 的 特性
# img-多继承1

# 语法

# class 子类名(父类名1, 父类名2...)
#     pass
# 问题的提出

# 如果 不同的父类 中存在 同名的方法，子类对象 在调用方法时，会调用 哪一个父类中的方法呢？
# 提示：开发时，应该尽量避免这种容易产生混淆的情况！ —— 如果 父类之间 存在 同名的属性或者方法，应该 尽量避免 使用多继承

# img-多继承2

class shengxian:    # 神仙
    def fei(self):
        print("神仙会飞")

    def eat(self):
        print("吃人参果")

class monkey:   # 猴
    def eat(self):
        print("吃桃子")

class songwukong(shengxian,monkey): #孙悟空既是神仙也是猴
    def __init__(self):
        self.name = "孙悟空"

    def eat(self):
        print("我是齐天大圣，我不用吃东西")

swk = songwukong()
swk.eat()
# 经典类
class A:
    pass
class B(A):
    pass
class C(A):
    pass
class D(B, C):
    pass
"""
class D(B,C)
MRO计算公式：
    L[D]=D+merge(L[B],L[C],[B,C])
        L[A]=A+merge(L[O],[O])=[A,O]        
        L[B]=B+merge(L[A],[A])=[B,A]
            =B+merge([A,O],A)
            =[B,A,O]
        L[C]=C+merge(L[A],[A])=[C,A]
            =C+merge([A,O],[A])
            =[C,A]+merge([O],[])    #merge
       
        
"""
class E:
    pass
class F(D, E):
    pass
class G(F, D):
    pass
class H:
    pass
class Foo(H, G):
    pass
# 示意图

# img-经典类多继承

# 在经典类中采⽤的是深度优先，遍历⽅案：优先遍历继承链的最左侧分支直至顶端，再向右查找其他分支。

# 类的 MRO (method resolution order): Foo-> H -> G -> F -> E -> D -> B -> A -> C。

# 新式类
# C3 算法是 Python 中用于解决多继承场景下方法解析顺序（MRO）的核心算法，其设计目标是保证继承关系的​​一致性​​、​​本地优先级​​和​​单调性​​。

# 算法核心原理
# C3 算法的核心是​​线性化合并规则​​，通过递归合并父类的MRO列表生成一个无冲突的继承顺序链。

# 对于类 C(B1, B2, ..., Bn) ，其 MRO 计算公式为为：L[C] = C + merge(L[B1],L[B2],..,L[Bn],[B1,B2,...,Bn]) 其中 megre 操作负责合并父类的 MRO 序列。

# merge 合并规则
# merge 操作是 C3 算法的核心步骤，具体执行流程如下：

# ​选取第一个列表的头元素（Head）​​： 即列表的第一个元素，记为 h。
# ​检查 h 的有效性：
# 若 h 不在其他列表的​​尾部​​（即其他列表除首元素外的部分），则将其加入结果序列，并从所有列表中删除 h。
# 若 h 存在于其他列表的尾部，则跳过当前列表，选择下一个列表的头元素重复检查。
# ​递归执行​​： 重复步骤1-2，直到所有列表为空（成功）或无法找到有效头元素（失败并抛出 TypeError）
# 示例解析

# 假设类 D 继承自 B 和 C，其父类的 MRO 分别为 L(B)=[B, A, O] 和 L(C)=[C, A, O]，则 D 的 MRO 计算如下： L(D) = D + merge([B,A,O],[C,A,O],[B,C])

# 初始合并列表为 [[B, A, O], [C, A, O], B, C]。
# 提取 B（不在其他列表尾部），结果序列为 [D, B]，剩余列表 [[A, O], [C, A, O], C]。
# 提取 C（不在其他列表尾部），结果序列扩展为 [D, B, C]，剩余列表 [[A, O], [A, O]]。
# 合并 A 和 O，最终得到 L(D)=[D, B, C, A, O]
# 实践案例
# img-新式类megre

# 计算 mro(A) 方式：

# step1: 
    L(A) = A + merge(L[B] + L[C], [B, C])
    L(B) = B + merge(L[D] + L[E], [D, E])
    L(C) = C + merge(L[E] + L[F], [E, F])
    L(D) = D + merge(L[O]) = [D, O]
    L(E) = E + merge(L[O]) = [E, O]
    L[F] = F + merge(L[O]) = [F, O]
# step2:
    L(B) = B + merge([D, O], [E, O], [D, E])
         = [B, D] + merge([O], [E, O], [E]) # 拿出并删除D
         = [B, D, E] + merge([O], [O])  # 拿出并删除E
         = [B, D, E, O]
    L(C) = C + merge([E, O], [F, O], [E, F])
         ...
         = [C, E, F, O]
# step3:
    L(A) = A + merge([B, D, E, O], [C, E, F, O], [B, C])
         = [A, B] + merge([D, E, O], [C, E, F, O], [C]) # h = B 拿出并删除B  
         = [A, B, D] + merge([E, O], [C, E, F, O], [C]) # h = D 拿出并删除D
         = [A, B, D] + merge([E, O], [C, E, F, O], [C]) # h = E 存在于其他列表的尾部则跳过
         ...
         = [A, B, D, C, E, F, O]
# 代码

class D:
    pass
class E:
    pass
class F:
    pass
class B(D,E):
    pass
class C(E,F):
    pass
class A(B,C):
    pass
print(A.__mro__)
# 多态
# 同一方法在不同对象中呈现不同行为，增强代码灵活性。例如，"动物"类的"发声"方法在"狗"和"猫"对象中分别输出"汪汪"和"喵喵"。

# 多态可以增加代码的灵活度
# 以继承和重写父类方法为前提
# 是调用方法的技巧，不会影响到类的内部设计
# img-多态示意图

class human(object):
    def work(self):
        return "喝杯咖啡，开始工作"

class ps_job(human):
    def work(self):
        return "开始美工"

class IT_job(human):
    def work(self):
        return "开始敲代码"


def job(person):    # 多态函数
    print(person.work())

# 创建不同类型的对象
ps = ps_job()
it = IT_job()

# 调用同一个函数，表现出不同的行为
job(ps)
job(it)
案例：哮天犬

需求

在 Dog 类中封装方法 game
定义 XiaoTianDog 继承自 Dog ，并且重写 game 方法
定义 Person 类，并且封装一个和狗玩的方法
img-多态

实现

class Dog(object):

    def __init__(self, name):
        self.name = name

    def game(self):
        print("%s 蹦蹦跳跳的玩耍..." % self.name)


class XiaoTianDog(Dog):

    def game(self):
        print("%s 飞到天上去玩耍..." % self.name)


class Person(object):

    def __init__(self, name):
        self.name = name

    def game_with_dog(self, dog):

        print("%s 和 %s 快乐的玩耍..." % (self.name, dog.name))

        # 让狗玩耍
        dog.game()


# 1. 创建一个狗对象
wangcai = Dog("旺财")
xiaotianquan = XiaoTianDog("飞天旺财")

# 2. 创建一个小明对象
xiaoming = Person("小明")

# 3. 让小明调用和狗玩的方法
xiaoming.game_with_dog(wangcai)
xiaoming.game_with_dog(xiaotianquan)
案例小结

Person 类中只需要让狗对象调用 game 方法，而不关心具体是什么狗。
game 方法是在 Dog 父类中定义的。
在程序执行时，传入不同的狗对象实参，就会产生不同的执行效果。
鸭子类型
python 中有一句谚语说的好，你看起来像鸭子，那么你就是鸭子。

这句谚语是关于鸭子类型（Duck Typing）的一种表达方式。鸭子类型是一种动态类型的概念，它强调一个对象的特征和行为，而不是其具体的类型或继承关系。

在 Python 中，鸭子类型的概念可以简单地表述为：如果一个对象具有像鸭子一样的特征和行为，那么我们可以认为它是一个鸭子。这意味着我们关注对象是否具备特定的方法和属性，而不关心对象的具体类型。

这种思想在 Python 中经常被使用，特别是在函数参数传递和对象的使用上。如果一个函数接受一个参数，并假设该参数具有某些特定的方法或属性，那么只要传递的对象满足这些要求，它就可以正常工作，无论对象的具体类型是什么。

下面是一个简单的示例来说明鸭子类型的概念：

class Duck:
    def quack(self):
        print("嘎嘎叫!")

    def fly(self):
        print("扑哧扑哧的飞!")


class Person:
    def quack(self):
        print("我喜欢跟鸭子一样嘎嘎叫")

    def fly(self):
        print("我也喜欢跟鸭子一样飞")


def make_it_quack_and_fly(obj):
    obj.quack()
    obj.fly()


duck = Duck()
person = Person()

make_it_quack_and_fly(duck)
make_it_quack_and_fly(person)
在上述示例中，我们定义了一个 Duck 类和一个 Person 类，它们都具有 quack 和 fly 方法。然后，我们定义了一个函数 make_it_quack_and_fly，它接受一个参数 obj，并调用 obj 的 quack 和 fly 方法。

我们可以看到，无论是 Duck 对象还是 Person 对象，只要它们具有 quack 和 fly 方法，都可以作为参数传递给 make_it_quack_and_fly 函数，并成功执行相应的方法。

这正是鸭子类型的思想：如果一个对象具有像鸭子一样的特征和行为（即具有 quack 和 fly 方法），那么我们可以将其视为鸭子，而无需关心对象的具体类型。

类的约束
写一个支付功能

class QQpay:
    def pay(self,money):
        print('使用qq支付%s元' % money)

class Alipay:
    def pay(self,money):
        print('使用阿里支付%s元' % money)

a = Alipay()
a.pay(100)

b = QQpay()
b.pay(200)
统一一下付款方式

class QQpay:
    def pay(self,money):
        print('使用qq支付%s元' % money)

class Alipay:
    def pay(self,money):
        print('使用阿里支付%s元' % money)

def pay(obj,money):
    obj.pay(money)


a = Alipay()
b = QQpay()

pay(a,100)
pay(b,200)
如果后期添加微信支付，但是没有统一标准，换个程序员就可能写成这样。

class QQpay:
    def pay(self,money):
        print('使用qq支付%s元' % money)

class Alipay:
    def pay(self,money):
        print('使用阿里支付%s元' % money)

class Wechatpay:
    def fuqian(self,money):
        print('使用微信支付%s元' % money)

def pay(obj,money):
    print("===============")
    obj.pay(money)


a = Alipay()
b = QQpay()

pay(a,100)
pay(b,200)

c = Wechatpay()
c.fuqian(300)
所以此时我们要用到对类的约束，对类的约束有两种：

提取父类，然后在父类中定义好⽅法，在这个方法中什么都不⽤⼲，就抛⼀个异常就可以了，这样所有的⼦类都必须重写这个⽅法，否则，访问的时候就会报错。

使⽤元类来描述方类，在元类中给出⼀个抽象方法，这样子类就不得不给出抽象方法的具体实现，也可以起到约束的效果。(推荐)

方法1

class Payment:
    """
    此类什么都不做，就是制定一个标准，谁继承我，必须定义我里面的方法。
    """
    def pay(self,money):
        raise Exception("你没有实现pay方法")

class QQpay(Payment):
    def pay(self,money):
        print('使用qq支付%s元' % money)

class Alipay(Payment):
    def pay(self,money):
        print('使用阿里支付%s元' % money)

class Wechatpay(Payment):
    def fuqian(self,money):
        print('使用微信支付%s元' % money)


def pay(obj,money):
    obj.pay(money)

a = Alipay()
b = QQpay()
c = Wechatpay()
pay(a,100)
pay(b,200)
pay(c,300)
**方法2：引入抽象类的概念处理

from abc import ABCMeta,abstractmethod
class Payment(metaclass=ABCMeta):    # 抽象类 接口类 规范和约束  metaclass 指定的是一个元类
    @abstractmethod
    def pay(self):pass  # 抽象方法

class Alipay(Payment):
    def pay(self,money):
        print('使用支付宝支付了%s元'%money)

class QQpay(Payment):
    def pay(self,money):
        print('使用qq支付了%s元'%money)

class Wechatpay(Payment):
    # def pay(self,money):
    #     print('使用微信支付了%s元'%money)
    def recharge(self):pass

def pay(a,money):
    a.pay(money)

a = Alipay()
a.pay(100)
pay(a,100)    # 归一化设计：不管是哪一个类的对象，都调用同一个函数去完成相似的功能
q = QQpay()
q.pay(100)
pay(q,100)
w = Wechatpay()
pay(w,100)   # 到用的时候才会报错



# 抽象类和接口类做的事情 ：建立规范
# 制定一个类的metaclass是ABCMeta，
# 那么这个类就变成了一个抽象类(接口类)
# 这个类的主要功能就是建立一个规范
super() 深入了解
super 是严格按照类的继承顺序执行。

示例1

class A:
    def f1(self):
        print('in A f1')

    def f2(self):
        print('in A f2')


class Foo(A):
    def f1(self):
        super().f2()
        print('in A Foo')

obj = Foo()
obj.f1()
示例2

class A:
    def f1(self):
        print('in A')

class Foo(A):
    def f1(self):
        super().f1()
        print('in Foo')

class Bar(A):
    def f1(self):
        print('in Bar')

class Info(Foo,Bar):
    def f1(self):
        super().f1()
        print('in Info f1')

obj = Info()
obj.f1()

# super() 是严格按照当前类的继承顺序执行的，不会收到过程中其他类的影响
print(Info.mro())
示例3

class A:
    def f1(self):
        print('in A')

class Foo(A):
    def f1(self):
        super().f1()
        print('in Foo')

class Bar(A):
    def f1(self):
        print('in Bar')

class Info(Foo,Bar):
    def f1(self):
        super(Foo,self).f1()    # 这里的意思是绕过Foo，从Foo的位置开始寻找下一个
        print('in Info f1')

obj = Info()
obj.f1()
学前沿IT，到英格科技! all right reserved，powered by Gitbook本文发布时间： 2025-05-17 09:36:07
class MyClass:
    # 1. 类属性：内部添加
    class_attr = "I am a class attribute"

    def __init__(self, name):
        # 2. 对象属性：内部添加
        self.name = name

    def add_instance_attr(self, age):
        # 3. 对象属性：内部添加（通过方法动态添加）
        self.age = age


# 创建实例
obj1 = MyClass("Object 1")

# 访问类属性和对象属性
print(obj1.name)           # 输出: Object 1
print(MyClass.class_attr)  # 输出: I am a class attribute

# 4. 对象属性：外部添加
obj1.gender = "Male"  # 动态给 obj1 添加 gender 属性
print(obj1.gender)    # 输出: Male

# 5. 类属性：外部添加
MyClass.new_class_attr = "I am a new class attribute"
print(MyClass.new_class_attr)  # 输出: I am a new class attribute

# 创建另一个实例，验证类属性的共享性
obj2 = MyClass("Object 2")
print(obj2.name)             # 输出: Object 2
print(obj2.new_class_attr)   # 输出: I am a new class attribute

# 6. 在内部通过方法添加对象属性
obj1.add_instance_attr(25)
print(obj1.age)  # 输出: 25

# 注意：obj2 没有 age 属性，因为 age 是通过 obj1 的方法动态添加的
# print(obj2.age)  # 访问时会报错，因为 obj2 没有 age 属性