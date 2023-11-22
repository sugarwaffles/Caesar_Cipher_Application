import turtle

class CaesarCipherVisualizer:
    def __init__(self, shift):
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.shifted_alphabet = self.shift_alphabet(shift)
        self.window = turtle.Screen()
        self.window.bgcolor("white")
        self.cipher_turtle = turtle.Turtle()
        self.cipher_turtle.speed(0)  # Set a faster speed

    def shift_alphabet(self, shift):
        return self.alphabet[shift:] + self.alphabet[:shift]

    def draw_letter(self, letter, angle, radius, color):
        self.cipher_turtle.penup()
        self.cipher_turtle.setheading(angle)
        self.cipher_turtle.forward(radius)
        self.cipher_turtle.pendown()
        self.cipher_turtle.color(color)
        self.cipher_turtle.write(letter, align="center", font=("Arial", 12, "normal"))
        self.cipher_turtle.penup()
        self.cipher_turtle.backward(radius)
        self.cipher_turtle.pendown()

    def draw_caesar_cipher(self):
        for i in range(26):
            angle = -i * 360 / 26
            self.draw_letter(self.alphabet[i], angle, 120, "black")

        for i in range(26):
            angle = -i * 360 / 26
            self.draw_letter(self.shifted_alphabet[i], angle, 150, "red")

        self.window.mainloop()

# Test the class with a shift of 3
visualizer = CaesarCipherVisualizer(3)
visualizer.draw_caesar_cipher()









