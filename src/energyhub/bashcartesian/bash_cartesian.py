import re
from typing import List

from src.energyhub.bashcartesian.graph_node import GraphNode


class BashCartesian:
    def parse(self, incoming: str) -> List[str]:
        tokens = re.split("({|}|,)", incoming)

        root = GraphNode("")
        parents = [root]

        result = []
        self.get_nodes(tokens, 0, parents, False)
        self.print(root, "", result)

        return result

    def get_nodes(self, tokens, start, parents, in_expansion):

        previous = parents
        all_children = []
        index = start
        local_parents = parents
        while index < len(tokens):
            new_children = []
            token = tokens[index]

            if token == "{":
                new_index, nodes = self.get_nodes(tokens, index + 1, previous, True)
                new_children = nodes
                index = new_index
                local_parents = new_children
            elif token == "}":
                all_children.extend(previous)
                return index, all_children
            elif token == ",":
                all_children.extend(previous)
                local_parents = parents
            else:
                node = GraphNode(token)
                new_children.append(node)

                for parent in local_parents:
                    for child in new_children:
                        parent.add_child(child)

                local_parents = new_children

            previous = new_children

            index += 1

    def print(self, node, suffix, results):
        current = suffix + node.get_content()
        if not node.has_children():
            results.append(current)
        else:
            for child in node.get_children():
                self.print(child, current, results)
