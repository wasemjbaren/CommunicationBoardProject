

def toggle_to_forgot(frame):
    frame.destroy()
    ForgotForm()


def ToggleToRegister(frame, flag):
    frame.destroy()
    RegisterForm(flag)


def Register(frame, flag):
    a = 0
    if(vars.ISADMIN.get() == 'yes'):
        a = 1
    if(Requests.AddUser(vars.FIRSTNAME.get(), vars.LASTNAME.get(), vars.PHONE.get(), vars.USERNAME.get(), vars.PASSWORD.get(), a)):
        vars.resetVariables()
        frame.destroy()
        if flag:
            LoginForm()
        else:
            main_frame()

    else:
        result = tkMessageBox.askokcancel('Incoreect data', 'Please correct data')


def toggle_to_main_page(LoginFrame, flag, event=None):
    global user
    u = Requests.CheckLogin(vars.USERNAME.get(), vars.PASSWORD.get())
    if u == -1 and flag:
        result = tkMessageBox.askokcancel('Incoreect data', 'user name or password isnt correct')
    else:
        if flag:
            user = u
            vars.resetVariables()
            with open('connected.txt', 'w') as file:
                file.write(str(user))
        LoginFrame.destroy()
        main_frame()

def add_child_to_db(frame, event=None):
    result = Requests.AddChild(vars.NAME.get(), vars.CITY.get(), vars.BIRTHDAY.get(), vars.SITS.get())
    if result:
        vars.resetVariables()
        frame.destroy()
        main_frame()
    else:
        result = tkMessageBox.askokcancel('Incoreect data', 'Please correct data')


def add_child():
    frame = tk.Frame(root)
    frame.pack(side=tk.TOP, pady=80)
    l_name = tk.Label(frame, text="Full Name:", font=('arial', 18), bd=18)
    l_name.grid(row=1)
    name = tk.Entry(frame, font=('arial', 20), textvariable=vars.NAME, width=15)
    name.grid(row=1, column=1)
    l_city = tk.Label(frame, text="City:", font=('arial', 18), bd=18)
    l_city.grid(row=2)
    city = tk.Entry(frame, font=('arial', 20), textvariable=vars.CITY, width=15)
    city.grid(row=2, column=1)
    l_birth = tk.Label(frame, text="Birth day:", font=('arial', 18), bd=18)
    l_birth.grid(row=3)
    birth = tk.Entry(frame, font=('arial', 20), textvariable=vars.BIRTHDAY, width=15)
    birth.grid(row=3, column=1)
    l_sits = tk.Label(frame, text="Number of sittings:", font=('arial', 18), bd=18)
    l_sits.grid(row=4)
    sits = tk.Entry(frame, font=('arial', 20), textvariable=vars.SITS, width=15)
    sits.grid(row=4, column=1)
    add = tk.Button(frame, text="Add Child", font=('arial', 18), width=35)  # need command
    add.bind('<Button-1>', lambda event, frame=frame: add_child_to_db(frame))
    add.grid(row=7, columnspan=2, pady=20)
    back_button(frame)


def toggle_to_add_child(frame, event=None):
    frame.destroy()
    add_child()

def a():
    result = tkMessageBox.askokcancel('Incoreect data', 'Please correct data')


def edit_image(frame):
    frame.destroy()
    frame = tk.Frame(root)
    frame.pack(side=tk.TOP, pady=80)
    file = ""
    def select():
        nonlocal file
        filename = filedialog.askopenfilename(initialdir="/", title="Select A File", defaultextension=
        (("jpeg files", "*.jpg"), ("all files", "*.*")))
    def update():
        if Requests.UpdateImage(file, vars.ENTRY.get()):
            result = tkMessageBox.askokcancel('Add', 'Image edited successfully')
        else:
            result = tkMessageBox.askokcancel('Add', 'Error in edit image')
    frame = tk.Frame(root)
    frame.pack(side=tk.TOP, pady=80)

    remove = tk.Button(frame, text="Select Image", font=('arial', 18), width=35)
    remove.bind('<Button-1>', lambda event, flag=False: select())
    remove.grid(row=1, columnspan=2, pady=20)
    l_name = tk.Label(frame, text="Description: ", font=('arial', 18), bd=18)
    l_name.grid(row=2)
    desc = tk.Entry(frame, font=('arial', 20), textvariable=vars.ENTRY, width=15)
    desc.grid(row=2, column=1)

    u = tk.Button(frame, text="Update", font=('arial', 18), width=35)
    u.bind('<Button-1>', lambda event, flag=False: update())
    u.grid(row=3, columnspan=2, pady=20)
    back_button(frame)




def load_images():
    frame = tk.Frame(root)
    frame.pack(side=tk.TOP, pady=80)

    def new_image():
        filename = filedialog.askopenfilename(initialdir="/", title="Select A File", defaultextension=
        (("jpeg files", "*.jpg"), ("all files", "*.*")))
        try:
            os.mkdir('images')
        except FileExistsError:
            print(filename)
        finally:
            try:
                shutil.copy(filename, 'images')
            except shutil.SameFileError:
                print('a')
            s = filename.split('/')
            s = s[len(s) - 1]
            print(s)
            if Requests.AddImage('images/' + s):
                result = tkMessageBox.askokcancel('Add', 'Image added successfully')
            else:
                result = tkMessageBox.askokcancel('Add', 'Error in Adding image')


        print('s')

    def remove_image():
        filename = filedialog.askopenfilename(initialdir="/", title="Select A File", defaultextension=
        (("jpeg files", "*.jpg"), ("all files", "*.*")))
        if Requests.DeleteImage(filename):
            os.remove(filename)
            result = tkMessageBox.askokcancel('Remove', 'Image removed successfully')
        else:
            result = tkMessageBox.askokcancel('Remove', 'Error in removing image')


    add_image = tk.Button(frame, text="Add New Image", font=('arial', 18), width=35)
    add_image.bind('<Button-1>', lambda event: new_image())
    add_image.grid(row=1, columnspan=2, pady=20)

    edit = tk.Button(frame, text="Edit Image", font=('arial', 18), width=35)
    edit.bind('<Button-1>', lambda event, flag=False, frame=frame: edit_image(frame))
    edit.grid(row=2, columnspan=2, pady=20)

    remove = tk.Button(frame, text="Remove image", font=('arial', 18), width=35)
    remove.bind('<Button-1>', lambda event, flag=False: remove_image())
    remove.grid(row=3, columnspan=2, pady=20)

    back_button(frame)


def toggle_to_images(frame, event=None):
    frame.destroy()
    load_images()