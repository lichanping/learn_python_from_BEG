import PyInstaller.__main__

PyInstaller.__main__.run([
    'huya_live_barrage_v2.py',
    '--onefile',
    '--exclude-module=tkinter',
    r'-iFacebook_icon-icons.com_66805.ico',
    # '--windowed'
])
