import os


def replace(line):
    if line.startswith('5') or line.startswith('7'):
        line = '2' + line[1:]
    return line


def rework_classes(labelpath, default=True):
    if default:

        if type(labelpath) == list:
            for path in labelpath:
                if os.path.exists(path):
                    data = ''
                    with open(path, "r") as fr:
                        lines = fr.readlines()
                        for line in lines:
                            line = replace(line)
                            data = data + line
                    with open(path, 'w') as fw:
                        fw.write(data)
            return

        if os.path.isdir(labelpath):
            labels = os.listdir(labelpath)
            labels.remove('classes.txt') if 'classes.txt' in labels else None
            for name in labels:
                path = os.path.join(labelpath, name)
                if os.path.exists(path):
                    data = ''
                    with open(path, "r") as fr:
                        lines = fr.readlines()
                        for line in lines:
                            line = replace(line)
                            data = data + line
                    with open(path, 'w') as fw:
                        fw.write(data)

        elif os.path.isfile(labelpath):
            data = ''
            with open(labelpath, "r") as fr:
                lines = fr.readlines()
                for line in lines:
                    line = replace(line)
                    data = data + line
            with open(labelpath, 'w') as fw:
                fw.write(data)


