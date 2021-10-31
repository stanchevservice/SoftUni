#1.Брой страници в текущата книга – цяло число;
#2.Страници, които може да прочита за 1 час – цяло число;
#3.Броя на дните, за които трябва да прочете книгата – цяло число

book_page=int(input())
page_read_per_day=int(input())
days=int(input())

aurs_per_day=(book_page/page_read_per_day)/days

print(aurs_per_day)