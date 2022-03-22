"""
v1.14
    1.实现子弹的移动

"""
# 导入pygame模块
import pygame, time, random

GameVersion = "v1.14 "  # 游戏版本变量


# 游戏主逻辑类
class MainGame:
    # 游戏主窗口
    window = None  # 定义游戏窗口对象
    SCREEN_HEIGHT = 500  # 游戏主窗口高度
    SCREEN_WIDTH = 800  # 游戏主窗口宽度
    COLOR_BLACK = pygame.Color(0, 0, 0)  # 窗口背景色-黑色
    COLOR_RED = pygame.Color(255, 0, 0)  # 左上角提示文字-红色
    # 创建我方坦克
    TANK_P1 = None
    # 存储敌方坦克
    Etank_list = []
    # 要创建的地方坦克的数量
    Etank_count = 5
    # 创建存放我方子弹的列表
    my_bullet_list = []

    def __init__(self):
        pass

    # 开始游戏
    def startGame(self):
        # 初始化显示模块
        pygame.display.init()
        # 创建窗口加载窗口（借鉴官方文档）
        # 初始化要显示的窗口
        MainGame.window = pygame.display.set_mode([MainGame.SCREEN_WIDTH, MainGame.SCREEN_HEIGHT])
        # 初始化我方坦克
        MainGame.TANK_P1 = Tank(self.SCREEN_WIDTH / 2 - 30, self.SCREEN_HEIGHT * 0.8)
        # 初始化敌方坦克
        self.creatEnemyTank()
        # 设置游戏窗口的标题
        pygame.display.set_caption("坦克大战%s" % len(MainGame.Etank_list))

        # 使用循环和游戏刷新方法让窗口一直展示

        # 创建一个测试表面

        while True:
            # 给游戏主窗口填充一个主背景色
            MainGame.window.fill(MainGame.COLOR_BLACK)
            # 事件监听
            self.getEvent()
            # 将绘制文字的小画布粘贴到游戏窗口左上角
            MainGame.window.blit(self.getTextSurface("敌方剩余坦克%s辆！" % 5), (10, 10))
            # 将我方坦克加载到窗口中
            MainGame.TANK_P1.displayTank()
            # 将敌方坦克加载到窗口中
            self.blitEnemyTank()
            # 将我方发射的子弹加载到窗口中
            # 持续调用坦克移动方法，实现坦克持续移动
            if MainGame.TANK_P1 and not MainGame.TANK_P1.stop:
                MainGame.TANK_P1.move()
                time.sleep(0.01)
            # 调用子弹展示方法
            self.blitBullet()
            # 窗口的刷新
            pygame.display.update()
            # MainGame.window.blit(testSurface,(100,150))
            # self.getEvent()

    # 获取程序运行期间所有事件 (鼠标事件、键盘事件)
    def getEvent(self):
        # 1.获取所有事件
        eventList = pygame.event.get()
        # 2。对所有事件进行判断处理（1.点击关闭按钮，2按下键盘上的某个按键）
        # 对获取到的事件裂变进行遍历
        for event in eventList:
            if event.type == pygame.QUIT:
                self.endGame()
                # print("退出",event.type)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    # print("向左掉头")
                    # 改变方向向Left
                    MainGame.TANK_P1.direction = "L"
                    # 改变坦克移动开关stop为False
                    MainGame.TANK_P1.stop = False
                    # 调用移动方法
                    # MainGame.TANK_P1.move()
                elif event.key == pygame.K_RIGHT:
                    # print("向右掉头")
                    MainGame.TANK_P1.direction = "R"
                    # 改变坦克移动开关stop为False
                    MainGame.TANK_P1.stop = False
                    # MainGame.TANK_P1.move()
                elif event.key == pygame.K_DOWN:
                    # print("向下掉头")
                    MainGame.TANK_P1.direction = "D"
                    # 改变坦克移动开关stop为False
                    MainGame.TANK_P1.stop = False
                    # MainGame.TANK_P1.move()
                elif event.key == pygame.K_UP:
                    # print("向上掉头")
                    MainGame.TANK_P1.direction = "U"
                    # 改变坦克移动开关stop为False
                    MainGame.TANK_P1.stop = False
                    # MainGame.TANK_P1.move()
                elif event.key == pygame.K_SPACE:
                    print("发射子弹")
                    # 调用发射子弹方法
                    m = Bullet(MainGame.TANK_P1)
                    # 将生成的子弹对象加入到我放子弹列表中
                    MainGame.my_bullet_list.append(m)
            # 松开方向按键时改变移动开关为True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    MainGame.TANK_P1.stop = True

    # 游戏窗口左上角文字绘制方法
    def getTextSurface(self, text):
        # 初始化字体模块
        pygame.font.init()
        # 选中其中一个合适的字体
        font = pygame.font.SysFont('kaiti', 18)
        # 使用对应的字体完成相关内容的绘制
        textSurface = font.render(text, True, MainGame.COLOR_RED)
        return textSurface

        # 结束游戏

    def endGame(self):
        print("谢谢使用")
        # 结束程序
        exit()

    # 生成敌方坦克
    def creatEnemyTank(self):
        for i in range(MainGame.Etank_count):
            top = 80
            speed = 1
            # 给地方坦克一个100到700的随机水平位置
            rand_n = random.randint(1, 7)
            # print(rand_n)
            left = rand_n * 100
            eTank = EnemyTank(left, top, speed)
            # 循环将敌方坦克加入到敌方坦克储存列表中
            MainGame.Etank_list.append(eTank)

    # 遍历敌方坦克储存列表，将列表中的每一项都加载到游戏窗口中
    def blitEnemyTank(self):
        for i in MainGame.Etank_list:
            i.displayTank()
            i.randomDirectionMove()

    # 发射子弹方法
    def sheetBullet(self):
        return Bullet(self)

    # 遍历我方坦克发射的子弹列表，将列表中的每一项加载到游戏窗口中
    def blitBullet(self):
        for bullet in MainGame.my_bullet_list:
            bullet.displayBullet()
            bullet.move()


# 坦克类
class Tank:

    def __init__(self, left, top):
        self.images = {
            "U": pygame.image.load("C:/Users/Administrator/PycharmProjects/3.Tank/img/p1tankU.gif"),
            "D": pygame.image.load("C:/Users/Administrator/PycharmProjects/3.Tank/img/p1tankD.gif"),
            "R": pygame.image.load("C:/Users/Administrator/PycharmProjects/3.Tank/img/p1tankR.gif"),
            "L": pygame.image.load("C:/Users/Administrator/PycharmProjects/3.Tank/img/p1tankL.gif"),
        }
        self.direction = "U"
        self.image = self.images[self.direction]
        # 坦克的区域
        self.rect = self.image.get_rect()
        # 指定坦克初始化位置  分别距x，y轴的位置
        self.rect.left = left
        self.rect.top = top
        # 新增速度属性
        self.speed = 1
        # 坦克移动开关属性
        self.stop = True

    # 坦克的移动方法
    def move(self):
        if self.direction == "U" and self.rect.top > 0:
            # print(self.rect.top)
            self.rect.top -= self.speed
        elif self.direction == "D" and self.rect.top < MainGame.SCREEN_HEIGHT - self.rect.height:
            self.rect.top += self.speed
        elif self.direction == "R" and self.rect.left < MainGame.SCREEN_WIDTH - self.rect.width:
            self.rect.left += self.speed
        elif self.direction == "L" and self.rect.left > 0:
            self.rect.left -= self.speed

    # 坦克的射击方  法
    def shot(self):
        pass

    # 坦克的展示
    def displayTank(self):
        # 1.重新设置坦克的图片
        self.image = self.images[self.direction]
        # 2.将坦克加载到窗口中
        MainGame.window.blit(self.image, self.rect)


# 我方坦克
class MyTank(Tank):
    def __init__(self):
        pass


# 敌方坦克
class EnemyTank(Tank):
    def __init__(self, left, top, speed):
        self.images = {
            "U": pygame.image.load("C:/Users/Administrator/PycharmProjects/3.Tank/img/enemy2U.gif"),
            "D": pygame.image.load("C:/Users/Administrator/PycharmProjects/3.Tank/img/enemy2D.gif"),
            "R": pygame.image.load("C:/Users/Administrator/PycharmProjects/3.Tank/img/enemy2R.gif"),
            "L": pygame.image.load("C:/Users/Administrator/PycharmProjects/3.Tank/img/enemy2L.gif"),
        }
        # 随机生成方向

        self.direction = self.randomDirection()
        self.image = self.images[self.direction]
        # 坦克的区域
        self.rect = self.image.get_rect()
        # 坦克的坐标和速度
        self.rect.left = left
        self.rect.top = top
        self.speed = speed
        # 坦克移动开关属性
        self.stop = True
        # 给地方坦克一个步长属性，用来递减，当步长减到一的时候让其调用随机方向方法随机生成一个方向
        self.step = 200

    # 随机生成一个方向
    def randomDirection(self):
        randnum = random.randint(1, 4)
        if randnum == 1:
            return "U"
        elif randnum == 2:
            return "D"
        elif randnum == 3:
            return "L"
        elif randnum == 4:
            return "R"

    # 地方坦克随机移动方法
    def randomDirectionMove(self):
        self.move()
        if self.step == 0:
            self.direction = self.randomDirection()
            self.step = 200
        else:
            self.step -= 1


# 子弹类
class Bullet:
    def __init__(self, tank):
        # 图片
        self.image = pygame.image.load("C:/Users/Administrator/PycharmProjects/3.Tank/img/enemymissile.gif")
        # 方向
        self.direction = tank.direction
        # 位置
        self.rect = self.image.get_rect()
        if self.direction == "U":
            self.rect.left = tank.rect.left + tank.rect.width / 2 - self.rect.width / 2
            self.rect.top = tank.rect.top - self.rect.height
        elif self.direction == "D":
            self.rect.left = tank.rect.left + tank.rect.width / 2 - self.rect.width / 2
            self.rect.top = tank.rect.top + tank.rect.height
        elif self.direction == "L":
            self.rect.left = tank.rect.left - self.rect.width
            self.rect.top = tank.rect.top + tank.rect.height / 2 - self.rect.height / 2
        elif self.direction == "R":
            self.rect.left = tank.rect.left + tank.rect.width
            self.rect.top = tank.rect.top + tank.rect.height / 2 - self.rect.height / 2
        # 速度
        self.speed = 3

    # 子弹移动方法
    def move(self):
        if self.direction == "U":
            if self.rect.top > 0:
                self.rect.top -= self.speed
        elif self.direction == "D":
            if self.rect.top < MainGame.SCREEN_HEIGHT - self.rect.height:
                self.rect.top += self.speed
        elif self.direction == "L":
            if self.rect.left > 0:
                self.rect.left -= self.speed
        elif self.direction == "R":
            if self.rect.left < MainGame.SCREEN_WIDTH - self.rect.width:
                self.rect.left += self.speed

    # 展示子弹的方法
    def displayBullet(self):
        MainGame.window.blit(self.image, self.rect)


# 爆炸效果
class Explode:
    def __init__(self):
        pass

    # 展示爆炸效果
    def displayExplode(self):
        pass


# 墙壁类
class Wall:
    def __init__(self):
        pass

    # 展示墙壁的方法
    def displayWall(self):
        pass


# 音效类
class Music:
    def __init__(self):
        pass

    # 开始播放音乐
    def playMusic(self):
        pass


# 初始化游戏方法
MainGame().startGame()
