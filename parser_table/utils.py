def split_productions(productions: list[str]):
    """
    Splits the productions of a grammar into individual elements.

    For each production, the first element (p[0]) is the left-hand side of the production,
    and the remaining elements (p[1:]) are the right-hand side of the production.

    Args:
        productions (list[str]): List of strings representing the productions of the grammar.

    Returns:
        tuple: A tuple containing three elements:
            - List of lists, where each sublist represents a split production.
            - List of terminals present in the grammar.
            - List of variables (non-terminals) present in the grammar.
    """
    aux_productions = []
    terminals, variables = set(), set()

    for p in productions:
        aux = [item for item in p.split() if item != "->"]
        for item in aux:
            if item.islower() or (len(item) >= 2 and item[0] == "\\"):
                terminals.add(item)
            elif item.isupper():
                variables.add(item)
        aux_productions.append(aux)
    return aux_productions, list(terminals), list(variables)

def calculate_first(productions: list[str]):
    pass

if __name__ == "__main__":
    test_productions = [
        [  # First Funcionou
            "E' -> E",
            "E -> E + n",
            "E -> n"
        ],
        [  # First NÃO Funcionou
            "E -> T E'",
            "E' -> v T E'",
            "E -> ε",
            "T -> F T'",
            "T' -> \\^ F T'",
            "T' -> ε",
            "F -> \\¬ F",
            "F -> id"
        ],
        [  # First Funcionou
            "S -> A B",
            "A -> a A",
            "A -> a",
            "B -> b B",
            "B -> b"
        ],
        [  # First Funcionou
            "S -> A",
            "S -> B C",
            "A -> a A S",
            "A -> D",
            "B -> b B",
            "B -> f A C",
            "B -> ɛ",
            "C -> c C",
            "C -> c",
            "D -> g D",
            "D -> C",
            "D -> ɛ"
        ],
        [  # First NÃO Funcionou
            "S -> X Y Z",
            "X -> a X b",
            "X -> ɛ",
            "Y -> c Y Z c X",
            "Y -> d",
            "Z -> e Z Y e",
            "Z -> f"
        ]
    ]

    for i, prod in enumerate(test_productions):
        productions, terminals, variables = split_productions(prod)
        first_sets = calculate_first(productions)
        print(f"------- Produções {i} -------")
        print(prod)
        print(f"FIRST: {first_sets}")
        
