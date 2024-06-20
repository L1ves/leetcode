class Guesser:
    def __init__(self, number, lives):
        self.number = number
        self.lives = lives

    def guess(self, n):
        self.n = n
        if self.lives <= 0:
            raise ValueError("No more lives left. Game over!")
        if self.n == self.number:
            return True
        if self.n != self.number:
            self.lives -= 1
            return False
