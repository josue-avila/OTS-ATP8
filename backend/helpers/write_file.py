def write_file(path: str, line: str) -> None:
    file = open(path, 'a')
    file.write(f'{line}\n')
    file.close()