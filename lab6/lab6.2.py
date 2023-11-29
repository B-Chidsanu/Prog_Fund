
class ShoppingCart:
    def __init__(self, id):
        self.id = id
        self.books = []

    def add_book(self, book, n, total):
        value = 0
        if len(self.books) == 0:
            self.books.append([book, n, total])
        else:
            for add in self.books:
                if add[0] == book:
                    add[1] += n
                    break
                else:
                    value += 1
                    if value == len(self.books):
                        self.books.append([book, n, total])
                        break

    def delete_book(self, book):
        for dele in range(0, len(self.books)):
            if book in self.books[dele]:
                self.books.pop(dele)
                break

    def get_total(self):
        total = 0
        for cost in self.books:
            total += int(cost[2]) * int(cost[1])
        return total

    def __lt__(self, rhs):
        return self.get_total() < rhs.get_total()


chidshop = ShoppingCart(5555)
chickenshop = ShoppingCart(69)
chidshop.add_book('b1', 2, 15)
chidshop.add_book('b2', 3, 20)
chidshop.add_book('b1', 1, 15)
chidshop.add_book('b2', 2, 20)
chidshop.add_book('b3', 1, 30)
chidshop.add_book('b3', 2, 30)
chickenshop.add_book('b4', 2, 50)
print(chidshop > chickenshop)
chidshop.delete_book('b1')
print(chidshop.books)
print('ราคารวม =', chidshop.get_total(), 'บาท')
