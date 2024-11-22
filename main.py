class Book:
  def __init__(self, title: str, author: str, price: float, quantity: int):
    self.title = title
    self.author = author
    self.price = price
    self.quantity = quantity

  def apply_discount(self, discount_percentage: float):
    self.price = self.price * (1 - discount_percentage)

  def sell(self, amount: int):
    if self.quantity >= amount:
      self.quantity -= amount
    else:
      print("Not enough books")

  def __str__(self):
    return f"Title: {self.title} Author: {self.author}, Price: {self.price}, Quantity: {self.quantity}"

class BookStore:
  def __init__(self, books: list[str]):
    self.books = []

  def add_book(self, book):
    for i in self.books:
      if i.title == book.title and i.author == book.author:
        i.quantity += book.quantity
        return f"Book {book.title} updated its quantity to {i.quantity}."
    self.books.append(book)
    return f"Book {book.title} added. Quantity: {book.quantity}"

  def search(self, query):
    result = []
    for i in self.books:
      if query.lower() in i.title.lower() or query.lower() in i.author.lower():
        result.append(i)
    return result

  def calculate_total_value(self):
    sum = 0
    for i in self.books:
      sum += i.price * i.quantity
    return f"Total value: {sum}"

book1 = Book("1984", "George Orwell", 10.99, 7)
book2 = Book("The Great Gatsby", "F. Scott Fitzgerald", 13.99, 3)

store = BookStore([])
print(store.add_book(book1))
print(store.add_book(book2))


book1.apply_discount(0.1)
print(f"New price for '{book1.title}': {book1.price}")

book1.sell(3)
print(f"Quantity of '{book1.title}': {book1.quantity}")
print(store.calculate_total_value())

search_results = store.search("1984")
print("\nSearch results for '1984':")
for book in search_results:
    print(book)