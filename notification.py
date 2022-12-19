from win10toast import ToastNotifier
toaster = ToastNotifier()

toaster.show_toast("Example two",
"This notification is in it's own thread!",
icon_path=None,

threaded=True)

