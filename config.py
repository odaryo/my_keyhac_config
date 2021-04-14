import sys
import os
import datetime

import pyauto
from keyhac import *

def configure(keymap):

    # --------------------------------------------------------------------
    # Text editer setting for editting config.py file

    # Setting with program file path (Simple usage)
    # 設定のデフォルトアプリをサクラエディタに設定
    if 1:
        keymap.editor = "C:\Program Files (x86)\sakura\sakura.exe"

    # Setting with callable object (Advanced usage)
    if 0:
        def editor(path):
            shellExecute( None, "notepad.exe", '"%s"'% path, "" )
        keymap.editor = editor

    # --------------------------------------------------------------------
    # Customizing the display

    # Font
    keymap.setFont( "メイリオ", 12 )

    # Theme
    keymap.setTheme("black")

    # --------------------------------------------------------------------

    # Simple key replacement
    #keymap.replaceKey( "Caps", "RCtrl" )  # Capslock -> RCtrl

    # 除外アプリの設定
    def is_gexe_target(window):
#        if window.getProcessName() in ("vcxsrv.exe"):
#            return False
        return True

    # Global keymap which affects any windows
    if 1:
        keymap_global = keymap.defineWindowKeymap(check_func=is_gexe_target)

        # モディファイアキーごとに設定
        for modifier in ("", "S-", "C-", "C-S-"):
            # カーソルキーのショートカット
            keymap_global[ modifier + "LA-P" ] = modifier + "Up"
            keymap_global[ modifier + "LA-N" ] = modifier + "Down"
            keymap_global[ modifier + "LA-L" ] = modifier + "Right"
            keymap_global[ modifier + "LA-K" ] = modifier + "Left"
            keymap_global[ modifier + "LA-J" ] = modifier + "Home"
            keymap_global[ modifier + "LA-U" ] = modifier + "PageUp"
            keymap_global[ modifier + "LA-M" ] = modifier + "PageDown"
            keymap_global[ modifier + "LA-Semicolon" ] = modifier + "End"

        # AltキーをMacのように英数/日本語切り替えに使用する
        keymap_global["O-LAlt"] = lambda: keymap.getWindow().setImeStatus(0)    # 左Altキーを英数キーに設定
        keymap_global["O-RAlt"] = lambda: keymap.getWindow().setImeStatus(1)    # 右Altキーをかなキーに設定

        # その他の操作
        keymap_global[ "LC-D" ] = "Delete"
        keymap_global[ "LA-D" ] = "Delete"
        keymap_global[ "LC-I" ] = "S-End","C-X"  # 行末まで切り取り
        keymap_global[ "LA-I" ] = "S-End","C-X"  # 行末まで切り取り

        # ワークスペース切り替え
        keymap_global[ "RA-Right" ] = "LW-LC-Right"
        keymap_global[ "RA-Left" ] = "LW-LC-Left"
        keymap_global[ "LW-2" ] = "LW-LC-Right"
        keymap_global[ "LW-1" ] = "LW-LC-Left"

        # LW-LA Left/Right/Down/Up : 40pixel単位のウインドウ移動
        keymap_global[ "LW-LC-Left"  ] = keymap.MoveWindowCommand( -40, 0 )
        keymap_global[ "LW-LC-Right" ] = keymap.MoveWindowCommand( +40, 0 )
        keymap_global[ "LW-LC-Down"  ] = keymap.MoveWindowCommand( 0, +40 )
        keymap_global[ "LW-LC-Up"    ] = keymap.MoveWindowCommand( 0, -40 )

        # LW-LS- Left/Right/Down/Up : 画面端までウィンドウ移動
        keymap_global[ "LW-LS-Left"  ] = keymap.MoveWindowToMonitorEdgeCommand(0)
        keymap_global[ "LW-LS-Right" ] = keymap.MoveWindowToMonitorEdgeCommand(2)
        keymap_global[ "LW-LS-Down"  ] = keymap.MoveWindowToMonitorEdgeCommand(3)
        keymap_global[ "LW-LS-Up"    ] = keymap.MoveWindowToMonitorEdgeCommand(1)

    # Customizing clipboard history list
    if 1:
        # Enable clipboard monitoring hook (Default:Enabled)
        keymap.clipboard_history.enableHook(False)
