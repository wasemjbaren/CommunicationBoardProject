
def toggle_to_rec(frame, event=None):
    def recommed():
        global user
        text = vars.ENTRY.get()
        vars.resetVariables()
        Requests.SendRecommend(user, text)

    frame.destroy()
    frame = tk.Frame(root)
    frame.pack(side=tk.TOP, pady=80)
    label = tk.Label(frame, text="Recommendation: ", font=('arial', 18), bd=18)
    label.grid(row=1)
    entry = tk.Entry(frame, font=('arial', 20), textvariable=vars.ENTRY, width=60)
    entry.grid(row=2)
    but = tk.Button(frame, text="Send Recommendation", font=('arial', 18), width=35)  # need command
    but.bind('<Button-1>', lambda event, frame=frame: recommed())
    but.grid(row=3, columnspan=2, pady=20)
    back_button(frame)



def toggle_to_child_com(frame, event=None):
    def write_comment():
        text = vars.ENTRY.get()
        flag = Requests.AddCommentForChild(user, vars.FIRSTNAME.get(), text)
        vars.resetVariables()
        if not flag:
            result = tkMessageBox.askokcancel('Incoreect data', 'invalid child name')

    frame.destroy()
    frame = tk.Frame(root)
    frame.pack(side=tk.TOP, pady=80)
    label = tk.Label(frame, text="Write comment for child: ", font=('arial', 18), bd=18)
    label.grid(row=1)
    e_label = tk.Label(frame, text="child name: ", font=('arial', 18), bd=18)
    e_label.grid(row=2)
    entry = tk.Entry(frame, font=('arial', 20), textvariable=vars.FIRSTNAME, width=15)
    entry.grid(row=3)
    e_labe = tk.Label(frame, text="comment: ", font=('arial', 18), bd=18)
    e_labe.grid(row=4)
    entry = tk.Entry(frame, font=('arial', 20), textvariable=vars.ENTRY, width=60)
    entry.grid(row=5)
    but = tk.Button(frame, text="Send comment", font=('arial', 18), width=35)  # need command
    but.bind('<Button-1>', lambda event, frame=frame: write_comment())
    but.grid(row=6, columnspan=2, pady=20)
    back_button(frame)

def back_button(frame, flag=False):
    btn = tk.Button(frame, text="Back to main page", font=('arial', 18), width=35)
    btn.bind('<Button-1>', lambda event, frame=frame: return_to_main_page(frame))
    if flag:
        btn.pack(side=tk.BOTTOM)
    else:
        btn.grid(row=10)

def return_to_main_page(frame):
    frame.destroy()
    main_frame()


def toggle_to_guide(frame, event=None):
    frame.destroy()
    frame = tk.Frame(root)
    frame.pack(side=tk.TOP, pady=80)
    label_guide = tk.Label(frame, text="This is user guide, write here all the guides for the user", font=('arial', 18), bd=18)
    label_guide.grid(row=1)
    back_button(frame)

def toggle_to_contact(frame,event=None):
    frame.destroy()
    frame = tk.Frame(root)
    frame.pack(side=tk.TOP, pady=80)
    label_guide = tk.Label(frame, text="Developer : wasem , email : wasemjbaren@gmail.com", font=('arial', 18),bd=18)
    label_guide1 = tk.Label(frame, text="Developer : rani , email : ranihajyahia1@gmail.com", font=('arial', 18),bd=18)
    label_guide2 = tk.Label(frame, text="Developer : adan , email : adan_rwashdi@gmail.com", font=('arial', 18),bd=18)
    label_guide3 = tk.Label(frame, text="Developer : tarek , email : tareksalem1@gmail.com", font=('arial', 18),bd=18)

    label_guide.grid(row=1)
    label_guide1.grid(row=2)
    label_guide2.grid(row=3)
    label_guide3.grid(row=4)
    back_button(frame)

def ask_holiday(frame, event=None):
    frame.destroy()
    frame = tk.Frame(root)
    frame.pack(side=tk.TOP, pady=80)
    def ask():
        if not Requests.AskForHoliday(user, vars.DATE.get()):
            result = tkMessageBox.askokcancel('Incoreect data', 'This date already packed')
        else:
            l = tk.Label(frame, text="Holiday saved", font=('arial', 18), bd=18)
            l.grid(row=3)

    frame.pack(side=tk.TOP, pady=80)
    label = tk.Label(frame, text="Type date for holiday: ", font=('arial', 18),bd=18)
    label.grid(row=1)
    e = tk.Entry(frame, font=('arial', 20), textvariable=vars.DATE, width=15)
    e.grid(row=1, column=1)
    btn = tk.Button(frame, text="Ask", font=('arial', 18), width=35)
    btn.bind('<Button-1>', lambda event: ask())
    btn.grid(row=2, columnspan=2, pady=20)
    back_button(frame)


def view_rec(frame, event=None):
    frame.destroy()
    frame = tk.Frame(root)
    frame.pack(side=tk.TOP, pady=40)
    tree = ttk.Treeview(frame)
    tree["columns"] = ("one", "two")
    tree.column("one", stretch=tk.NO)
    tree.column("two", width=400, stretch=tk.YES)
    tree.heading("one", text='Name', anchor=tk.W)
    tree.heading("two", text='Recommendation', anchor=tk.W)
    tree.pack(side=tk.TOP, fill=tk.X)
    lst = Requests.GetRecommendations()
    for line in lst:
        r = Requests.GetUser(line['UserID'])
        name = r['FirstName'] + ' ' + r['LastName']
        comment = line['Comment']
        tree.insert("",tk.END, values=(name, comment))

    back_button(frame, True)

def view_holidays(frame, event=None):
    frame.destroy()
    frame = tk.Frame(root)
    frame.pack(side=tk.TOP, pady=40)
    tree = ttk.Treeview(frame)
    tree["columns"] = ("one", "two")
    tree.column("one", stretch=tk.NO)
    tree.column("two", width=400, stretch=tk.YES)
    tree.heading("one", text='Name', anchor=tk.W)
    tree.heading("two", text='Date', anchor=tk.W)
    tree.pack(side=tk.TOP, fill=tk.X)
    lst = Requests.GetHolidays()
    for line in lst:
        r = Requests.GetUser(line['UserID'])
        name = r['FirstName'] + ' ' + r['LastName']
        comment = line['Date']
        tree.insert("", tk.END, values=(name, comment))

    back_button(frame, True)
def child_data(frame, r):
    frame.destroy()
    frame = tk.Frame(root)
    frame.pack(side=tk.TOP, pady=40)
    tk.Label(frame, text="Child name: " + r[0]['FullName'], font=('arial', 18), bd=18).grid(row=1)
    tk.Label(frame, text="City: " + r[0]['City'], font=('arial', 18), bd=18).grid(row=2)
    tk.Label(frame, text="Birthday: " + r[0]['Birthday'], font=('arial', 18), bd=18).grid(row=3)
    tk.Label(frame, text="Sitting: " + str(r[0]['Sitting']), font=('arial', 18), bd=18).grid(row=4)

    j=6
    tk.Label(frame, text="Comments:", font=('arial', 18), bd=18).grid(row=5)
    for i in range(min(len(r[1]), 4)):
        comment = r[1][i]['Comment']
        print(r[1][i]['UserID'])
        user = Requests.GetUser(r[1][i]['UserID'])
        name = user['FirstName'] + ' ' + user['LastName']
        tk.Label(frame, text=name + ': ' + comment, font=('arial', 18), bd=18).grid(row=j)
        j += 1

    back_button(frame, True)

def toggle_to_child(frame):
    frame.destroy()
    frame = tk.Frame(root)
    frame.pack(side=tk.TOP, pady=40)

    def get():
        r = Requests.GetChild(vars.FIRSTNAME.get())
        if r is None:
            result = tkMessageBox.askokcancel('Incoreect data', 'Please correct data')
            vars.resetVariables()
        else:
            child_data(frame, r)
            back_button(frame, True)

    label = tk.Label(frame, text="Enter child name: ", font=('arial', 18), bd=18)
    label.grid(row=1)
    e = tk.Entry(frame, font=('arial', 20), textvariable=vars.FIRSTNAME, width=15)
    e.grid(row=1, column=1)
    btn = tk.Button(frame, text="Ask", font=('arial', 18), width=35)
    btn.bind('<Button-1>', lambda event: get())
    btn.grid(row=2, columnspan=2, pady=20)
