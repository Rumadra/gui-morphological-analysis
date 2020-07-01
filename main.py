import tkinter as tk

import MeCab

class GuiApp(tk.Frame):
    noun = []
    verb = []
    adjective = []
    pw_main = tk
    pw_top = tk
    pw_bottom = tk

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.pw_main = tk.PanedWindow(self.master, orient='vertical')
        self.pw_main.pack(expand=True, fill=tk.BOTH, side="top")

        self.pw_top = tk.PanedWindow(self.pw_main, bg="olivedrab", orient='vertical')
        self.pw_main.add(self.pw_top)
        self.pw_bottom = tk.PanedWindow(self.pw_main, bg="gray", orient='vertical')
        self.pw_main.add(self.pw_bottom)

        self.quit = tk.Button(self.pw_top, fg="olivedrab", text="終了",
                              command=self.master.destroy)
        self.quit.pack(side="right")

        self.submit_btn = tk.Button(self.pw_top, bg="olivedrab", text="決定", command=self.place_words)
        self.submit_btn.pack(side="right")

        self.text_box = tk.Entry(self.pw_top, width=20, fg="olivedrab")
        self.text_box.insert(tk.END, "何か入力してください。")
        self.text_box.pack(side="top")

    def place_words(self):
        self.analize_phrase()
        if self.pw_bottom.winfo_exists():
            

        for n in range(len(self.noun)):
            label_noun = tk.Label(self.pw_bottom, text=self.noun[n], width=20, bg="blue")
            label_noun.grid(row=n, column=0, padx=2, pady=2)

        for v in range(len(self.verb)):
            label_verb = tk.Label(self.pw_bottom, text=self.verb[v], width=20, bg="red")
            label_verb.grid(row=v, column=1, padx=2, pady=2)

        for a in range(len(self.adjective)):
            label_adjective = tk.Label(self.pw_bottom, text=self.adjective[a], width=20, bg="green")
            label_adjective.grid(row=a, column=2, padx=2, pady=2)

    def analize_phrase(self):
        txt = self.text_box.get()
        print("文字が入力されしました。:" + txt)
        mecab = MeCab.Tagger("-Ochasen")
        node = mecab.parseToNode(txt)
        malist = mecab.parse(txt)

        print(malist)

        while node:
            if node.feature.split(",")[0] == u"名詞":
                self.noun.append(node.surface)
            elif node.feature.split(",")[0] == u"動詞":
                self.verb.append(node.feature.split(",")[6])
            elif node.feature.split(",")[0] == u"形容詞":
                self.adjective.append(node.feature.split(",")[6])
            node = node.next

        print('名詞　:')
        for n in self.noun: print(n)
        print('動詞　:')
        for v in self.verb: print(v)
        print('形容詞:')
        for a in self.adjective: print(a)

root = tk.Tk()
root.geometry('600x400')
root.title('gui-morphological-analysis')

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

app = GuiApp(master=root)
app.mainloop()
