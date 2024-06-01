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

    def __first_of(symbol):
        """
        Função interna que retorna o conjunto FIRST de um símbolo.

        Args:
        symbol (str): O símbolo para o qual se deseja calcular o conjunto FIRST.

        Returns:
        set: O conjunto FIRST do símbolo.
        """
        if symbol in aux_terminals:  # Se terminal, retornar o cunjunto somente com o terminal
            return {symbol}
        if symbol == "ε":  # Se vazio, retornar o conjunto contendo apenas vazio
            return {"ε"}
        return first_set[symbol]  # Se for variável, retorna o conjunto FIRST da variável

    def __add_to_first_set(X, symbols_set):
        """
        Função interna que adiciona símbolos ao conjunto FIRST de uma variável.

        Args:
        X (str): A variável para a qual se deseja adicionar símbolos ao conjunto FIRST.
        symbols_set (set): O conjunto de símbolos a ser adicionado ao conjunto FIRST de X.

        Returns:
        bool: True se o conjunto FIRST de X foi atualizado, False caso contrário.
        """
        initial = len(first_set[X])
        first_set[X].update(symbols_set)
        return len(first_set[X]) > initial

    while True:
        updated = False

        for prod in productions:
            left, right = prod[0], prod[1:]

            add_epsilon = True  
            for symbol in right:
                f = __first_of(symbol)
                updated |= __add_to_first_set(left, f - {"ε"})

                if "ε" not in f:  # símbolo não produz ε, atualiza a flag e sai do loop
                    add_epsilon = False
                    break

            if add_epsilon: # todas simbolos da produção produzem ε, adicionar ε a FIRST(left)
                updated |= __add_to_first_set(left, {"ε"})

        if not updated: # Nenhum conjunto FIRST foi atualizado, terminar execução
            break
    return {k: list(v) for k, v in first_set.items()}

def calculate_follow(productions: list[list[str]], first_set: dict[str, list], variables: list[str]):
    return None

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