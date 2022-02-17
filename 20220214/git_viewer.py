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
    object_path = join('.git', 'objects', object_id[:2], object_id[2:-1])
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
        print_out_commit(header, size, commit_details, commit_message)
    case _:
        print("Unknown operands count")
