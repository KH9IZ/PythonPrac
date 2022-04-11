import gettext

translation = gettext.translation("dia", "po", fallback=True)
_ = translation.gettext
ngettext = translation.ngettext

def dialog():
    while s := input(_("Input a string: ")):
        n = len(s.split())
        print(ngettext("{s} word entered", "{s} words entered", n).format(s=n))
