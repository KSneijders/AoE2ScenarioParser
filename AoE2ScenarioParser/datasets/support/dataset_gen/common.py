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
    string = regex.sub(r"_+", "_", string)

    return string
