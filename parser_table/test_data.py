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

def check(real_set: dict, calculated_set: dict):
    return real_set.items() == calculated_set.items()