### Standalone Python EXE Executable

_Pyinstaller_

```
pip install pyinstaller
```

```
pip install freeze
```


### Ejecucion 1

```
pyinstaller nombreArchivo.py  -w
```

### Archivo | calc.spec

```python
from kivy_deps import sdl2, glew
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(['calc.py'],
             pathex=['C:\\Users\\brian\\Documents\\Python-Kivy\\019 Standalone Python EXE Executable'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

a.datas += [('019 Standalone Python EXE Executable\cal.kv', 'C:\\Users\\brian\\Documents\\Python-Kivy\\019 Standalone Python EXE Executable\\cal.kv', 'DATA')]

exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='calc',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False )
coll = COLLECT(exe, Tree('C:\\Users\\brian\\Documents\\Python-Kivy\\019 Standalone Python EXE Executable\\'),
               a.binaries,
               a.zipfiles,
               a.datas,
               *[Tree(p) for p in
               (sdl2.dep_bins +
               glew.dep_bins)],
               strip=False,
               upx=True,
               upx_exclude=[],
               name='calc')

```

### Ejecucion 2

```
pyinstaller nombreArchivo.spec  -y
```

