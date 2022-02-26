#!/home/knyaz/tmp/myenv/bin/python3
# EASY-INSTALL-ENTRY-SCRIPT: 'ipsedixit==1.1.1','console_scripts','ipsedixit'
__requires__ = 'ipsedixit==1.1.1'
import re
import sys
from ipsedixit import meta
from ipsedixit import Generator
import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('num',
        nargs = '?',
        default = 4,
        type = int,
        help = 'number of paragraphs to generate (default: %(default)s)',
    )
    parser.add_argument('text', 
        nargs = '?',
        default = Generator.__init__.__defaults__[0],
        type = str,
        help = 'initial text base (default: %(default)s)',
    )
    parser.add_argument('-v', '--version',
        action='version',
        version=meta.__version__,
    )
    parser.add_argument('--min',
        default = 2,
        type = int,
        help = 'min number of sentences per paragraph (default: %(default)s)',
    )
    parser.add_argument('--max',
        default = 4,
        type = int,
        help = 'max number of sentences per paragraph (default: %(default)s)',
    )
    return parser.parse_args()

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    args = parse_args()
    if args.text in ('caesar', 'tacitus'):
        generator = Generator(args.text)
    elif args.text is not None:
        with open(args.text, encoding='utf-8') as f:
            generator = Generator(f.read())
    else:
        generator = Generator()
    print('\n\n'.join(generator.paragraphs(args.num, args.min, args.max)))
