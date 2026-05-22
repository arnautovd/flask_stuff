def get_sum(a: int, b: int) -> int:
    """Return the sum of two integers."""
    return a + b


CENSORED_WORDS = ['fuck', 'suck']
CENSORED_MESSAGE = 'CENSORED'


def censor_check(data: str) -> str:
    """Check if data contains censored words and return appropriate message."""
    # Check for censored words as substrings (case-insensitive)
    data_lower = data.lower()
    for word in CENSORED_WORDS:
        if word.lower() in data_lower:
            return CENSORED_MESSAGE
    return format_message(data)


def format_message(data: str) -> str:
    """Format the data with its length."""
    return f"The length of {data} is {len(data)}"