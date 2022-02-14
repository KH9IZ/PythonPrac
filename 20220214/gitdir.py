import zlib
import sys
from glob import iglob
from os.path import join

repo = sys.argv[1]
repopath = join(repo, "objects", "??", "*")
for objname in iglob(repopath):
    print(objname)
    with open(objname, "rb") as of:
        fo = zlib.decompress(of.read())
        header, _, body = fo.partition(b'\x00')
        kind, size = header.split()
        print(kind.decode(), int(size))
        if kind == b'commit':
            print("\t", body.decode().replace('\n', '\n\t'))
        elif kind == b"tree":
            while body:
                treehdr, _, tail = body.partition(b'\x00')
                gitid, body = tail[:20], tail[20:]
                print(f"\t{treehdr}, {gitid.hex()}")

