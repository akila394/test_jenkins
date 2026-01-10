def get_base_url(env : str) -> str:
    env = (env or "").lower().strip()

    if env == "dev":
        return "https://dev.example.local"
    if env == "uat":
        return "https://uat.example.local"
    if env == "prod":
        return "https://prod.example.local"

    raise ValueError(f"Unknown env: {env}")

