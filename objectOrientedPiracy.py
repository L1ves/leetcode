class Ship:
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew
    # Your code here
    def is_worth_it(self):
        if (self.draft - self.crew * 1.5) > 20:
            return True
        return False


# class Ship:
#     def __init__(self, draft, crew):
#         self.draft = draft
#         self.crew = crew
#     # Your code here
#     def is_worth_it(self):
#         return self.draft - self.crew * 1.5 > 20