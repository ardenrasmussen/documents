#!/usr/bin/python3

import sys
import math

def main():
    color_map = {
        'i': "iyellow",
        'o': "ired",
        'd': "igreen",
        'r': "iblue",
        'c': "ipurple"
    }
    preamble = "\\begin{tikzpicture}[scale=1, transform shape]\n  \\definecolor{ired}{RGB}{244,67,54}\n  \\definecolor{ipurple}{RGB}{156,39,176}\n  \\definecolor{iblue}{RGB}{33,150,243}\n  \\definecolor{igreen}{RGB}{76,175,80}\n  \\definecolor{iyellow}{RGB}{255,235,59}\n"
    postamble = "\\end{tikzpicture}"
    with open(sys.argv[1], 'w') as out:
        out.write(preamble)
        step = 1.0
        prev = []
        for i, layer in enumerate(sys.argv[2:]):
            if layer[0] != 'c':
                count = int(layer[1:])
            else:
                count = int(layer[2:])
                stride = int(layer[1:2])
            nodes = []
            center = step * ((count - 1) / 2.0)
            for j in range(count):
                nodes.append("{}{}{}".format(layer[0], i, j))
                color = color_map[layer[0]]
                out.write(
                    "  \\node[circle,fill={}] ({}{}{}) at ({},{}) {{}};\n".
                    format(color, layer[0], i, j, i, (j * step) - center))
                if layer[0] in "dor":
                    for k, prev_node in enumerate(prev):
                        out.write("  \\draw ({}) -- ({});\n".format(
                            prev_node, nodes[-1]))
                if layer[0] == 'r':
                    if j != 0:
                        out.write("  \\draw ({}) -- ({});\n".format(
                            nodes[-2], nodes[-1]))
                    out.write(
                        "  \\draw[] ({}.45) arc (-15:195:1.25mm);\n".format(
                            nodes[-1]))
            if layer[0] == 'c':
                if len(prev) >= len(nodes):
                    for j, node in enumerate(nodes):
                        for k, prev_node in enumerate(prev):
                            if j - math.ceil(stride/2) < k <= j + math.floor(stride/2):
                                out.write("  \\draw ({}) -- ({});\n".format(
                                    prev_node, node))
                else:
                    pass
            prev = nodes
        out.write(postamble)


if __name__ == "__main__":
    main()
