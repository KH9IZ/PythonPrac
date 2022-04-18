import gettext

translation = gettext.translation("dia", "po", fallback=True)
_ = translation.gettext
ngettext = translation.ngettext

def dialog():
    while s := input(_("Input a string: ")):
        n = len(s.split())
        print(ngettext("Entered {s} word", "Entered {s} words", n).format(s=n))
