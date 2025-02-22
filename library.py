'''
19122120
侯兆晗
'''

class Library:                                          # 定义一个名为Library的类，用于模拟图书馆借还书业务  
    # 初始化方法，为books和readers字典赋值  
    def __init__(self):  
        self.books = {}                                 # 用于存储所有图书的信息，键为图书ID，值为该图书的库存数量  
        self.readers = {}                               # 用于存储所有读者的信息，键为读者姓名，值为该读者的密码  
  
    # 定义一个方法用于注册读者，参数为读者姓名和密码  
    def register_reader(self, reader_name, password):  
        self.readers[reader_name] = password            # 在readers字典中添加读者信息  

    # 定义一个方法用于读者登录，参数为读者姓名和密码  
    def login(self, reader_name, password):  
        if reader_name in self.readers and self.readers[reader_name] == password:  # 判断读者是否存在且密码是否正确  
            print('登录成功')
            return True                                 # 如果验证通过，返回True  
        else:
            print('登录失败')
            return False                                # 如果验证不通过，返回False  

    # 定义一个方法用于借书，参数为图书ID和读者姓名
    def borrow_book(self, book_id, reader_name):  
        if book_id in self.books:                       # 判断图书是否存在  
            self.books[book_id] -= 1                    # 如果图书存在，库存减1  
            print(f"Reader {reader_name} borrowed book {book_id}.")  # 打印借书信息  
            return True                                 # 借书成功，返回True  
        else:  
            print("Book not available.")                # 如果图书不存在，打印提示信息  
            return False                                # 借书失败，返回False  

    # 定义一个方法用于还书，参数为图书ID和读者姓名  
    def return_book(self,book_id,reader_name):  
        if book_id in self.books:                       # 判断图书是否存在  
            self.books[book_id] += 1                    # 如果图书存在，库存加1  
            print(f"Reader {reader_name} returned book {book_id}.")  # 打印还书信息  
            return True                                 # 还书成功，返回True  
        else:  
            print("Book not found.")                    # 如果图书不存在，打印提示信息  
            return False                                # 还书失败，返回False  
  
    # 定义一个方法用于打印所有图书的库存情况以及每个读者的已借图书数量  
    def print_books(self):  
        for book in self.books:                         # 遍历所有图书  
            print(f"Book {book}: {self.books[book]} copies available.")  # 打印图书库存信息  
        print("----------------------")                 # 打印分隔线  
        for reader in self.readers:                     # 遍历所有读者  
            print(f"Reader {reader}: {self.readers[reader]} books borrowed.")  # 打印每个读者的已借图书数量

	#借还书查询  
    # 定义一个方法用于查询读者的借阅记录  
    def query_reader_borrow_records(self, reader_name):  
        if reader_name in self.readers:                 # 判断读者是否存在  
            borrow_records = []                         # 初始化借阅记录列表  
            for book_id in self.books:                  # 遍历所有图书ID  
                if self.books[book_id] > 0:             # 判断图书库存是否大于0，即图书是否已被借出  
                    if reader_name in self.readers:     # 判断读者是否已借该图书  
                        borrow_records.append(f"Reader {reader_name} borrowed book {book_id} on {self.readers[reader_name]}")  # 将借阅记录添加到列表中  
            return borrow_records                       # 返回借阅记录列表  
        else:  
            print("Invalid reader.")                    # 如果读者不存在，打印提示信息  
            return []                                   # 返回空列表  
  
    # 定义一个方法用于查询馆内图书流通情况  
    def query_book_circulation(self):  
        circulation_records = []                        # 初始化流通记录列表  
        for book_id in self.books:                      # 遍历所有图书ID  
            if self.books[book_id] > 0:                 # 判断图书库存是否大于0，即图书是否已被借出  
                borrowed_by = [reader for reader in self.readers if book_id in self.readers[reader]]  # 获取借阅该图书的所有读者  
                for reader in borrowed_by:              # 遍历借阅该图书的读者  
                    circulation_records.append(f"Book {book_id} is currently borrowed by {reader}.")  # 将流通记录添加到列表中  
        return circulation_records                      # 返回流通记录列表  
  
    # 定义一个方法用于查询读者借还书情况  
    def query_reader_borrow_return(self, reader_name):  
        if reader_name in self.readers:                 # 判断读者是否存在  
            borrow_records = [f"Book {book_id} borrowed on {self.readers[reader_name]}"]  # 初始化借阅记录列表  
            return borrow_records                       # 返回借阅记录列表  
        else:  
            print("Invalid reader.")                    # 如果读者不存在，打印提示信息  
            return []                                   # 返回空列表 

	#预约服务  
    # 定义一个方法用于读者预约图书  
    def reserve_book(self, reader_name, book_id):  
        if reader_name in self.readers and book_id in self.books:  # 判断读者和图书是否存在  
            if self.books[book_id] > 0:                 # 判断图书库存是否大于0  
                self.books[book_id] -= 1                # 预约成功，库存减1  
                print(f"Reader {reader_name} successfully reserved book {book_id}.")  # 打印预约成功信息  
                return True                             # 预约成功，返回True  
            else:  
                print("The book is out of stock.")      # 如果图书库存不足，打印提示信息  
                return False                            # 预约失败，返回False  
        else:
            print("Invalid reader or book.")            # 如果读者或图书不存在，打印提示信息  
            return False                                # 预约失败，返回False  
  
    #逾期罚款  
    # 定义一个方法用于计算逾期天数并生成罚款记录  
    def calculate_fine(self, reader_name, book_id, overdue_days):  
        fine = overdue_days * 0.5                       # 假设每天的罚款金额为0.5元  
        fine_record = f"Reader {reader_name} owes a fine of {fine} yuan for overdue book {book_id} for {overdue_days} days."  # 生成罚款记录  
        return fine, fine_record                        # 返回罚款金额和罚款记录

    #定义一个方法用于注册新书，参数为书名
    def register_book(self, book_id):  
        if book_id not in self.books:  
            self.books[book_id] = 2                     # 初始库存为2  
            print(f"Book {book_id} has been registered.")  
        else:  
            print("The book is already registered.")

#调用
library = Library()                                   # 创建Library类实例
library.register_book("book1")                        # 注册新图书book1
library.register_book("book2")                        # 注册新图书book2 
library.register_reader("Alice", "password123")       # 注册读者   

print('登录！')
library.login("Alice","password123")                  # 登录读者   

library.borrow_book("book1","Alice")                  # 借书  

print('查询读者借阅记录')
print(library.query_reader_borrow_records("Alice"))   # 查询读者借阅记录  

print('查询图书流通情况')
print(library.query_book_circulation())               # 查询图书流通情况

print('打印所有图书的库存情况以及每个读者的已借图书数量')
print(library.print_books())                          # 打印所有图书的库存情况以及每个读者的已借图书数量  

print('查询图书流通情况')
print(library.query_book_circulation())               # 查询图书流通情况（包括新注册的图书）  

print('查询读者借还书情况')
print(library.query_reader_borrow_return("book1"))    # 查询读者借还书情况

library.return_book("book1","Alice")                  # 还书

print("预约图书")
library.reserve_book("Alice", "book2")                # 预约图书  

print("查询预约情况")
print(library.reserve_book("Alice", "book2"))         # 查询预约情况  

# 逾期罚款（假设逾期归还图书）  
overdue_days = 5                                      # 逾期天数  
fine, fine_record = library.calculate_fine("Alice", "book2", overdue_days)  
print("打印罚款记录")
print(fine_record)                                    # 打印罚款记录

