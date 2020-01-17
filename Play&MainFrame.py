
def checkPlay(frame, value):
    if(value == int(str(vars.DATE.get()))):
        result = tkMessageBox.askokcancel('coreect data', 'Correct answer')
        play(frame)
    else:
        result = tkMessageBox.askokcancel('incoreect data', 'inCorrect answer')
    vars.resetVariables()

def play(frame):
    import random
    frame.destroy()
    frame = tk.Frame(root)
    frame.pack(side=tk.TOP, pady=80)

    first = random.randint(1,20)
    second = random.randint(1,20)
    operator = random.choice(["-","+","*"])
    if(operator ==  "-" and  first <  second):
        temp= first
        first = second
        second = temp

    value =  0
    if operator == "+" :
        value = first + second
    elif operator == "-":
        value = first - second
    else:
        value = first * second

    label = tk.Label(frame, text=str(first) + " " + operator + " " + str(second) + " = ", font=('arial', 30), bd=18)
    label.grid(row=1)
    e = tk.Entry(frame, font=('arial', 30), textvariable=vars.DATE, width=10)
    e.grid(row=1, column=1)
    btn = tk.Button(frame, text="Answer", font=('arial', 30), width=10)
    btn.grid(row=2, columnspan=2, pady=20)
    btn.bind('<Button-1>', lambda event, value=value, frame=frame: checkPlay(frame, value))

def child_window():
    def messageWindow():
        win = tk.Toplevel(pady=80)
        win.geometry("%dx%d+%d+%d" % (width, height, x, y))
        def action():
            result = tkMessageBox.askokcancel('Help', 'The consultant will come in two minutes')

        path = 'images'
        COLUMNS = 10
        image_count = 0
        for infile in glob.glob(os.path.join(path, '*.jpeg')):
            image_count += 1
            r, c = divmod(image_count - 1, COLUMNS)
            im = Image.open(infile)
            resized = im.resize((200, 200), Image.ANTIALIAS)
            tkimage = ImageTk.PhotoImage(resized)
            myvar = tk.Button(win, image=tkimage, command=action)
            myvar.image = tkimage
            myvar.grid(row=r, column=c)
    messageWindow()

def main_frame():
    global user, main
    frame = tk.Frame(root)
    main = frame
    frame.pack(side=tk.TOP, pady=10)
    u = Requests.GetUser(user)
    if int(u['isAdmin']) == 1:
        register = tk.Button(frame, text="Add New Worker", font=('arial', 18), width=35)  # need command
        register.bind('<Button-1>', lambda event, frame=frame, flag=False: ToggleToRegister(frame, False))
        register.grid(row=1, columnspan=2, pady=20)

        child = tk.Button(frame, text="Add New Child", font=('arial', 18), width=35)
        child.bind('<Button-1>', lambda event, frame=frame: toggle_to_add_child(frame))
        child.grid(row=2, columnspan=2, pady=20)

        images = tk.Button(frame, text="Images", font=('arial', 18), width=35)
        images.bind('<Button-1>', lambda event, frame=frame, flag=False: toggle_to_images(frame))
        images.grid(row=3, columnspan=2, pady=20)

        recommend = tk.Button(frame, text="View Recommendations", font=('arial', 18), width=35)
        recommend.bind('<Button-1>', lambda event, frame=frame: view_rec(frame))
        recommend.grid(row=4, columnspan=2, pady=20)

        holi = tk.Button(frame, text="View Holidays Requests", font=('arial', 18), width=35)
        holi.bind('<Button-1>', lambda event, frame=frame: view_holidays(frame))
        holi.grid(row=5, columnspan=2, pady=20)


    else:
        rec = tk.Button(frame, text="Recommend", font=('arial', 18), width=35)
        rec.grid(row=1, columnspan=2, pady=20)
        rec.bind('<Button-1>', lambda event, frame=frame: toggle_to_rec(frame))

        child_comment = tk.Button(frame, text="Write comment for a child", font=('arial', 18), width=35)
        child_comment.grid(row=2, columnspan=2, pady=20)
        child_comment.bind('<Button-1>', lambda event, frame=frame: toggle_to_child_com(frame))

        child_data = tk.Button(frame, text="Child data", font=('arial', 18), width=35)
        child_data.grid(row=3, columnspan=2, pady=20)
        child_data.bind('<Button-1>', lambda event, frame=frame: toggle_to_child(frame))

        guide = tk.Button(frame, text="User Guide", font=('arial', 18), width=35)
        guide.grid(row=4, columnspan=2, pady=20)
        guide.bind('<Button-1>', lambda event, frame=frame: toggle_to_guide(frame))

        holiday = tk.Button(frame, text="Ask for holiday", font=('arial', 18), width=35)
        holiday.grid(row=5, columnspan=2, pady=20)
        holiday.bind('<Button-1>', lambda event, frame=frame: ask_holiday(frame))
        playBtn = tk.Button(frame, text="Play game", font=('arial', 18), width=35)
        playBtn.grid(row=6, columnspan=2, pady=20)
        playBtn.bind('<Button-1>', lambda event, frame=frame: play(frame))

        contact = tk.Button(frame, text="Contact developer", font=('arial', 18), width=35)
        contact.grid(row=7, columnspan=2, pady=20)
        contact.bind('<Button-1>', lambda event, frame=frame: toggle_to_contact(frame))

        forChild = tk.Button(frame, text="For child", font=('arial', 18), width=35)
        forChild.grid(row=8, columnspan=2, pady=20)
        forChild.bind('<Button-1>', lambda event, frame=frame: child_window())


    log = tk.Button(frame, text="Logout", font=('arial', 18), width=35)
    log.grid(row=9, columnspan=2, pady=20)
    log.bind('<Button-1>', lambda event, frame=frame: logout(frame))



def logout(frame):
    global user
    try:
        open('connected.txt', 'w').close()
    except FileNotFoundError:
        print('a')
    result = tkMessageBox.askquestion('System', 'Are you sure you want to logout?', icon="warning")
    if result == 'yes':
        user = 0
        ToggleToLogin(frame)

def remove_user():
    Requests.RemoveUser(user)
    root.destroy()
    exit()


menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Logout", command=logout)
filemenu.add_command(label="Remove Account", command=remove_user)
menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)
LoginForm()
root.mainloop()