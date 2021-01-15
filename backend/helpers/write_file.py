def write_file(path: str, line: str) -> None:
    with open(path, 'a') as file:
        file.write(f'{line}\n')
