class GraphNode:
    def __init__(self, content: str):
        self.children = []
        self.content = content

    def get_children(self) -> list:
        return self.children

    def add_child(self, node):
        self.children.append(node)

    def has_children(self) -> bool:
        return len(self.children) > 0

    def get_content(self) -> str:
        return self.content

    def __str__(self):
        return "Node: " + self.content