import sys
import tty
import termios
import select

class GetInputKey(object):
    def __enter__(self):
        #編集前の設定状態を保存
        self.before_fileno = sys.stdin.fileno()
        self.before_terminalattribute = termios.tcgetattr(self.before_fileno)

        #設定変更
        new_terminalattribute = termios.tcgetattr(self.before_fileno)
        new_terminalattribute[3] &= ~termios.ICANON
        new_terminalattribute[3] &= termios.ECHO
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, new_terminalattribute)

        return self

    def __exit__(self, exc_type, exc_value, traceback):
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, self.before_terminalattribute)
    
    def is_key_down(self):
        return select.select([sys.stdin],[],[],0)==([sys.stdin],[],[])
    
    def get_key_unicode_codepoint(self):
        return ord(sys.stdin.read(1)) if self.is_key_down() else -1