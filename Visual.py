from graphviz import Digraph

def visualize_tree(root):
    dot = Digraph()
    visualize_node(dot, root)
    return dot

def visualize_node(dot, node, parent_name=None, edge_label=None):
    if node is None:
        return

    dot.node(node.name, label=f"{node.name}\n{node.prob}\n{node.code}")

    if parent_name:
        dot.edge(parent_name, node.name, label=edge_label)

    visualize_node(dot, node.left, node.name, "0")
    visualize_node(dot, node.right, node.name, "1")

def print_codes(node, prefix=""):
    if node is None:
        return

    if not node.left and not node.right:  # it's a leaf node
        print(f"{node.name} ({node.prob}) = {node.code}")

    print_codes(node.left, prefix + "0")
    print_codes(node.right, prefix + "1")