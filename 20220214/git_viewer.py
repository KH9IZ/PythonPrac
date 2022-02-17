#!/usr/bin/env python3.10
import sys
from os.path import join
import os
import zlib
from collections import defaultdict


def get_head_commit_id(branch_name):
    branch_head_path = join('.git', 'refs', 'heads', branch_name)
    with open(branch_head_path, 'r') as t:
        return t.read()


def get_object(object_id):
    object_id = object_id.strip()
    object_path = join('.git', 'objects', object_id[:2], object_id[2:])
    with open(object_path, 'rb') as f:
        header, _, body = zlib.decompress(f.read()).partition(b'\x00')
    obj_type, size = header.split()
    obj_type = obj_type.decode()
    return obj_type, int(size), body


def parse_commit(body):
    body = body.decode()
    meta_info, _, commit_message = body.partition('\n\n')
    details = defaultdict(list)
    for row in meta_info.split('\n'):
        field, _, value = row.partition(' ')
        if field == 'parent':
            details[field].append(value)
        else:
            details[field] = value
    return details, commit_message


def print_out_commit(header, size, commit_details, commit_message):
    print(f"Object: {header} (size={size})")
    for field, value in commit_details.items():
        print(f"  - {field:<10}: {value}")
    print("\n  ", commit_message)


def parse_tree(body):
    details = {}
    while body:
        hdr, _, tail = body.partition(b'\00')
        attrs, _, fname = hdr.partition(b' ')
        object_id, body = tail[:20], tail[20:]
        details[fname.decode()] = (attrs, object_id)
    return details        

spcs = 0
def print_out_tree(header, size, details):
    global spcs
    # print(f"Object: {header} (size={size})")
    for fname, (attrs, obj_id) in details.items():
        sub_obj_type, sub_size, sub_body = get_object(obj_id.hex())
        line = '├' if sub_obj_type != 'tree' else '├┬'
        print(f"{'│'*spcs}{line}{fname:<13}[{sub_obj_type}]({attrs.decode():^6}): {obj_id.hex()}")
        if sub_obj_type == 'tree':
            spcs += 1
            print_out_tree(sub_obj_type, sub_size, parse_tree(sub_body))
            spcs -= 1
            print(f"{'│'*spcs}├┘")


match len(sys.argv):
    case 1:
        repopath = join('.git', "refs", "heads")
        print("Branches of current repository:")
        for branchname in os.listdir(repopath):
            print('  - ', branchname)
    case 2:
        branch_name = sys.argv[1]
        commit_id = get_head_commit_id(branch_name)
        header, size, body = get_object(commit_id)
        commit_details, commit_message = parse_commit(body)
        #print_out_commit(header, size, commit_details, commit_message)
        tree_id = commit_details['tree']
        header, size, body = get_object(tree_id)
        tree_details = parse_tree(body)
        print_out_tree(header, size, tree_details)
    case _:
        print("Unknown operands count")
