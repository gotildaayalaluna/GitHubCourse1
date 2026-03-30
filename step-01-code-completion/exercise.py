import re


def normalize_username(name: str) -> str:
    """Normalize a username.

    Rules:
    - Trim outer whitespace.
    - Convert to lowercase.
    - Replace spaces with underscores.
    - Remove any character that is not a-z, 0-9, or underscore.
    - Collapse repeated underscores into one underscore.
    - Strip leading/trailing underscores.
    """
    # Trim outer whitespace and convert to lowercase
    result = name.strip().lower()
    # Replace spaces with underscores
    result = result.replace(' ', '_')
    # Remove any character that is not a-z, 0-9, or underscore
    result = re.sub(r'[^a-z0-9_]', '', result)
    # Collapse repeated underscores into one underscore
    result = re.sub(r'_+', '_', result)
    # Strip leading/trailing underscores
    result = result.strip('_')
    return result


def build_slug(title: str) -> str:
    """Convert a title into a URL-friendly slug.

    Rules:
    - Lowercase.
    - Keep letters and digits.
    - Replace any sequence of non-alphanumeric characters with a single '-'.
    - Strip leading/trailing '-'.
    """
    # Convert to lowercase
    result = title.lower()
    # Replace any sequence of non-alphanumeric characters with a single '-'
    result = re.sub(r'[^a-z0-9]+', '-', result)
    # Strip leading/trailing '-'
    result = result.strip('-')
    return result