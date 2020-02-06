import pygame

pygame.init()

#创建游戏窗口 480*700
screen = pygame.display.set_mode((480, 700))

#绘制背景图像
#加载图像数据
bg = pygame.image.load("./images/background.png")
#blit绘制图像
screen.blit(bg, (0, 0))
#update更新屏幕显示
#pygame.display.update()

#绘制英雄飞机
hero = pygame.image.load("./images/me1.png")
screen.blit(hero, (200, 500))
pygame.display.update()

#创建时钟对象
clock = pygame.time.Clock()


#游戏循环:意味着游戏开始
i = 0

while True:
    #tick()方法可以指定时钟对象每秒钟运行的频率
    clock.tick(60)
    print(i)
    i += 1
    pass

pygame.quit()