from setuptools import setup

APP = ['Locanhchinh123_app.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'packages': ['PIL', 'pytesseract', 'openpyxl'],
    'plist': {
        'CFBundleName': 'LocAnhChinhApp',
        'CFBundleDisplayName': 'Lọc ảnh Chính HV',
        'CFBundleIdentifier': 'com.chinhhv.locanh',
        'CFBundleVersion': '0.1',
        'CFBundleShortVersionString': '0.1.0',
    },
}

setup(
    app=APP,
    name='LocAnhChinhApp',
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
