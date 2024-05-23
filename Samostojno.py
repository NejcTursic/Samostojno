import pygame
import random

class SnakeGame:
    def __init__(self):
        pygame.init()
        self.window_width = 800
        self.window_height = 600
        self.display_surf = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption('Kača')
        self.clock = pygame.time.Clock()
        self.snake = [(100, 100)]
        self.apple = self.spawn_apple()
        self.score = 0
        self.speed = 10
        self.font = pygame.font.Font(None, 36)

    def spawn_apple(self):
        return random.randrange(0, self.window_width, 10), random.randrange(0, self.window_height, 10)

    def move_snake(self, direction):
        head_x, head_y = self.snake[0]
        if direction == 'right':
            head_x += 10
        elif direction == 'left':
            head_x -= 10
        elif direction == 'up':
            head_y -= 10
        elif direction == 'down':
            head_y += 10
        self.snake.insert(0, (head_x, head_y))

    def check_collision(self):
        head = self.snake[0]
        if head == self.apple:
            self.apple = self.spawn_apple()
            self.score += 1
        else:
            self.snake.pop()

        if head in self.snake[1:]:
            pygame.quit()
            exit() 

    def draw_score(self):
        score_text = f"Score: {self.score}"
        text_surface = self.font.render(score_text, True, (255, 255, 255))
        self.display_surf.blit(text_surface, (10, 10))

    def run(self):
        running = True
        direction = 'right'

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        direction = 'right'
                    elif event.key == pygame.K_LEFT:
                        direction = 'left'
                    elif event.key == pygame.K_UP:
                        direction = 'up'
                    elif event.key == pygame.K_DOWN:
                        direction = 'down'

            self.move_snake(direction)
            self.check_collision()

            self.display_surf.fill((0, 0, 0))
            pygame.draw.rect(self.display_surf, (255, 0, 0), (*self.apple, 10, 10))
            for segment in self.snake:
                pygame.draw.rect(self.display_surf, (0, 255, 0), (*segment, 10, 10))

            self.draw_score()
            pygame.display.flip()
            self.clock.tick(self.speed)

if __name__ == "__main__":
    game = SnakeGame()
    game.run()