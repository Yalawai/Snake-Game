import pygame
import random

pygame.init()

WIDTH  = 1000
HEIGHT = 800
BOX_SIZE = 20
FPS = 15
FOOD_COLOR = "#ff0000"
SNAKE_COLOR = "#00ff00"

BACKGROUND_COLOR = "#000000"
STAT_FONT = pygame.font.SysFont("comicsans", 50)
 

    
        
    
class Snake:
    
    def __init__(self):
        self.x = WIDTH//2 - BOX_SIZE
        self.y = HEIGHT//2 - BOX_SIZE
        self.coordinates = []
        self.food_coordinates = []
        self.to_place = True
        self.direction = "up"
        self.score = 0
        self.body = 3
        factor = 0
        for _ in range(self.body):
            self.coordinates.append((self.x + BOX_SIZE * factor, self.y))
            factor += 1



    def draw(self, win):

        for x,y in self.coordinates:
            pygame.draw.rect(win, SNAKE_COLOR,(x, y, BOX_SIZE,BOX_SIZE), 1)
            
        text = STAT_FONT.render("SCORE:" + str(self.score), 1, (255,255,255))
        win.blit(text, (WIDTH - 10 - text.get_width(), 10))

        

    
            


    def move(self):
        
        
        self.coordinates.pop()

        x,y = self.coordinates[0]        
    
        if self.direction == "left":
            x1,y1 = x-BOX_SIZE, y 
        elif self.direction == "right":
            x1,y1 = x+BOX_SIZE, y 
        elif self.direction == "up":
            x1,y1 = x, y-BOX_SIZE 
        elif self.direction == "down":
            x1,y1 = x, y+BOX_SIZE 
        
        
        


        self.coordinates.insert(0, (x1, y1))
    
    def collision(self):
        if self.coordinates[0] in self.coordinates[1:] or self.coordinates[0][0] < 0 or self.coordinates[0][1] < 0 or self.coordinates[0][0] > WIDTH or self.coordinates[0][1] > HEIGHT:
            return True
        return False
    
    def place_food(self, win):
        
    
        
        while self.to_place:
            
            food_x = random.randrange(0, WIDTH, BOX_SIZE)
            food_y = random.randrange(0, HEIGHT, BOX_SIZE)
            if (food_x,food_y) not in self.coordinates:
                 self.food_coordinates.append((food_x,food_y))


                 self.to_place = False


        pygame.draw.rect(win, FOOD_COLOR, (self.food_coordinates[0][0], self.food_coordinates[0][1], BOX_SIZE, BOX_SIZE))
        
            
        
        if self.coordinates[0] == (self.food_coordinates[0][0], self.food_coordinates[0][1]):
            self.score += 1
            
         
            
            self.coordinates.append(self.coordinates[0])
            self.food_coordinates.pop()
            self.to_place = True
            print("TRUE")








def main():
    run = True
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("HISSS")
    clock = pygame.time.Clock()
    snake = Snake()

    

    
    
    while run:

        key = pygame.key.get_pressed()

        win.fill(BACKGROUND_COLOR)
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
        if key[pygame.K_UP] and snake.direction != "down":
            snake.direction = "up"
           

        if key[pygame.K_DOWN]and snake.direction != "up":
            snake.direction = "down"
            
        if key[pygame.K_LEFT] and snake.direction != "right":
            snake.direction = "left"
           


        if key[pygame.K_RIGHT] and snake.direction != "left":
            snake.direction = "right"
            
    
    

     
        snake.move()
        if snake.collision():
            run = False
        
        
        snake.place_food(win)
        snake.draw(win)
        pygame.display.update()

    

    pygame.quit()
    quit()



    
main()