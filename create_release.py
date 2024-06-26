import platform

import PyInstaller.__main__

# PyInstaller.__main__.run([
#     'lists_compiler.py',
#     '--onefile',
#     '--add-data', "./cards.collectible.json:.",
#     '-n lists_compiler.exe'
# ])
#
# PyInstaller.__main__.run([
#     'smn_helper.py',
#     '--onefile',
#     '--add-data', "./cards.collectible.json:.",
#     '--add-data', "./rich.wav:.",
#     '-n smn_helper.exe'
# ])
if platform.system() == 'Windows':
    filename = '-n lst_helper.exe'
else:
    filename = '-n lst_helper.mac'
PyInstaller.__main__.run(
    [
        'lst_helper.py',
        '--onefile',
        filename
    ]
)

if platform.system() == 'Windows':
    filename = '-n lst_power_parser.exe'
else:
    filename = '-n lst_power_parser'
PyInstaller.__main__.run([
    'lst_power_parser.py',
    '--onefile',
    filename
])
