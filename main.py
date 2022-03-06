from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk
from sys import platform
from tkinter import filedialog


class NookEncodeUI:
    def __init__(self, parent: ThemedTk):
        # Initialise data for application
        self.filepath = ''
        self.__RESOURCES_SUPPORTED_LIST__ = ["Image", "Audio", "Video"]
        self.__RESOURCES_SUPPORTED__ = StringVar(value=self.__RESOURCES_SUPPORTED_LIST__)
        self.val_key = StringVar(value='')
        self.val_status = StringVar(value='Ready to Work! Select a resource to get started.')

        parent.grid_columnconfigure(1, weight=1)
        parent.grid_rowconfigure(1, weight=1)

        # Create a frame to hold all components
        self.frame = ttk.Frame(parent, padding='5 5 10 10')
        self.frame.grid(column=1, row=1, sticky=(N, S, E, W))

        # Resize the frame to fill entire window.
        self.frame.grid_columnconfigure(1, weight=1)
        self.frame.grid_rowconfigure(1, weight=1)

        # create a label
        ttk.Label(self.frame, text='Select Resource').grid(column=1, row=1, sticky=W)

        # create a listbox with all the resources
        self.lbox_resources = Listbox(self.frame, listvariable=self.__RESOURCES_SUPPORTED__)
        self.lbox_resources.grid(column=1, row=2, rowspan=8, sticky=W)
        self.lbox_resources.bind("<<ListboxSelect>>", self.handle_lbox_resources_select)
        self.lbox_resources.bind('<Return>', self.handle_lbox_resources_select)

        # create select file encode decode buttons
        self.btn_selectfile = ttk.Button(self.frame, text='Select File', command=self.handle_btn_select_file)
        self.btn_selectfile.grid(column=2, row=2, sticky=W)

        self.btn_encode = ttk.Button(self.frame, text='Encode', command=self.none)
        self.btn_encode.grid(column=3, row=2, sticky=W)

        # create encode key label and text area
        ttk.Label(self.frame, text='Enter Encode Key').grid(column=2, row=3, sticky=W)
        self.entry_key = ttk.Entry(self.frame, textvariable=self.val_key)
        self.entry_key.grid(column=2, row=4, sticky=W)

        # create encode algorithm label and buttons
        ttk.Label(self.frame, text='Select Encode Algorithm').grid(column=2, row=5, sticky=W)
        self.btn_lsb = ttk.Button(self.frame, text='LSB',  command=self.none)
        self.btn_lsb.grid(column=2, row=6, sticky=W)

        ttk.Label(self.frame, text='Encoded Action').grid(column=2, row=7, sticky=W)
        self.btn_save_encoded_file = ttk.Button(self.frame, text="Save encoded file.", command=self.none)
        self.btn_save_encoded_file.grid(column=2, row=8, sticky=W)

        self.lbl_status = ttk.Label(self.frame, textvariable=self.val_status)
        self.lbl_status.grid(column=1, row=9, columnspan=4, sticky=W)

        # space all components with padding.
        for child in self.frame.winfo_children():
            child.grid_configure(padx=5, pady=5)

    def handle_lbox_resources_select(self, *args):
        current = self.lbox_resources.curselection()
        resource = self.__RESOURCES_SUPPORTED_LIST__[current[0]]

        if resource.lower() == "image":
            self.val_status.set(f"Selected Resource: {resource}, Now select file to upload.")
        else:
            self.val_status.set(f"Selection option: {resource} is currently work in progress!")

    def handle_btn_select_file(self):
        startdir = '/home' if platform == 'linux' else 'C:\\'
        filepath = filedialog.askopenfilename(initialdir=startdir, filetypes=[("Audio files", "*.{mp3,wav}"), ("JPEG Files", "*.{jpg,jpeg}"), ("PNG Files", "*.png"), ('All Files', "*.*")])

        if not str(filepath).endswith("png") or not str(filepath).endswith("jpg") or not str(filepath).endswith("jpeg"):
            self.val_status.set(f"Only JPEG and PNG files are supported yet.")

        self.filepath = filepath
        self.val_status.set(f"Selected file: {filepath}")

    def none(self, *args):
        pass


if __name__ == '__main__':
    theme = 'arc' if platform == "linux" else 'default'
    win = ThemedTk(theme=theme)
    win.title("Nook Encode GUI - Shaurya Bhatnagar and Jayant Malik")
    NookEncodeUI(parent=win)
    win.minsize(600, 400)
    win.maxsize(600, 600)
    win.resizable(False, False)
    win.mainloop()
