import sys
import argparse


# Parses arguments
def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input')
    parser.add_argument('-o', '--output')
    parser.add_argument('-l', '--line-length', default=80)
    parser.add_argument('-p', '--paragraph-spaces', default=4)

    return parser.parse_args(sys.argv[1:])


# Stores formatted text
class Result:
    def __init__(self):
        self.buffer = ''
        self.line_len = 0
        self.l = 80
        self.p = 4

    def new_line(self):
        self.buffer += '\n'

    def indent(self):
        for j in xrange(self.p):
            self.buffer += ' '
        result.line_len = self.p

    def write(self, word):
        if len(word) > self.l:
            sys.exit(2)

        if self.line_len + len(word) + 1 > self.l:
            # Break line
            self.buffer += '\n'
            self.line_len = 0

        # Write a word
        self.buffer += word
        self.buffer += ' '
        self.line_len += len(word) + 1

# Punctuation marks
marks = [',', '.', '?', '!', '-', ':', '`']

# Parsing args
args = parse_args()

# Reading text
if args.input is None:
    text = sys.stdin.read()
else:
    f = open(args.input, "rt")
    text = f.read()
    f.close()

word = ''
new_para = False
new_word = False
result = Result()
result.l = int(args.line_length)
result.p = int(args.paragraph_spaces)

# Formatting text
result.indent()
for c in text.strip():
    # Checking for new paragraphs
    if c == '\n':
        new_para = True
        new_word = True
    elif new_para:
        result.new_line()
        result.indent()
        new_para = False

    # Checking for new words in line
    if c == ' ' or c in marks:
        new_word = True
    if c != ' ':
        if c not in marks and new_word:
            result.write(word)
            word = ''
            new_word = False
        if c != '\n':
            word += c
result.write(word)

# Writing output
if args.output is None:
    print result.buffer
else:
    f = open(args.output, "wt")
    f.write(result.buffer)
    f.close()

