# -*- mode: python ; coding: utf-8 -*-

a = Analysis(
    ['example.py'],
    pathex=[],
    binaries=[],
    datas=[('static/*', '.'), ('static/assets/*', 'assets')],  # Adjusted paths
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='example',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
)