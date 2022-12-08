import tkinter as tk
from tkinter import ttk
import sqlite3

class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.db = db
        self.view_records()

    def init_main(self):
        toolbar = tk.Frame(bg='black',bd=2)
        toolbar.pack(side=tk.TOP,fill=tk.X)
        #Параметры кнопки для добавления данных
        btn_open_dialog = tk.Button(toolbar,text='Добавить данные', command=self.open_dialog,bg='green',bd=0,compound=tk.TOP)
        btn_open_dialog.pack(side=tk.RIGHT)
        #Кортеж из колонок для бд
        self.tree = ttk.Treeview(self, columns=('id', 'login', 'password', 'email'), height=15, show='headings')
        #Параметры колонок
        self.tree.column('id', width=50, anchor=tk.CENTER)
        self.tree.column('login', width=200, anchor=tk.CENTER)
        self.tree.column('password', width=200, anchor=tk.CENTER)
        self.tree.column('email', width=200, anchor=tk.CENTER)
        #Даем названия столбцов
        self.tree.heading('id',text='ID')
        self.tree.heading('login',text='Логин')
        self.tree.heading('password',text='Пароль')
        self.tree.heading('email',text='Почта')

        self.tree.pack()
    #Пишем данные в таблицу
    def records(self,login,password,email):
        self.db.insert_data(login,password,email)
    #автообновление данных
        self.view_records()
    #Извлекаем данные из таблицы laba9
    def view_records(self):
        self.db.c.execute('''SELECT * FROM laba9 ''')
        #Для очистки строки ввода
        [self.tree.delete(i) for i in self.tree.get_children()]
        #отображаем содержимое бд
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def open_dialog(self):
        Child()


class Child(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child()
        self.view = app
    #Параметры для окна добавляющего данные в бд
    def init_child(self):
        self.title('Добавить данные')
        self.geometry('400x220+400+300')
        self.resizable(False, False)
    #Подпись полей ввода
        label_login = ttk.Label(self, text='Логин:')
        label_login.place(x=108,y=50)
        label_password = ttk.Label(self, text='Пароль:')
        label_password.place(x=100,y=90)
        label_email = ttk.Label(self, text='Почта:')
        label_email.place(x=108,y=130)
    #Поля ввода данных
        self.entry_login = ttk.Entry(self)
        self.entry_login.place(x=150,y=50)
        self.entry_password = ttk.Entry(self)
        self.entry_password.place(x=150,y=90)
        self.entry_email = ttk.Entry(self)
        self.entry_email.place(x=150,y=130)
    #Кноки закрытия окна и добавления данных
        btn_cancel=ttk.Button(self,text='Закрыть окно',command=self.destroy)
        btn_cancel.place(x=100,y=180)
        btn_add=ttk.Button(self,text='Внести данные',command=self.destroy)
        btn_add.place(x=200,y=180)
        btn_add.bind('<Button-1>', lambda event: self.view.records(self.entry_login.get(),self.entry_password.get(),
                                                                   self.entry_email.get()))
    #Главное окно позади, не даем юзеру им пользоваться или закрывать.
        self.grab_set()
        self.focus_set()
#Параметры главного окна
class DB:
    def __init__(self):
        self.conn = sqlite3.connect('laba9.db')
        self.c = self.conn.cursor()
        self.c.execute(
            '''CREATE TABLE IF NOT EXISTS laba9 (id INTEGER PRIMARY KEY, login TEXT,password BLOB, email TEXT)'''
        )
        self.conn.commit()
    def insert_data(self, login, password, email):
        self.c.execute('''INSERT INTO laba9(login,password,email) VALUES (?,?,?)''', (login, password, email))
        self.conn.commit()
if __name__ == "__main__":
    root = tk.Tk()
    db = DB()
    app = Main(root)
    app.pack()
    root.title("Взаимодействие с БД")
    root.geometry("650x350+300+200")
    root.resizable(False, False)
    root.mainloop()