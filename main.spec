# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[('munro.ttf', '.'), ('wingding.ttf', '.'), ('Snoop Dogg.png', '.'), ('Snoop Frog.png', '.'), ('Python.png', '.'), ('icon.png', '.'), ('victory.mp3', '.'), ('lowhp.mp3', '.'), ('backgroundMusic.mp3', '.'), ('damage.wav', '.')],
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
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['icon.icns'],
)
app = BUNDLE(
    exe,
    name='main.app',
    icon='icon.icns',
    bundle_identifier=None,
)
