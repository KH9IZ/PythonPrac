from pyfiglet import Figlet
import gettext

translation = gettext.translation("prog", "po", fallback=True)
_ = translation.gettext

def solve(a, b):
    if a == 0:
        return None
    return -b / a

def main():
    f = Figlet(font='graceful')
    def figprint(s):
        print(f.renderText(s))
    try:
        a = int(input())
        b = int(input())
    except ValueError:
        figprint(_("INVALID VALUES"))
        quit(1)
    if (root := solve(a, b)) is not None:
        figprint(_("Root: {root}").format(root=root))
    else:
        figprint(_("NO ROOTS"))

if __name__ == "__main__":
    main()
