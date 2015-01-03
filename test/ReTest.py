__author__ = 'renliang'

import re


# re为未编译版本
def find_str_by_re():
    re_string = "{{(.*?)}}"
    some_thing = "this is a string with {{words}} embedded in\"" \
                 "{{curly breackerts}} to show an {{example}} of {{regular expressions}}"
    for match in re.findall(re_string, some_thing):
        print "MATCH->", match

# re 为编译版本
def find_str_by_re_comp():
    re_string = re.compile("{{(.*?)}}")
    some_thing = "this is a string with {{words}} embedded in\"" \
                 "{{curly breackerts}} to show an {{example}} of {{regular expressions}}"
    for match in re_string.findall(re_string, some_thing):
        print "MATCH->", match


def main():
    print "****************未编译版本****************"
    find_str_by_re()
    print "****************编译版本******************"
    find_str_by_re_comp()


if __name__ == '__main__':
    main()