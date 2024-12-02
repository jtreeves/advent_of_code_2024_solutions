from typing import List


def get_list_of_lines(block: str) -> List[str]:
    lines = block.split("\n")
    return list(filter(None, lines))
