import tkinter as tk
import random

# Game settings
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 600
BASKET_WIDTH = 80
BASKET_HEIGHT = 20
APPLE_RADIUS = 20
APPLE_SPEED = 6
BASKET_SPEED = 60

class CatchAppleGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Catch the Apple")
        self.canvas = tk.Canvas(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg="lightblue")
        self.canvas.pack()

        # Basket
        self.basket_x = WINDOW_WIDTH // 2 - BASKET_WIDTH // 2
        self.basket = self.canvas.create_rectangle(
            self.basket_x, WINDOW_HEIGHT - BASKET_HEIGHT - 10,
            self.basket_x + BASKET_WIDTH, WINDOW_HEIGHT - 10,
            fill="brown"
        )

        # Apple
        self.apple = None
        self.apple_x = 0
        self.apple_y = 0
        self.score = 0
        self.score_text = self.canvas.create_text(10, 10, anchor="nw", text="Score: 0", font=("Arial", 16))

        self.root.bind("<Left>", self.move_left)
        self.root.bind("<Right>", self.move_right)

        self.spawn_apple()
        self.update()

    def spawn_apple(self):
        self.apple_x = random.randint(APPLE_RADIUS, WINDOW_WIDTH - APPLE_RADIUS)
        self.apple_y = -APPLE_RADIUS
        if self.apple:
            self.canvas.delete(self.apple)
        self.apple = self.canvas.create_oval(
            self.apple_x - APPLE_RADIUS, self.apple_y - APPLE_RADIUS,
            self.apple_x + APPLE_RADIUS, self.apple_y + APPLE_RADIUS,
            fill="red"
        )

    def move_left(self, event):
        if self.basket_x > 0:
            self.basket_x -= BASKET_SPEED
            self.canvas.move(self.basket, -BASKET_SPEED, 0)

    def move_right(self, event):
        if self.basket_x < WINDOW_WIDTH - BASKET_WIDTH:
            self.basket_x += BASKET_SPEED
            self.canvas.move(self.basket, BASKET_SPEED, 0)

    def update(self):
        self.apple_y += APPLE_SPEED
        self.canvas.coords(
            self.apple,
            self.apple_x - APPLE_RADIUS, self.apple_y - APPLE_RADIUS,
            self.apple_x + APPLE_RADIUS, self.apple_y + APPLE_RADIUS
        )

        # Check for collision
        basket_top = WINDOW_HEIGHT - BASKET_HEIGHT - 10
        basket_bottom = WINDOW_HEIGHT - 10
        if (basket_top < self.apple_y + APPLE_RADIUS < basket_bottom and
            self.basket_x < self.apple_x < self.basket_x + BASKET_WIDTH):
            self.score += 1
            self.canvas.itemconfig(self.score_text, text=f"Score: {self.score}")
            self.spawn_apple()
        elif self.apple_y - APPLE_RADIUS > WINDOW_HEIGHT:
            self.spawn_apple()

        self.root.after(30, self.update)

if __name__ == "__main__":
    root = tk.Tk()
    game = CatchAppleGame(root)
    root.mainloop()