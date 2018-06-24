# coding=utf-8
import os

def os_walk(path):
    export = []
    for root, dirs, files in os.walk(path):
        export.append('%s %s %s' % (root, dirs, files))
    return export

if __name__ == '__main__':
    print('\n'.join(os_walk('.')))
