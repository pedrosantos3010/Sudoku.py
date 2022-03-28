from game_input import GameInput
from game_view import GameView
from level_generator import LevelGenerator


def get_game_options():
    _difficulty = {
        1: {'name': "Impossível", "hints": 10},
        2: {'name': "Difícil", "hints": 20},
        3: {'name': "Médio", "hints": 30},
        3: {'name': "Fácil", "hints": 40},
        9: {'name': "Molezinha", "hints": 80}
    }

    _options = {
        'difficulty': 0
    }
    while _options['difficulty'] == 0:
        try:
            print("\nSelecione a dificuldade:")
            for k, v in _difficulty.items():
                print(f'\t{k} - {v["name"]} ({v["hints"]} dicas);')
            _selection = int(input("escolha: "))
        except:
            print("Digite um número inteiro válido...")

        _selected_difficulty = _difficulty.get(_selection, 0)
        _options['difficulty'] = _selected_difficulty["hints"]
        if _options['difficulty'] == 0:
            print("Opção inválida, tente novamente...")

    return _options


def create_new_level():
    level_generator = LevelGenerator()

    game_level = [[0 for i in range(9)] for j in range(9)]
    created_level = level_generator.create_level()
    options = get_game_options()

    hints = level_generator.get_hints(options["difficulty"])
    for hint in hints:
        game_level[hint.row][hint.column] = hint.value

    return game_level, created_level


if __name__ == '__main__':
    game_display = GameView(int(input("tamanho da tela: ")))
    game_input = GameInput()

    game_created = False
    game_end = False

    while not game_end:
        if not game_created:
            game_level, created_level = create_new_level()
            game_created = True

        try:
            game_display.display_game(game_level)

            if created_level == game_level:
                print("venceu caraio!")

                if input("Criar novo jogo? (y/N)").lower() == 'y':
                    create_new_level = True
                else:
                    game_end = True

            cell = game_input.get_input()
            game_level[cell.row][cell.column] = cell.value

        except Exception as e:
            print("Não foi possível ler dados inputados")
            print(e)
            game_end = True

    print("jogo finalizado")
