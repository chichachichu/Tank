"""
v1.05
    新增功能：
    事件处理：
        游戏窗口左上角显示敌方坦克剩余多少辆
"""
# 导入pygame模块
import pygame

GameVersion = "v1.05 "  # 游戏版本变量


# 游戏主逻辑类
class MainGame:
    # 游戏主窗口
    window = None  # 定义游戏窗口对象
    SCREEN_HEIGHT = 500  # 游戏主窗口高度
    SCREEN_WIDTH = 800  # 游戏主窗口宽度
    COLOR_BLACK = pygame.Color(0, 0, 0)  # 窗口背景色-黑色
    COLOR_RED = pygame.Color(255, 0, 0)  # 左上角提示文字-红色

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
            # 时间监听
            self.getEvent()
            #将绘制文字的小画布粘贴到游戏窗口左上角
            MainGame.window.blit(self.getTextSurface("敌方剩余坦克%s辆！"%5),(10,10))
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
                    print("向左掉头")
                elif event.key == pygame.K_RIGHT:
                    print("向右掉头")
                elif event.key == pygame.K_DOWN:
                    print("向下掉头")
                elif event.key == pygame.K_UP:
                    print("向上掉头")
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
    def __init__(self):
        pass

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
