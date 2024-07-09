def pass_dbus_variant(variant: str, keys: list) -> dict:
    lines = variant.strip().split("\n")
    i = 0
    
    values = {}

    while i < len(lines):
        line = lines[i].strip()
        
        contains = False
        active_key = None
        for key in keys:
            if key in line:
                contains = True
                active_key = key 
                break
        
        if contains:
            i += 1
            line = lines[i].strip()
            # Various strips - don't ask why
            value = line.split(" ", 2)[-1].strip().strip("string").strip().strip("\"")
            values[active_key] = value

        i += 1

    return values
