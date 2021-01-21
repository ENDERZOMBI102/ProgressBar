# -*- mode: python ; coding: utf-8 -*-

a = Analysis(
    ['src\\ProgressBar.py'],
    pathex=['C:\\Users\\Flavia\\PycharmProjects\\ProgressBar'],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=[
        'tkinter',
        'lib2to3'
    ],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=None,
    noarchive=False
)
pyz = PYZ(
    a.pure,
    a.zipped_data,
    cipher=block_cipher
)
exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='ProgressBar',
    debug=False,
    bootloader_ignore_signals=False,
    strip=True,
    upx=False,
    console=False
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=True,
    upx=False,
    upx_exclude=[],
    name='ProgressBar'
)
