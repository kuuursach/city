import os
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from Script import config as cg
from Library import work
from Library import invalid
from tkinter import Entry

import matplotlib.pyplot as plt


import matplotlib
matplotlib.use("TkAgg")

from matplotlib.backends.backend_tkagg import FigureCanvasAgg, NavigationToolbar2Tk, FigureCanvasTkAgg
from matplotlib.figure import Figure



class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)

        self.add_img_modify = tk.PhotoImage(file="../Graphics/add2.png")
        self.add_img_cancel = tk.PhotoImage(file="../Graphics/add1.png")
        self.add_img = tk.PhotoImage(file="../Graphics/add.png")
        self.save_img = tk.PhotoImage(file="../Graphics/save.png")
        self.graph_img = tk.PhotoImage(file="../Graphics/graph.png")
        self.search_img = tk.PhotoImage(file="../Graphics/search.png")

        self.set_frame(root).pack(anchor='n')
        self.tree = self.init_main(root)
        self.tree.pack()
        self.fill_on_start()
        # self.find()

    def init_main(self, root):
        tree = ttk.Treeview(root, height=30, show='headings')
        tree['columns'] = ('Town', 'Founded', 'Population', 'Federal_subject', 'Population_area')

        tree.column("Town", width=200, anchor=tk.CENTER)
        tree.column("Founded", width=200, anchor=tk.CENTER)
        tree.column("Population", width=175, anchor=tk.CENTER)
        tree.column("Federal_subject", width=200, anchor=tk.CENTER)
        tree.column("Population_area", width=175, anchor=tk.CENTER)

        tree.heading("Town", text='Город')
        tree.heading("Founded", text='Год основания')
        tree.heading("Population", text='Население_города')
        tree.heading("Federal_subject", text='Субъект РФ')
        tree.heading("Population_area", text='Население_области')

        tree.bind('<Double-Button-1>', lambda event: self.change_town())

        return tree

    def set_frame(self, root):
        toolbar = tk.Frame(bg='#d7d8e0', bd=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        btn_open_dialog_cancel = tk.Button(toolbar, text='Удалить', command=self.delete_item, bg='#d7d8e0', bd=0,
                                           compound=tk.TOP, image=self.add_img_cancel)

        btn_open_dialog = tk.Button(toolbar, text='Добавить позицию', command=self.change_town, bg='#d7d8e0', bd=0,
                                    compound=tk.TOP, image=self.add_img)

        btn_open_dialog_modify = tk.Button(toolbar, text='Изменить', command=self.change_town, bg='#d7d8e0', bd=0,
                                           compound=tk.TOP, image=self.add_img_modify)

        btn_open_dialog_save = tk.Button(toolbar, text='Сохранить', bg='#d7d8e0', command=self.save, bd=0,
                                         compound=tk.TOP, image=self.save_img)

        btn_open_dialog_graph = tk.Button(toolbar, text='Графики', bg='#d7d8e0', command=self.graph_selector, bd=0,
                                          compound=tk.TOP, image=self.graph_img)

        btn_open_dialog_search = tk.Button(toolbar, text='Поиск', bg='#d7d8e0', command=self.graph_selector, bd=0,
                                           compound=tk.TOP, image=self.search_img)

        btn_open_dialog.pack(side=tk.LEFT)

        btn_open_dialog_cancel.pack(side=tk.LEFT)
        btn_open_dialog_modify.pack(side=tk.LEFT)
        btn_open_dialog_save.pack(side=tk.LEFT)
        btn_open_dialog_graph.pack(side=tk.LEFT)
        btn_open_dialog_search.pack(side=tk.LEFT)

        return toolbar

    def save(self):
        work._save_dataframe()

    def change_town(self):
        top = tk.Toplevel()
        top.title('Изменить/добавить город')
        top.geometry('520x280+400+300')
        top.resizable(False, False)

        label_town = tk.Label(top, text='Город:')
        label_town.place(x=50, y=50)
        entry_town = ttk.Entry(top)
        entry_town.place(x=200, y=50)

        label_founded = tk.Label(top, text='Год основания:')
        label_founded.place(x=50, y=80)
        entry_founded = ttk.Entry(top)
        entry_founded.place(x=200, y=80)

        label_population = tk.Label(top, text='Население:')
        label_population.place(x=50, y=110)
        entry_population = ttk.Entry(top)
        entry_population.place(x=200, y=110)

        label_federal = tk.Label(top, text='Субъект РФ:')
        label_federal.place(x=50, y=140)
        entry_federal = ttk.Entry(top)
        entry_federal.place(x=200, y=140)

        label_population_area = tk.Label(top, text='Население_области:')
        label_population_area.place(x=50, y=170)
        entry_population_area = ttk.Entry(top)
        entry_population_area.place(x=200, y=170)

        self.find(entry_town, entry_founded, entry_population, entry_federal, entry_population_area, self.tree)

        btn_cancel = ttk.Button(top, text='Закрыть', command=top.destroy)
        btn_cancel.place(x=300, y=210)

        btn_ok = ttk.Button(top, text='Изменить')
        btn_ok.place(x=220, y=210)
        btn_ok.bind('<Button-1>', lambda event: self.change_item(entry_town, entry_founded, entry_population,
                                                                 entry_federal, entry_population_area, self.tree))
        btn_ok = ttk.Button(top, text='Добавить')
        btn_ok.place(x=140, y=210)
        btn_ok.bind('<Button-1>', lambda event: self.add_item(entry_town, entry_founded, entry_population,
                                                              entry_federal, entry_population_area))

        top.grab_set()
        top.focus_set()

    def fill_on_start(self):
        for row in work.get_records():
            self.tree.insert("", tk.END, values=row)

    def delete_item(self):
        item = self.tree.focus()
        print(item)
        work.delete_record(self.tree.index(item))
        self.tree.delete(item)

    def find(self, entry_town, entry_founded, entry_population, entry_federal, entry_population_area, tree):
        values = tree.item(tree.focus())["values"]
        print(values)
        entries_list = [entry_town, entry_founded, entry_population, entry_federal, entry_population_area]
        for entry, val in zip(entries_list, values):
            # entry.delete(0, tk.END)
            # print(entry.delete(0, tk.END))
            entry.insert(0, val)
        # print(val)

    def change_item(self, entry_town, entry_founded, entry_population, entry_federal, entry_population_area, tree):
        try:

            item = tree.focus()
            index = tree.index(item)
            # values = tree.item(item)["values"]
            # print(values)
            # entries_list = [entry_town, entry_federal, entry_founded, entry_population, entry_area]
            # for entry, val in zip(entries_list, values):
            #     entry.delete(0, tk.END)
            #     entry.insert(0, val)

            print(item)
            print(index)

            town = invalid.invalid_text(entry_town.get())
            print(town)
            founded = invalid.invalid_number(entry_founded.get())
            print(founded)
            population = invalid.invalid_number(entry_population.get())
            print(population)
            federal = invalid.invalid_text(entry_federal.get())
            print(federal)
            population_area = invalid.invalid_number(entry_population_area.get())
            print(population_area)

            work.insert_record({
                "Town": town,
                "Founded": founded,
                "Population": population,
                "Federal_subject": federal,
                "Population_area": population_area
            })
            # work.update_record(index, (town, federal, founded, population, area))
            tree.item(item, values=(town, founded, population, federal, population_area))

            messagebox.showinfo(title='Успешно', message='Successful!!')
        except ValueError:
            messagebox.showerror("Invalid input", "Input are not valid string or number")

    def add_item(self, entry_town, entry_founded, entry_population, entry_federal, entry_population_area):
        try:

            town = invalid.invalid_text(entry_town.get())
            print(town)
            founded = invalid.invalid_number(entry_founded.get())
            print(founded)
            population = invalid.invalid_number(entry_population.get())
            print(population)
            federal = invalid.invalid_text(entry_federal.get())
            print(federal)
            population_area = invalid.invalid_number(entry_population_area.get())
            print(population_area)

            work.insert_record({
                "Town": town,
                "Founded": founded,
                "Population": population,
                "Federal_subject": federal,
                "Population_area": population_area
            })
            self.tree.insert("", tk.END, values=(town, founded, population, federal, population_area))

            messagebox.showinfo(title='Успешно', message='Successful!!')
        except ValueError:
            messagebox.showerror("Invalid input", "Input are not valid string or number")

    def graph_selector(self):
        popup = tk.Toplevel()
        popup.title('Выбор типа графика')
        popup.geometry('400x250')
        button_task1 = tk.Button(
            popup,
            text='Кластеризованная столбчатая диаграмма',
            command=lambda: self.graph_town_task1()
        )
        button_task1.pack()
        button_task4 = tk.Button(
            popup,
            text='Категоризированная диаграмма рассеивания',
            command=lambda: self.graph_town_task4()
        )
        button_task4.pack()
        button_not_implemented = tk.Button(
            popup,
            text='Not implemented',
            command=lambda: print('Not implemented')
        )
        button_not_implemented.pack()

    def save_graph(self, graph: plt.Figure):
        filename = tk.filedialog.asksaveasfilename(
            filetypes=[
                ('PDF', '*.pdf'),
                ('PNG', '*.png'),
                ('All files', '*.*')
            ]
        )
        do_continue = True
        if os.path.exists(filename):
            do_continue = tk.messagebox.askokcancel(message='Файл существует, заменить?')
            if not do_continue:
                os.remove(filename)
        if do_continue:
            try:
                graph.savefig(filename)
            except Exception as e:
                tk.messagebox.showerror(message='Exception: {}'.format(e))
            else:
                tk.messagebox.showinfo(message='Plot saved as {}'.format(filename))

    def graph_town_task4(self):
        graph = tk.Toplevel()
        graph.title('Население городов, по убыванию')
        graph.geometry('1366x768')
        graph.resizable(False, False)

        f = plt.Figure()
        prev_dx = 0
        for dx in [1861, 2000]:
            data = work.suffer[(prev_dx <= work.suffer['Founded']) & (work.suffer['Founded'] < dx)]
            sub = f.add_subplot(1, 2, dx > 1861 and 2 or 1)
            sub.scatter(
                data['Founded'],
                data['Population']
            )
            sub.set_ylim(top=1.3e7)
            sub.set_yticks(range(0, int(1.3e7), int(5e5)))
            sub.set_yticklabels([])
            sub.yaxis.grid(True)
            prev_dx = dx

        f.get_axes()[0].title.set_text('До отмены крепостного права')
        f.get_axes()[1].title.set_text('После отмены крепостного права')
        f.get_axes()[0].set_yticklabels(range(0, int(1.3e7), int(5e5)))

        canvas = FigureCanvasTkAgg(f, graph)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        save_button = tk.Button(graph, text='Save to file', command=lambda: self.save_graph(f))
        save_button.pack(side='top')

    def graph_town_task1(self):
        graph = tk.Toplevel()
        graph.title('Население городов с группировкой по дате основания')
        graph.geometry('1366x768')
        graph.resizable(False, False)

        f = plt.Figure()
        sub = f.add_subplot(1, 1, 1)
        prev_dx = 0
        add = {
            1861: 0.05,
            2000: 0.35
        }
        xticks = [], []
        for dx in [1861, 2000]:
            data = work.suffer[(prev_dx <= work.suffer['Founded']) & (work.suffer['Founded'] < dx)]\
                .sort_values('Population', ascending=False)
            sub.bar(
                [x + add[dx] for x in range(data.index.size)],
                data['Population'],
                width=0.2,
                label='{} отмены крепостного права'.format(dx == 1861 and 'До' or 'После')
            )
            xticks[0].extend([x + add[dx] for x in range(data.index.size)])
            xticks[1].extend(data['Town'])
            sub.set_ylim(top=1.3e7)
            sub.set_yticks(range(0, int(1.3e7), int(5e5)))
            sub.yaxis.grid(True)
            prev_dx = dx
        sub.set_xticks(xticks[0])
        sub.set_xticklabels(xticks[1], rotation='vertical')
        sub.legend(loc='upper right')
        f.subplots_adjust(bottom=0.2)
        canvas = FigureCanvasTkAgg(f, graph)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        save_button = tk.Button(graph, text='Save to file', command=lambda: self.save_graph(f))
        save_button.pack(side='top')

def main():
    work.load_dataframe(cg.db_plays_path, cg.db_plays_path1)


if __name__ == "__main__":
    main()
    root = tk.Tk()
    app = Main(root)
    app.pack()
    root.title("Города России")
    root.geometry("950x550+300+150")
    root.resizable(False, False)
    root.mainloop()
