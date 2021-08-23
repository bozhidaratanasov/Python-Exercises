def negative_vs_positive(numbers):
    positive_sum = 0
    negative_sum = 0
    for number in numbers:
        if number >= 0:
            positive_sum += number
            continue
        negative_sum += number
    print(negative_sum)
    print(positive_sum)
    if abs(negative_sum) > positive_sum:
        print("The negatives are stronger than the positives")
    else:
        print("The positives are stronger than the negatives")


numbers = [int(el) for el in input().split()]
negative_vs_positive(numbers)
