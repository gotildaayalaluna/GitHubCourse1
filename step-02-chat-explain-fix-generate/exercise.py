def parse_scoreboard(raw: str) -> dict[str, int]:
    """Parse 'name:score' pairs separated by commas.

    Example: "alice:10,bob:9,alice:14" -> {"alice": 14, "bob": 9}

    Invalid segments should be skipped.
    """
    board: dict[str, int] = {}
    if raw.strip() == "":
        return board

    parts = raw.split(",")
    for part in parts:
        try:
            name, score = part.split(":")
            name = name.strip().lower()
            value = int(score.strip())
            if name in board:
                board[name] = max(board[name], value)
            else:
                board[name] = value
        except (ValueError, AttributeError):
            # Skip malformed segments
            continue
    return board


def top_player(board: dict[str, int]) -> tuple[str, int] | None:
    """Return the player with the highest score, else None.

    Keep this deterministic by sorting names alphabetically when scores tie.
    """
    if not board:
        return None
    # Sort by score descending, then by name ascending for ties
    sorted_players = sorted(board.items(), key=lambda x: (-x[1], x[0]))
    return sorted_players[0]