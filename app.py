import re
      
def replace_words_with_numbers(input_string):
    # Define a dictionary mapping words to their numerical representations
    word_to_number = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    # Define a regular expression pattern to find the words
    pattern = re.compile('|'.join(re.escape(word) for word in word_to_number.keys()), re.IGNORECASE)

    # Use the sub method to replace matched words with their numerical representations
    result_string = pattern.sub(lambda x: word_to_number[x.group(0).lower()], input_string)

    return result_string

def first_and_last_numbers(line):
    digits = [x for x in line if x.isdigit()]
    return (digits[0], digits[-1])

def calculate_answer(f):
    sum = 0
    for line in f:
        line = replace_words_with_numbers(line)
        numbers = first_and_last_numbers(line)
        sum += int(numbers[0] + "" + numbers[1])
    return sum

if __name__ == "__main__": 
    f = open("./inputs/input1-1.txt", "r")
    answer = calculate_answer(f)
    print(answer)