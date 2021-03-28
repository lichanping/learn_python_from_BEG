import PyInstaller.__main__

PyInstaller.__main__.run([
    'main.py',
    '--onefile',
    r'-iFacebook_icon-icons.com_66805.ico',
    # '--windowed'
])