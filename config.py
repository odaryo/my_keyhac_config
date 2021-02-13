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
    # keymap.replaceKey( "(240)", "RCtrl" )                  # Capslock -> RCtrl

    # 除外アプリの設定
    def is_gexe_target(window):
        if window.getProcessName() in ("vcxsrv.exe"):
            return False
        return True

    # Global keymap which affects any windows
    if 1:
        keymap_global = keymap.defineWindowKeymap(check_func=is_gexe_target)

        # カーソルキーのショートカット
        keymap_global[ "LC-P" ] = "Up"                  # Move cursor up
        keymap_global[ "LC-N" ] = "Down"                # Move cursor down
        keymap_global[ "LC-L" ] = "Right"               # Move cursor right
        keymap_global[ "LC-K" ] = "Left"                # Move cursor left
        keymap_global[ "LC-J" ] = "Home"                # Move to beginning of line
        keymap_global[ "LC-U" ] = "PageUp"
        keymap_global[ "LC-M" ] = "PageDown"
        keymap_global[ "LC-Semicolon" ] = "End"

        # 選択肢たままカーソル移動
        keymap_global[ "LC-LS-P" ] = "S-Up"
        keymap_global[ "LC-LS-N" ] = "S-Down"
        keymap_global[ "LC-LS-L" ] = "S-Right"
        keymap_global[ "LC-LS-K" ] = "S-Left"
        keymap_global[ "LC-LS-J" ] = "S-Home"
        keymap_global[ "LC-LS-U" ] = "S-PageUp"
        keymap_global[ "LC-LS-M" ] = "S-PageDown"
        keymap_global[ "LC-LS-Semicolon" ] = "S-End"

        # その他の操作
        keymap_global[ "LC-D" ] = "Delete"
        keymap_global[ "LC-I" ] = "S-End","C-X"  # 行末まで切り取り

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
