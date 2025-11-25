import os
import io

from jinja2 import Environment, FileSystemLoader, select_autoescape
env = Environment(
    loader=FileSystemLoader("templates"),
    autoescape=select_autoescape()
)
template = env.get_template("tree.html")

default_path = "files"


def make_tree(path):
    tree = dict(dict(basename=os.path.basename(path),name=path), children=[])
    try: lst = os.listdir(path)
    except OSError:
        pass #ignore errors
    else:
        for name in lst:
            fn = "/".join([path, name])
            if os.path.isdir(fn):
                tree['children'].append(dict(make_tree(fn),type="directory"))
            else:
                tree['children'].append(dict(dict(basename=name,name=fn), type="file"))
    return tree


with open("files.html", "w") as i:
    h = template.render(tree=make_tree(default_path), root=default_path)
    i.write(h)

