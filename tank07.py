"""
v1.07
    新增功能：
        优化坦克移动方式
        1.按下方向键坦克一直移动
        2.松开方向键坦克停止移动
"""
# 导入pygame模块
import pygame

GameVersion = "v1.07 "  # 游戏版本变量


# 游戏主逻辑类
class MainGame:
    # 游戏主窗口
    window = None  # 定义游戏窗口对象
    SCREEN_HEIGHT = 500  # 游戏主窗口高度
    SCREEN_WIDTH = 800  # 游戏主窗口宽度
    COLOR_BLACK = pygame.Color(0, 0, 0)  # 窗口背景色-黑色
    COLOR_RED = pygame.Color(255, 0, 0)  # 左上角提示文字-红色
    #创建我方坦克
    TANK_P1=None
    TANK_P1=pygame.image.load("C:/Users/Administrator/PycharmProjects/3.Tank/img/p1tankU.gif")
    #图片放在水平垂直偏移100/50的位置上
    #TANK_P1.scroll(100,50)
    #获取坦克的宽高
    TANK_W=TANK_P1.get_width()
    TANK_H=TANK_P1.get_height()
    #我方坦克的初始位置
    position_p1=[SCREEN_WIDTH/2-TANK_W/2,SCREEN_HEIGHT*0.8-TANK_H]
    #我方坦克的移动速度
    speed_p1=10
    def __init__(self):
        pass

    # 开始游戏
    def startGame(self):
        # 初始化显示模块
        pygame.display.init()
        # 创建窗口加载窗口（借鉴官方文档）
        # 初始化要显示的窗口
        MainGame.window = pygame.display.set_mode([MainGame.SCREEN_WIDTH, MainGame.SCREEN_HEIGHT])
        # 设置游戏窗口的标题
        pygame.display.set_caption("坦克大战%s" % GameVersion)
        # 使用循环和游戏刷新方法让窗口一直展示

        #创建一个测试表面

        while True:
            # 给游戏主窗口填充一个主背景色
            MainGame.window.fill(MainGame.COLOR_BLACK)
            #self.position_p1=[self.SCREEN_WIDTH/2-self.TANK_W/2,self.SCREEN_HEIGHT*0.8-self.TANK_H]
            # 时间监听
            self.getEvent()
            #将绘制文字的小画布粘贴到游戏窗口左上角
            MainGame.window.blit(self.getTextSurface("敌方剩余坦克%s辆！"%5),(10,10))
            #将我方坦克放到主屏幕上
            MainGame.window.blit(self.TANK_P1,self.position_p1)
            # 窗口的刷新
            pygame.display.update()

            #MainGame.window.blit(testSurface,(100,150))
            #self.getEvent()

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
                    #掉头
                    self.TANK_P1=pygame.image.load("C:/Users/Administrator/PycharmProjects/3.Tank/img/p1tankL.gif")
                    #设置移动边界条件，position(x,y)中的x范围为（0,self.SCREEN_WIDTH-self.TANK_W）,y的范围为（0,self.SCREEN_HEIGHT-self.TANK_H）
                    if self.position_p1[0]>0:
                        #向掉头方向移动
                        self.position_p1[0]-=self.speed_p1
                elif event.key == pygame.K_RIGHT:
                    self.TANK_P1=pygame.image.load("C:/Users/Administrator/PycharmProjects/3.Tank/img/p1tankR.gif")
                    # print("向右掉头")
                    # 设置移动边界条件，position(x,y)中的x范围为（0,self.SCREEN_WIDTH-self.TANK_W）,y的范围为（0,self.SCREEN_HEIGHT-self.TANK_H）
                    if self.position_p1[0] <(self.SCREEN_WIDTH-self.TANK_W):
                        #向掉头方向移动
                        self.position_p1[0]+=self.speed_p1
                elif event.key == pygame.K_DOWN:
                    self.TANK_P1=pygame.image.load("C:/Users/Administrator/PycharmProjects/3.Tank/img/p1tankD.gif")
                    # print("向下掉头")
                    # 设置移动边界条件，position(x,y)中的x范围为（0,self.SCREEN_WIDTH-self.TANK_W）,y的范围为（0,self.SCREEN_HEIGHT-self.TANK_H）
                    if self.position_p1[1]<(self.SCREEN_HEIGHT-self.TANK_H):
                        #向掉头方向移动
                        self.position_p1[1]+=self.speed_p1
                elif event.key == pygame.K_UP:
                    self.TANK_P1=pygame.image.load("C:/Users/Administrator/PycharmProjects/3.Tank/img/p1tankU.gif")
                    # 设置移动边界条件，position(x,y)中的x范围为（0,self.SCREEN_WIDTH-self.TANK_W）,y的范围为（0,self.SCREEN_HEIGHT-self.TANK_H）
                    if self.position_p1[1] > 0:
                        #向掉头方向移动
                        self.position_p1[1]-=self.speed_p1
                    # print("向上掉头")
                elif event.key == pygame.K_SPACE:
                    print("发射子弹")


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


# 初始化游戏方法
MainGame().startGame()


# 测试事件获取方法的返回值
# MainGame().getEvent()

# 坦克类
class Tank:
    # 获取坦克的宽高
    TANK_W = TANK_P1.get_width()
    TANK_H = TANK_P1.get_height()
    def __init__(self):
        self.images={
            'U':pygame.image.load('C:/Users/Administrator/PycharmProjects/3.Tank/img/p1tankU.gif'),
            'D':pygame.image.load('C:/Users/Administrator/PycharmProjects/3.Tank/img/p1tankD.gif'),
            'L':pygame.image.load('C:/Users/Administrator/PycharmProjects/3.Tank/img/p1tankL.gif'),
            'R':pygame.image.load('C:/Users/Administrator/PycharmProjects/3.Tank/img/p1tankR.gif'),
        }
        self.direction="u"
        self.image=self.images[self.direction]
        #坦克所在位置


    # 坦克的移动方法
    def move(self):
        pass

    # 坦克的射击方法
    def shot(self):
        pass

    # 坦克的展示
    def displayTank(self):
        pass


# 我方坦克
class MyTank(Tank):
    def __init__(self):
        pass


# 敌方坦克
class EnemyTank(Tank):
    def __init__(self):
        pass


# 子弹类
class Bullet:
    def __init__(self):
        pass

    # 子弹移动方法
    def move(self):
        pass

    # 展示子弹的方法
    def displayBullet(self):
        pass


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
