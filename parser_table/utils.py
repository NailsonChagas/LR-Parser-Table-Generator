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


def __first_of(symbol: str, first_set: dict[str, set], terminals: list[str]):
    """
    Retorna o conjunto FIRST de um símbolo.

    Args:
    symbol (str): O símbolo para o qual se deseja calcular o conjunto FIRST.

    Returns:
    set: O conjunto FIRST do símbolo.
    """
    if symbol in terminals:
        # Se terminal, retornar o cunjunto somente com o terminal
        return {symbol}
    if symbol == "ε":
        return {"ε"}  # Se vazio, retornar o conjunto contendo apenas vazio
    # Se for variável, retorna o conjunto FIRST da variável
    return first_set[symbol]


def __add_to_first_set(X: str, first_set: dict[str, set], symbols_set: set):
    """
    Adiciona símbolos ao conjunto FIRST de uma variável.

    Args:
    X (str): A variável para a qual se deseja adicionar símbolos ao conjunto FIRST.
    symbols_set (set): O conjunto de símbolos a ser adicionado ao conjunto FIRST de X.

    Returns:
    bool: True se o conjunto FIRST de X foi atualizado, False caso contrário.
    """
    initial = len(first_set[X])
    first_set[X].update(symbols_set)
    return len(first_set[X]) > initial


def calculate_first(productions: list[list[str]], terminals: list[str], variables: list[str]):
    """
    Calcula o conjunto FIRST para cada variável de uma gramática.

    Args:
    productions (list[list[str]]): Lista de produções da gramática.
    terminals (list[str]): Lista de símbolos terminais da gramática.
    variables (list[str]): Lista de variáveis da gramática.

    Returns:
    dict: Um dicionário onde as chaves são as variáveis e os valores são listas dos símbolos em seus conjuntos FIRST.
    """
    first_set = {var: set() for var in variables}
    aux_terminals = [t for t in terminals if t != "ε"]

    while True:
        updated = False
        for prod in productions:
            left, right = prod[0], prod[1:]
            add_epsilon = True
            for symbol in right:
                f = __first_of(symbol, first_set, aux_terminals)
                updated |= __add_to_first_set(left, first_set, f - {"ε"})
                if "ε" not in f:  # símbolo não produz ε, atualiza a flag e sai do loop
                    add_epsilon = False
                    break
            # todas simbolos da produção produzem ε, adicionar ε a FIRST(left)
            if add_epsilon:
                updated |= __add_to_first_set(left, first_set, {"ε"})
        if not updated:
            break  # Nenhum conjunto FIRST foi atualizado, terminar execução
    return {k: list(v) for k, v in first_set.items()}


def calculate_follow(productions: list[list[str]], first_set: dict[str, list], terminals: list[str], variables: list[str]):
    follow_set = {var: set() for var in variables}

    return {k: list(v) for k, v in follow_set.items()}


if __name__ == "__main__":
    productions1 = [
        "E' -> E",
        "E -> E + n",
        "E -> n"
    ]

    productions2 = [
        "E -> T E'",
        "E' -> v T E'",
        "E -> ε",
        "T -> F T'",
        "T' -> \\^ F T'",
        "T' -> ε",
        "F -> \\¬ F",
        "F -> id"
    ]
    productions, terminals, variables = split_productions(productions1)
    first = calculate_first(productions, terminals, variables)
    print(first)

    productions, terminals, variables = split_productions(productions2)
    first = calculate_first(productions, terminals, variables)
    print(first)
