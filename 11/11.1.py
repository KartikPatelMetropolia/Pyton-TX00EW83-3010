
class Publication:

    def __init__(self, name : str):
        self.name = name

    def print_information(self):
        print(f"Publication name: {self.name}",end = "")

class Magazine(Publication):

    def __init__(self, publication_name : str, name : str):
        self.editor_name = name
        super().__init__(publication_name)

    def print_information(self):
        super().print_information()
        print(f", Chief Editor : {self.editor_name}")

class Book(Publication):

    def __init__(self, publication_name : str, author_name : str, pages : int):
        self.author = author_name
        self.page_count = pages
        super().__init__(publication_name)

    def print_information(self):
        super().print_information()
        print(f", Author name : {self.author}, No.of.Pages : {self.page_count}")

magazine = Magazine("Donald Duck", "Aki Hyyppä")
book = Book("Compartment No. 6", "Rosa Liksom", 192)

magazine.print_information()
book.print_information()