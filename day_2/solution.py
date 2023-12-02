def solution():
    data = extract_data_from_file()
    games = list_games(data)
    info_for_all_games = compile_info_for_all_games(games)
    id_sum = 0
    for game_info in info_for_all_games:
        game_id = get_game_id_if_all_scenarios_possible(game_info, [{"color": "red", "count": 12}, {"color": "green", "count": 13}, {"color": "blue", "count": 14}])
        id_sum += game_id
    return id_sum

def get_game_id_if_all_scenarios_possible(game_info: dict, color_count_rules: [dict]) -> int:
    game_id = game_info["id"]
    if check_if_any_maximum_exceeded_in_scenarios(game_info["scenarios"], color_count_rules):
        game_id = 0
    return game_id

def check_if_any_maximum_exceeded_in_scenarios(scenarios: [[dict]], color_count_rules: [dict]) -> bool:
    exceeded = False
    for scenario in scenarios:
        for color_count_pair in color_count_rules:
            if check_if_maximum_exceeded_in_scenario(scenario, color_count_pair["color"], color_count_pair["count"]):
                exceeded = True
    return exceeded

def check_if_maximum_exceeded_in_scenario(scenario: [dict], color: str, max: int) -> bool:
    exceeded = False
    for block_details in scenario:
        if block_details["color"] == color:
            if block_details["count"] > max:
                exceeded = True
    return exceeded

def compile_info_for_all_games(games: [str]) -> [dict]:
    all_info = []
    for game in games:
        game_info = compile_game_info(game)
        all_info.append(game_info)
    return all_info

def compile_game_info(game: str) -> dict:
    main_sections = separate_description_from_sets(game)
    game_id = determine_game_id(main_sections[0])
    game_scenarios = determine_block_scenarios_for_game(main_sections[1])
    game_info = {
        "id": game_id,
        "scenarios": game_scenarios
    }
    return game_info

def determine_block_scenarios_for_game(collected_sets: str) -> [[dict]]:
    sets = collected_sets.split("; ")
    block_scenarios = []
    for single_set in sets:
        block_details = determine_block_details_for_scenario(single_set)
        block_scenarios.append(block_details)
    return block_scenarios

def determine_block_details_for_scenario(single_set: str) -> [dict]:
    cubes = single_set.split(", ")
    block_details = []
    for cube_description in cubes:
        cube_pieces = cube_description.split(" ")
        color = cube_pieces[1]
        count = int(cube_pieces[0])
        block_details.append({
            "color": color,
            "count": count
        })
    return block_details

def determine_game_id(description: str) -> int:
    description_sections = description.split(" ")
    game_id = int(description_sections[1])
    return game_id

def separate_description_from_sets(game: str) -> [str]:
    main_sections = game.split(": ")
    return main_sections

def list_games(data: str) -> [str]:
    games = data.split("\n")
    return games

def extract_data_from_file() -> str:
    file = open("data.txt", "r")
    data = file.read()
    file.close()
    return data

result = solution()
print(result)