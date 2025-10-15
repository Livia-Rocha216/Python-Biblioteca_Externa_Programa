import requests 

def moves_lvl16():
    pokemon_nome = input("Digite o nome do Pokémon: ")
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_nome.lower()}"
    resposta = requests.get(url)

    if resposta.status_code != 200:
        print("Pokémon não encontrado.")
        return
    
    dados = resposta.json()
    moves_lvl16 = set()

    for move in dados["moves"]:
        for detalhe in move["version_group_details"]:
            if (detalhe["move_learn_method"]["name"] == "level-up" and
                detalhe["level_learned_at"] == 16):
                moves_lvl16.add(move["move"]["name"])

    if moves_lvl16:
        print(f"Ataques que {pokemon_nome} aprende no nível 16:")
        for move in sorted(moves_lvl16):
            print(f"— {move}")
    else:
        print(f"{pokemon_nome} não aprende ataques no nível 16.")


moves_lvl16()
