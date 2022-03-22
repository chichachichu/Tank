"""
v1.03
    新增功能：
    创建游戏窗口
    用到游戏引擎中的功能模块
    官方开发文档
"""
# 导入pygame模块
import pygame


# 游戏主逻辑类
class MainGame:
    # 游戏主窗口
    window = None  # 定义游戏窗口对象
    SCREEN_HEIGHT = 500  # 游戏主窗口高度
    SCREEN_WIDTH = 800  # 游戏主窗口宽度
    COLOR_BLACK=pygame.Color(0,0,0)  #游戏主窗口的颜色
    def __init__(self):
        pass

    # 开始游戏
    def startGame(self):
        # 初始化显示模块
        pygame.display.init()
        # 创建窗口加载窗口（借鉴官方文档）
        # 初始化要显示的窗口
        MainGame.window = pygame.display.set_mode([MainGame.SCREEN_WIDTH, MainGame.SCREEN_HEIGHT])
        #设置游戏窗口的标题
        pygame.display.set_caption("坦克大战游戏v1.0")
        #使用循环和游戏刷新方法让窗口一直展示
        while True:
            #给游戏主窗口填充一个主背景色
            MainGame.window.fill(MainGame.COLOR_BLACK)
            #窗口的刷新
            pygame.display.update()
    # 结束游戏
    def endGame(self):
        print("谢谢使用")
        # 结束程序
        exit()


MainGame().startGame()


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
