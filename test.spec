# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['/home/bobi/Desktop/proxy_magic_bdx/magic_proxy-main/magic_proxy-main/choice.py', 'choice.spec'],
             pathex=[],
             binaries=[],
             datas=[('/home/bobi/Desktop/proxy_magic_bdx/magic_proxy-main/magic_proxy-main/formatted', 'formatted'), ('/home/bobi/Desktop/proxy_magic_bdx/magic_proxy-main/magic_proxy-main/magic_proxy.py', '.'), ('/home/bobi/Desktop/proxy_magic_bdx/magic_proxy-main/magic_proxy-main/magic_proxy_set.py', '.'), ('/home/bobi/Desktop/proxy_magic_bdx/magic_proxy-main/magic_proxy-main/magic_proxy_for_mpc.py', '.'), ('/home/bobi/Desktop/proxy_magic_bdx/magic_proxy-main/magic_proxy-main/A4_cards.pdf', '.'), ('/home/bobi/Desktop/proxy_magic_bdx/magic_proxy-main/magic_proxy-main/card.txt', '.'), ('/home/bobi/Desktop/proxy_magic_bdx/magic_proxy-main/magic_proxy-main/config.py', '.'), ('/home/bobi/Desktop/proxy_magic_bdx/magic_proxy-main/magic_proxy-main/setting.py', '.'), ('/home/bobi/Desktop/proxy_magic_bdx/magic_proxy-main/magic_proxy-main/keygen.mp3', '.'), ('/home/bobi/Desktop/proxy_magic_bdx/magic_proxy-main/magic_proxy-main/price.py', '.')],
             hiddenimports=["scrython", "skimage", "requests", "imageio", "fpdf"],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,  
          [],
          name=os.path.join('dist', 'magic_proxy.exe'),
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True, 
          icon='Magic.ico',
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
