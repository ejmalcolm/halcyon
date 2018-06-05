# -*- mode: python -*-

block_cipher = None


a = Analysis(['halcyon_client.py'],
             pathex=['C:\\Users\\Evan\\Downloads\\Programming\\Halcyon\\halcyon'],
             binaries=[],
             datas=[('gamestate.pickle', '.'), ('tags_file.pickle', '.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='halcyon_client',
          debug=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='halcyon_client')
