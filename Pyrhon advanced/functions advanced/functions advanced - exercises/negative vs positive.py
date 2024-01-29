def separated_numbers(numbers):
    positive_numbers = [num for num in numbers if num > 0]
    negative_numbers = [num for num in numbers if num < 0]
    return positive_numbers, negative_numbers

def sum_numbers(numbers):
    positive_numbers, negative_numbers = separated_numbers(numbers)
    sum_positive = sum(positive_numbers)
    sum_negative = sum(negative_numbers)
    return sum_positive, sum_negative

def print_pos_neg_numbers(numbers):
    sum_positive, sum_negative = sum_numbers(numbers)
    print(sum_negative)
    print(sum_positive)

def absolute_max_p_n(numbers):
    sum_positive, sum_negative = sum_numbers(numbers)
    absolute_max = max(abs(sum_positive), abs(sum_negative))
    if absolute_max > sum_positive:
        print("The negatives are stronger than the positives")
    else:
        print("The positives are stronger than the negatives")


input_numbers = [int(n) for n in input().split()]

print_pos_neg_numbers(input_numbers)
absolute_max_p_n(input_numbers)
