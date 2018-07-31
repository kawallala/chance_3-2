import sys

if sys.platform == 'win32':

    import msvcrt

    def keypressed():
        key = msvcrt.getch()
        if key == b"\x1b": #ESC
            return "Escape"
        else:
            return "holi"
