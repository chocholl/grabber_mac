import os
import sys

needed = []

with open('modules.txt', 'r') as f:
        for l in f.readlines():
                if(l != ''):
                        needed.append(l.replace('\n', ''))

installed = sys.modules.keys()

for n in needed:
        found = False
        for i in installed:
                if(n == i):
                        found = True
                        
        if(found == False):
                print(n + ' not found... Installing...')
                os.system("pip install " + n)
        if(found == True):
                print(n + ' found.')

print('')
print('Done.')
