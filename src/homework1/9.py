import glob
# glob supports Unix style pathname extensions
python_files = glob.glob('1.py')
for file_name in sorted(python_files):
    print('    ------' + file_name)

    with open(file_name) as f:
        for line in f:
            print(' qwer   ' + line.rstrip())

    print()
