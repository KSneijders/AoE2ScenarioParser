from regex import regex


def tab(string: str) -> str:
    return f"    {string}"

def train_case(string: str) -> str:
    string = (
        string
        .upper()
        .replace(" ", "_")
        .replace("%", "PERCENT")
    )
    string = regex.sub(r"[!()/]", "", string)

    return string