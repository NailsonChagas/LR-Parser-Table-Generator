def split_productions(productions: list[str]):
    """
    Splits the productions of a grammar into individual elements.

    For each production, the first element (p[0]) is the left-hand side of the production,
    and the remaining elements (p[1:]) are the right-hand side of the production.

    Parameters:
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


def __add_to_set(X: str, set: dict[str, set], symbols_set: set):
    initial = len(set[X])
    set[X].update(symbols_set)
    return len(set[X]) > initial


def calculate_first(productions: list[str], terminals: list[str], variables: list[str]):
    """
    Calculates the First set for each variable in a grammar.

    Parameters:
        productions (list[str]): List of productions of the grammar.
        terminals (list[str]): List of terminals of the grammar.
        variables (list[str]): List of variables of the grammar.

    Returns:
        dict[str, set]: A dictionary where the keys are the variables and the values are the corresponding First sets.
    """

    first_set = {var: set() for var in variables}

    while True:
        updated = False
        for prod in productions:
            left, right = prod[0], prod[1:]

            if right[0] in variables:
                can_be_empty = True
                for symbol in right:
                    if symbol not in variables:
                        continue

                    updated |= __add_to_set(
                        left, first_set, first_set[symbol] - {"ɛ"})
                    if "ɛ" not in first_set[symbol]:
                        can_be_empty = False
                        break

                if can_be_empty:
                    updated |= __add_to_set(left, first_set, set("ɛ"))
            else:
                if len(right) == 1 and right[0] == "ɛ":
                    # APENAS PRODUÇÂO VAZIA
                    updated |= __add_to_set(left, first_set, set("ɛ"))
                # TERMINAL OU PRIMEIRO ELEMENTO É VAZIO
                updated |= __add_to_set(
                    left, first_set, set([right[0]]) - {"ɛ"})

        if not updated:
            break

    return first_set


if __name__ == "__main__":
    test_productions = [
        [
            "E' -> E",
            "E -> E \\+ n",
            "E -> n"
        ],
        [
            "E -> T E'",
            "E' -> v T E'",
            "E' -> ε",
            "T -> F T'",
            "T' -> \\^ F T'",
            "T' -> ε",
            "F -> \\¬ F",
            "F -> id"
        ],
        [
            "S -> A B",
            "A -> a A",
            "A -> a",
            "B -> b B",
            "B -> b"
        ],
        [
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
        [
            "S -> X Y Z",
            "X -> a X b",
            "X -> ɛ",
            "Y -> c Y Z c X",
            "Y -> d",
            "Z -> e Z Y e",
            "Z -> f"
        ]
    ]
    test_first_set = [
        {"E'": {"n"}, "E": {"n"}},
        {"E": {"\\¬", "id"}, "E'": {"v", "ε"}, "T": {
            "\\¬", "id"}, "T'": {"ε", "\\^"}, "F": {"\\¬", "id"}},
        {"B": {"b"}, "S": {"a"}, "A": {"a"}},
        {"D": {"c", "ɛ", "g"}, "A": {"c", "a", "ɛ", "g"}, "B": {
            "b", "ɛ", "f"}, "S": {"ɛ", "g", "c", "a", "f", "b"}, "C": {"c"}},
        {"Z": {"e", "f"}, "S": {"c", "a", "d"}, "X": {"a", "ɛ"}, "Y": {"d", "c"}}
    ]

    def __check(real_set: dict, calculated_set: dict):
        return real_set.items() == calculated_set.items()

    for i, prod in enumerate(test_productions):
        productions, terminals, variables = split_productions(prod)
        first_set = calculate_first(productions, terminals, variables)
        passed = __check(test_first_set[i], first_set)
        print(f"------- Produções {i} -------")
        print(prod)
        print(f"FIRST Calculated Set: {first_set}")
        print(f"FIRST Real Set: {test_first_set[i]}")
        print(f"FIRST Test passed: {passed}")
