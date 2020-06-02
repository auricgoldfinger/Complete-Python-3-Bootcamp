class Book():
    def __init__(self,title,author,pages):
        self.title=title
        self.author=author
        self.pages=pages

    def __str__(self):
        return f"{self.title} ({self.pages}p) by {self.author}"

    def __len__(self):
        return self.pages

    def __del__(self):
        print("Nooo I was too cute. Goodbye cruel world")

b = Book('Hello', "Bert", 209)
print(len(b))
print(b)
del b