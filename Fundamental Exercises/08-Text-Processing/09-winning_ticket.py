tickets = input().split(", ")
left_match_symbol = ""
right_match_symbol = ""
for ticket in tickets:
    left_count = 1
    right_count = 1
    if len(ticket) != 20:
        print("invalid ticket")
        continue
    for index in range(len(ticket) // 2):
        if ticket[index] == '$' or ticket[index] == '@' or ticket[index] == '#' or ticket[index] == '^':
            left_match_symbol = ticket[index]
            if ticket[index] == ticket[index + 1]:
                left_count += 1
    if left_count == 11:
        left_count -= 1
    for index in range(len(ticket) // 2, len(ticket) - 1):
        if ticket[index] == '$' or ticket[index] == '@' or ticket[index] == '#' or ticket[index] == '^':
            right_match_symbol = ticket[index]
            if ticket[index] == ticket[index + 1]:
                right_count += 1
    if left_count == right_count and 6 <= left_count <= 9:
        print(f" ticket \"{ticket}\" - {left_count}{left_match_symbol}")
    elif left_count == right_count == 10:
        print(f" ticket \"{ticket}\" - {left_count}{left_match_symbol} Jackpot!")
    else:
        print(f"ticket \"{ticket}\" - no match")
