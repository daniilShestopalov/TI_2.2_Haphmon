import Visual
from Huffman_code import check_probabilities, huffman_coding_with_node_final, entropy, average_code_length, \
    extract_codes_from_node

if __name__ == '__main__':
    probabilities = {
        "Z1": 0.147,
        "Z2": 0.27,
        "Z3": 0.025,
        "Z4": 0.1,
        "Z5": 0.16,
        "Z6": 0.024,
        "Z7": 0.028,
        "Z8": 0.146,
        "Z9": 0.038,
        "Z10": 0.062
    }
    try:
        check_probabilities(probabilities)

        root = huffman_coding_with_node_final(probabilities)  # Используем эту функцию, а не get_huffman_codes_with_node

        sorted_freqs = sorted(probabilities.items(), key=lambda x: x[1], reverse=True)
        print("Sorted Frequencies:")
        for char, freq in sorted_freqs:
            print(f"{char}={freq}")

        print("H,L and R:")
        H = entropy(probabilities)
        L = average_code_length(probabilities, extract_codes_from_node(root))
        R = L - H
        print(f'H = {round(H, 3)}')
        print(f'L = {round(L, 3)}')
        print(f'R = {round(R, 3)}')

        print("Huffman Codes:")
        Visual.print_codes(root)

        visual = Visual.visualize_tree(root)
        visual.view()
    except ValueError as e:
        print(e)