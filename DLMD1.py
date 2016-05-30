

import pygame
pygame.init()

height = 600
width = 800



gameDisplay = pygame.display.set_mode((width, height))

pygame.display.set_caption("Don't Lose my Doge")
rect = ((0, 20, 30, 40))
clock = pygame.time.Clock()
guyImg2 = pygame.image.load('Odddoge2.png')
guyImg = pygame.image.load('Odddoge1.png')
menuImg = pygame.image.load('menu1.png')
parkImg = pygame.image.load('park.jpg')
def guy(x,y):
    gameDisplay.blit(guyImg,(x,y))
def menuimg():
    gameDisplay.blit(menuImg,(0,0))
def park(xp,yp):
    gameDisplay.blit(parkImg,(xp,yp))
myfont = pygame.font.SysFont("monospace", 15)

time = 0.0
def firsttime ():
    global time
    global ltime
    ltime = str(time)
    return ltime
def guy2(xl,yl):
    gameDisplay.blit(guyImg2,(xl,yl))
global best
best = 0.0
def ttime():
    label = myfont.render(ltime, 1, (255,255,0))
    gameDisplay.blit(label, (100, 100))
def tttime():
    label = myfont.render(ltime, 1, (255,255,0))
    gameDisplay.blit(label, (100, 450))
def timebest():
    global best
    global time
    def ques():
        global best
        global time
        if time >= best:
            best = time
    ques()
    bests = str(best)
    label = myfont.render(bests, 1, (255,255,0))
    gameDisplay.blit(label, (100, 300))
    return best
def gametime():
    global time
    time += 0.0165
    return time
def zerotime():
    global time
    time = 0
    return time
def menu():
    ended = False


    while not ended:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ended = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RETURN:
                    game()
                if event.key == pygame.K_SPACE:
                    game2()
                if event.key == pygame.K_BACKSPACE:
                    ended = True
        menuimg()
        firsttime()
        tttime()
        timebest()
        #gameDisplay.fill((255,255,255))
        pygame.display.update()
        clock.tick(60)
def game2():
    xp = 0
    yp = 0
    x = (width * 0.6)
    y = (height * 0.6)
    xl = (width * 0.6)
    yl = (height * 0.6)
    zerotime()
    xt_change = 1.0
    yt_change = 1.0
    y_change = 1.0
    x_change = 1.0
    xtl_change = 1.0
    ytl_change = 1.0
    yl_change = 1.0
    xl_change = 1.0
    ended = False
    rspeed = 1.0
    gspeed = 25
    while not ended:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ended = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -gspeed
                elif event.key == pygame.K_RIGHT:
                    x_change = gspeed
                elif event.key == pygame.K_UP:
                    y_change = -gspeed
                elif event.key == pygame.K_DOWN:
                    y_change = gspeed
                if event.key == pygame.K_a:
                    xl_change = -gspeed
                elif event.key == pygame.K_d:
                    xl_change = gspeed
                elif event.key == pygame.K_w:
                    yl_change = -gspeed
                elif event.key == pygame.K_s:
                    yl_change = gspeed
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0
                elif event.key == pygame.K_a or event.key == pygame.K_d:
                    xl_change = 0
                elif event.key == pygame.K_w or event.key == pygame.K_s:
                    yl_change = 0
            if x > 300:
                xt_change = rspeed
            if x < 300:
                xt_change = -rspeed
            if y > 200:
                yt_change = rspeed
            if y < 200:
                yt_change = -rspeed
            if xl > 300:
                xtl_change = rspeed
            if xl < 300:
                xtl_change = -rspeed
            if yl > 200:
                ytl_change = rspeed
            if yl < 200:
                ytl_change = -rspeed
            #print(event)
        if x > width + 20or x < -155:
            ended = True
        if y > height + 20 or y < -260:
            ended = True
        if xl > width + 20or xl < -155:
            ended = True
        if yl > height + 20 or yl < -260:
            ended = True

        y += y_change
        y += yt_change
        x += x_change
        x += xt_change
        yl += yl_change
        yl += ytl_change
        xl += xl_change
        xl += xtl_change
        #gameDisplwaay.fill((255,255,255))
        park(xp,yp)
        rspeed += 0.005
        guy(x,y)
        guy2(xl,yl)
        firsttime()
        gametime()
        ttime()
        pygame.display.update()
        clock.tick(60)
def game():
    zerotime()
    xp = 0
    yp = 0
    x = (width * 0.6)
    y = (height * 0.6)


    xt_change = 1.0
    yt_change = 1.0
    y_change = 0
    x_change = 0

    ended = False
    rspeed = 1.0
    gspeed = 25
    while not ended:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ended = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -gspeed
                elif event.key == pygame.K_RIGHT:
                    x_change = gspeed
                elif event.key == pygame.K_UP:
                    y_change = -gspeed
                elif event.key == pygame.K_DOWN:
                    y_change = gspeed

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0

            if x > 300:
                xt_change = rspeed
            if x < 300:
                xt_change = -rspeed
            if y > 200:
                yt_change = rspeed
            if y < 200:
                yt_change = -rspeed

            #print(event)
        if x > width + 20or x < -155:
            ended = True
        if y > height + 20 or y < -260:
            ended = True

        y += y_change
        y += yt_change
        x += x_change
        x += xt_change
        firsttime()
        #gameDisplwaay.fill((255,255,255))
        park(xp,yp)
        #time += 0.0165
        rspeed += 0.005
        guy(x,y)
        gametime()
        ttime()
        pygame.display.update()
        clock.tick(60)

menu()
pygame.quit()
print time
quit()

