n = int(input())
piece_composer = {}
piece_keys = {}
for _ in range(n):
    data = input().split("|")
    piece = data[0]
    composer = data[1]
    piece_key = data[2]
    piece_composer[piece] = composer
    piece_keys[piece] = piece_key
line = input()
while not line == "Stop":
    data = line.split("|")
    command = data[0]
    if command == "Add":
        piece = data[1]
        composer = data[2]
        piece_key = data[3]
        if piece in piece_composer:
            print(f"{piece} is already in the collection!")
        else:
            piece_composer[piece] = composer
            piece_keys[piece] = piece_key
            print(f"{piece} by {composer} in {piece_key} added to the collection!")
    elif command == "Remove":
        piece = data[1]
        if piece not in piece_composer:
            print(f"Invalid operation! {piece} does not exist in the collection.")
        else:
            piece_composer.pop(piece)
            piece_keys.pop(piece)
            print(f"Successfully removed {piece}!")
    elif command == "ChangeKey":
        piece = data[1]
        new_key = data[2]
        if piece not in piece_keys:
            print(f"Invalid operation! {piece} does not exist in the collection.")
        else:
            piece_keys[piece] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
    line = input()

piece_composer = dict(sorted(piece_composer.items(), key=lambda el: (el[0], el[1])))
for key in piece_composer:
    print(f"{key} -> Composer: {piece_composer[key]}, Key: {piece_keys[key]}")
