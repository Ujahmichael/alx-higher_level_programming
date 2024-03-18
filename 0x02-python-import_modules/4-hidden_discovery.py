#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    
    names = dir(hidden_4)

    sorted_name = sorted(name for name in names if not name.startswith("_"))

    for name in sorted_name:
        print(name)
