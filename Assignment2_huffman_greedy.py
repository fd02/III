class Node:
    def __init__(self, symbol, freq, left=None, right=None):
        self.symbol = symbol
        self.freq = freq
        self.left = left
        self.right = right

def build_huffman_tree(symbols, freqs):
    nodes = [Node(symbols[i], freqs[i]) for i in range(len(symbols))]
    
    while len(nodes) > 1:
        # Sort nodes based on frequency
        nodes.sort(key=lambda node: node.freq)
        # Pop two smallest nodes
        left, right = nodes.pop(0), nodes.pop(0)
        # Create a new node with left and right children
        new_node = Node(left.symbol + right.symbol, left.freq + right.freq, left, right)
        nodes.append(new_node)
    
    return nodes[0]

def generate_codes(node, code=''):
    if node.left is None and node.right is None:
        print(f"{node.symbol}: {code}")
        return
    generate_codes(node.left, code + '0')
    generate_codes(node.right, code + '1')

# Taking input from user
n = int(input("Enter number of characters: "))
symbols = [input(f"Enter character {i + 1}: ") for i in range(n)]
freqs = [int(input(f"Enter frequency for {symbols[i]}: ")) for i in range(n)]

# Build Huffman Tree and generate codes
root = build_huffman_tree(symbols, freqs)
print("Huffman Codes:")
generate_codes(root)

# Time complexity : O(n log n)
# Space complexity : O(n)