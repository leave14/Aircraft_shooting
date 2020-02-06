import pygame

pygame.init()

# 创建游戏窗口 480*700
screen = pygame.display.set_mode((480, 700))

# 绘制背景图像
# 加载图像数据
bg = pygame.image.load("./images/background.png")

# 绘制英雄飞机
hero = pygame.image.load("./images/me1.png")

# 创建时钟对象
clock = pygame.time.Clock()

# 1. 定义rect记录飞机初始位置
hero_rect = pygame.Rect(150, 300, 102, 126)

# 游戏循环:意味着游戏开始

while True:
    # tick()方法可以指定时钟对象每秒钟运行的频率
    clock.tick(60)

    #监听事件
    for event in pygame.event.get():

        #判断事件类型是否是退出事件
        if event.type == pygame.QUIT:
            print("游戏退出。。")

            #quit卸载所有模块
            pygame.quit()

            # exit（）直接终止当前正在执行的程序
            exit()


    # 2. 修改飞机的位置
    hero_rect.y -= 1

    # 判断飞机位置
    if hero_rect.y <= 0-126:
        hero_rect.y = 700

    # 3.调用blit方法绘制图像
    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)

    # 4. 调用update方法更新
    pygame.display.update()

pygame.quit()
