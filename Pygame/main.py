import random
import time
import pygame
pygame.init()

global menu
ultraColor = (20,200,140)
ultraRed = (150,0,100)
ultraLemon = (200,255,100)
ultraBlue = (100,50,255)
def main_menu():
    menu = True
    selected = 'start'
    while menu:
        sf.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    selected = 'quit'
                if event.key == pygame.K_UP:
                    selected = 'start'
                if event.key == pygame.K_RETURN:
                    if selected == 'start':
                        menu = False
                        return True
                    else:
                        return False

        tf = pygame.font.SysFont('Comic Sans Ms', 90)
        title = tf.render('Warm And Apples',True, ultraBlue)
        mf1 = pygame.font.SysFont('Comic Sans Ms', 70)
        mf2 = pygame.font.SysFont('Comic Sans Ms', 50)
        if selected == 'start':
            start = mf1.render('Start Dinner', True, ultraLemon)
        else:
            start = mf1.render('Start Dinner', True, ultraBlue)
        if selected == 'quit':
            quitBut = mf2.render('Do you want to quit?', True, ultraRed)
        else:
            quitBut = mf2.render('Do you want to quit?', True, ultraBlue)

        sf.blit(title, (display_x/2-400, 100))
        sf.blit(start, (display_x / 2 - 400, 285))
        sf.blit(quitBut, (display_x / 2 - 400, 450))

        clock.tick(fps)
        pygame.display.update()
class Snake:
    def __init__(self,posx,posy,ultraColor,sf,display_x,display_y):
        self.sf = sf
        self.display_x = display_x
        self.display_y = display_y
        self.color = ultraColor
        self.speed = 20
        self.posx = posx
        self.posy = posy
        self.draw = True
        self.eated = False
        self.dir_x = 1  # -1 0 1
        self.dir_y = 0  # -1
        #   0
        #   1
        self.count = 1
        self.heads = []
        self.add_head()

    def set(self):
        self.draw = True
        self.eated = False
        self.dir_x = 1 #-1 0 1
        self.dir_y = 0 #   -1
                       #   0
                       #   1
        self.count = 1
        self.heads = []
        self.add_head()
        self.color = ultraColor
        self.posy = snake_y
        self.posx = snake_x
    def change_color(self):
        colors = [ultraColor,ultraRed,ultraBlue,ultraLemon]
        self.color = random.choice(colors)
    def add_head(self):
        self.heads.append(Snake_head(self.posx,self.posy,self.speed,self.color,self.sf,self.display_x,self.display_y))
    def remove_head(self):
        if len(self.heads) > self.count:
            self.heads.pop(0)
    def draw_(self):
        for head in self.heads:
            head.draw_(self.sf)
    def move(self):
        if self.dir_x == 1:
            self.posx = self.posx + self.speed
        if self.dir_x == -1:
            self.posx = self.posx - self.speed
        if self.dir_y == -1:
            self.posy = self.posy - self.speed
        if self.dir_y == 1:
            self.posy = self.posy + self.speed
        self.add_head()
        self.remove_head()
    def move_right(self):
        if self.count == 1:
            self.dir_x = 1
            self.dir_y = 0
        else:
            if self.dir_y:
                self.dir_x = 1
                self.dir_y = 0
    def move_up(self):
        if self.count == 1:
            self.dir_x = 0
            self.dir_y = -1
        else:
            if self.dir_x:
                self.dir_x = 0
                self.dir_y = -1
    def move_left(self):
        if self.count == 1:
            self.dir_x = -1
            self.dir_y = 0
        else:
            if self.dir_y:
                self.dir_x = -1
                self.dir_y = 0
    def move_down(self):
        if self.count == 1:
            self.dir_x = 0
            self.dir_y = 1
        else:
            if self.dir_x:
                self.dir_x = 0
                self.dir_y = 1
    def check_walls(self):
        if self.posx <= 0 or self.posx >= self.display_x - 10 or self.posy <= 0 or self.posy >= self.display_y - 10:
            return False
        else:
            return True
    def check_snake(self):
        for i in range(len(self.heads)):
            if i != len(self.heads) - 1:
                if self.posx == self.heads[i].posx and self.posy == self.heads[i].posy:
                    return False
        return True
    def eating(self,food_x,food_y):
        self.food_x = food_x
        self.food_y = food_y
        if food_x+20 >= snake.posx >= food_x and food_y+20 >= snake.posy >= food_y:
            self.draw = False
            self.eated = True
class Snake_head:
    def __init__(self,posx,posy,speed,ultraColor,sf,display_x,display_y):
        self.sf = sf
        self.display_x = display_x
        self.display_y = display_y
        self.color = ultraColor
        self.speed = speed
        self.posx = posx
        self.posy = posy
        self.draw = True
        self.eated = False
        self.dir_x = 1 #-1 0 1
        self.dir_y = 0 #   -1
                       #   0
                       #   1
    def change_color(self):
        colors = [ultraColor,ultraRed,ultraBlue,ultraLemon]
        self.color = random.choice(colors)

    def draw_(self,surface):
        pygame.draw.rect(surface, self.color, (self.posx, self.posy, 20, 20))


snake_x = 20
snake_y = 20
food_x = 1000
food_y = 780
display_x = 1920
display_y = 1060
pygame.display.set_caption('War for colonies')
sf = pygame.display.set_mode((display_x,display_y))
clock = pygame.time.Clock()
fps = 15
f1 = pygame.font.Font(None,50)

GAMEOVER = f1.render('GAMEOVER',True,ultraLemon)


keyupd = False
keydownd = False
keyleftd = False
keyrightd = False

snake = Snake(snake_x,snake_y,ultraColor, sf, display_x, display_y)



haveadinner = main_menu()

while haveadinner:
    sf.fill((0, 0, 0))
    f2 = pygame.font.Font(None, 250)
    score = f1.render(str(snake.count), True, ultraLemon)
    sf.blit(score,(1700,20))

    quitInMenu = False
    quitInMenu_ns = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                keyrightd = True
            if event.key == pygame.K_a:
                keyleftd = True
            if event.key == pygame.K_w:
                keyupd = True
            if event.key == pygame.K_s:
                keydownd = True
            if event.key == pygame.K_ESCAPE:
                quitInMenu = True
            if event.key == pygame.K_TAB:
                quitInMenu_ns = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                keyrightd = False
            if event.key == pygame.K_a:
                keyleftd = False
            if event.key == pygame.K_w:
                keyupd = False
            if event.key == pygame.K_s:
                keydownd = False
    if quitInMenu == True:
        main_menu()
    if quitInMenu_ns == True:
        main_menu()
        snake_x = 20
        snake_y = 20
        snake.set()
        food_x = 1000
        food_y = 780
        display_x = 1920
        display_y = 1060
        clock = pygame.time.Clock()
        fps = 15
    if keyrightd == True:
        snake.move_right()
    if keyleftd == True:
        snake.move_left()
    if keyupd == True:
        snake.move_up()
    if keydownd == True:
        snake.move_down()
    snake.move()
    snake.check_snake()
    snake.eating(food_x,food_y)
    if snake.draw == True:
        pygame.draw.rect(sf, ultraRed, (food_x, food_y, 20, 20))
    if snake.eated == True:
        snake.change_color()
        fps = 15 + snake.count // 3
        snake.eated = False
        snake.draw = True
        snake.count = snake.count + 1
        repeat = True
        while repeat == True:
            repeat = False
            food_x = 20 * random.randint(0,display_x) % display_x
            food_y = 20 * random.randint(0,display_y) % display_y
            for anyHead in snake.heads:
                if anyHead.posx == food_x and anyHead.posy == food_y:
                    repeat = True
    if snake.check_snake() == False or snake.check_walls() == False:
        haveadinner = False
    snake.draw_()

    clock.tick(fps)
    pygame.display.update()

sf.blit(GAMEOVER,(300,400))
pygame.display.update()
time.sleep(1)