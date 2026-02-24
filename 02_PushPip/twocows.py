import subprocess
import sys
 
mas1 = ['cowsay']
if '-f' in sys.argv:
    mas1 += ['-f', sys.argv[sys.argv.index('-f') + 1]]
if '-e' in sys.argv:
    mas1 += ['-e', sys.argv[sys.argv.index('-e') + 1]]
if '-n' in sys.argv:
    mas1 += ['-n']
mas1 += [sys.argv[-2]]
result = subprocess.run(mas1, capture_output=True, text=True)
m1 = result.stdout.split('\n')

mas2 = ['cowsay']
if '-F' in sys.argv:
    mas2 += ['-f', sys.argv[sys.argv.index('-F') + 1]]
if '-E' in sys.argv:
    mas2 += ['-e', sys.argv[sys.argv.index('-E') + 1]]
if '-N' in sys.argv:
    mas2 += ['-n']
mas2 += [sys.argv[-1]]
result = subprocess.run(mas2, capture_output=True, text=True)
m2 = result.stdout.split('\n')

if len(m1) < len(m2):
    m1 = [''] * (len(m2) - len(m1)) + m1
if len(m2) < len(m1):
    m2 = [''] * (len(m1) - len(m2)) + m2

for i in range(len(m1) - 1):
    print(m1[i].ljust(len(max(m1, key=len)), ' ') + m2[i])
