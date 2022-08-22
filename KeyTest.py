# ノンブロッキング入力
# https://qiita.com/asana_yui/items/eb9fcbbc4e8879f10fc5
# shift, ctrl, alt, caps lockは無理っぽい
# unicode-key-code enter:10, forward_delete:127, tab:9, space:32, esc:27
# https://fmhelp.filemaker.com/help/13/fmp/ja/html/func_ref3.33.50.html
# with使えるようにしたい
# https://qiita.com/nakasone/items/cce6670f0919aca5112f


from utils.keyinput import GetInputKey

"""
#ノンブロッキング入力の設定
old_fn = sys.stdin.fileno()
old_tt = termios.tcgetattr(old_fn)
tty.setcbreak(old_fn)

try:
    while True:
        if is_key_down():
            push_key = get_key_unicode()
            print(chr(push_key))
            #Escで終了
            if(push_key == 27):                                      
                break
finally:
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_tt)
"""

with GetInputKey() as gik:
    while True:
        if gik.is_key_down():
            push_key = gik.get_key_unicode_codepoint()
            print('{}, {}'.format(push_key, chr(push_key)))
            if push_key == 27:
                print(' Esc')
                break