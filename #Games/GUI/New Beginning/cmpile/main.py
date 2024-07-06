import PyInstaller.__main__

PyInstaller.__main__.run([
    'class_test.py',
    '--onefile',
    '--windowed',
    '-n Effects',
])
