import re
from itertools import zip_longest


def convert_to_regular(text):
    """Helper function"""

    return re.sub(r"\s+", " ", text).strip()


def justify_line(line, width):
    """
    Justify line with
    :param line:
    :param width:
    :return:
    """

    justified = ""
    words = line.split(" ")
    words_len = len(line.replace(" ", ""))
    space_to_fill = width - words_len
    spaces = [" "] * (len(words) - 1)
    index = 0

    while spaces:
        if len("".join(spaces)) < space_to_fill:
            spaces[index] = f"{spaces[index]} "
            index += 1
            if index == len(spaces):
                index = 0
        else:
            break

    for word, space in zip_longest(words, spaces):
        if space is None:
            space = ""

        justified += f"{word}{space}"

    return justified


def justify(text: str, width: int):
    """
    Use spaces to fill in the gaps between words.
    Each line should contain as many words as possible.
    Use '\n' to separate lines.
    Gap between words can't differ by more than one space.
    Lines should end with a word not a space.
    '\n' is not included in the length of a line.
    Large gaps go first, then smaller ones ('Lorem--ipsum--dolor--sit-amet,' (2, 2, 2, 1 spaces)).
    Last line should not be justified, use only one space between words.
    Last line should not contain '\n'
    Strings with one word do not need gaps ('somelongword\n').

    :param text: input text
    :param width: line length
    :return: formatted text
    """

    words = convert_to_regular(text).split(" ")
    sentences = [""]
    index = 0

    for word in words:
        sentence = f"{sentences[index]} {word}".strip()

        if len(sentence) > width:
            sentences[index] = justify_line(sentences[index], width)
            sentences.append(word)
            index += 1
        else:
            sentences[index] = sentence

    justified = "\n".join(sentences)
    return justified
