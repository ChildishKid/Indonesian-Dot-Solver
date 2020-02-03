from os.path import isfile

from agents.config import agent_dict
from agents.dfs import dfs

DEFAULT_PATH = '../resources/'
DEFAULT_IN_FILE = DEFAULT_PATH + 'test'
FUNCTION = [dfs]

if not isfile(DEFAULT_IN_FILE):
    raise FileNotFoundError(f'File {DEFAULT_PATH}{DEFAULT_IN_FILE} not found')

target = open(DEFAULT_IN_FILE)

commands = []
lines = target.readlines()
for line in lines:
    if line == '\n':
        continue

    l_arr = line.split(' ')
    l_arr[-1] = l_arr[-1][:-1]
    c = agent_dict()
    key = list(c.keys())

    if len(l_arr) != len(key):
        raise SyntaxError(f'Error:: Line {line} does not have appropriate attributes.')

    c.update({key[i]: (int(l_arr[i]) if i < len(l_arr) - 1 else l_arr[i]) for i in range(len(l_arr))})
    commands.append(c)

del lines

for i in range(0, len(commands)):
    for j in range(len(FUNCTION)):
        func = FUNCTION[j]
        search, sol = func(**commands[i])
        search = ['0 0 ' + str(s) + '\n' for s in search]
        sol = [str(s) + '\n' for s in sol]
        reg = DEFAULT_PATH + str(i+1) + '_' + func.__name__ + '_'
        f = open(reg+'search', 'w')
        f.writelines(search)
        f.close()
        f = open(reg + 'solution', 'w')
        f.writelines(sol)
        f.close()
