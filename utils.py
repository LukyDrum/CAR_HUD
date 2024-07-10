def limit_text(text: str, limit: int) -> str:
    if len(text) > limit:
        return text[:limit - 3] + "..."
    else:
        return text