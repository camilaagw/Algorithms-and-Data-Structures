"""
Given a math equation, write an algorithm to tell whether the brackets are well balanced.
Brackets can be any of these: (,),[,],{,}. For example, this is unbalanced: [(2+3{}],
and this is balanced: (3-[3*{4}])
"""


def main(equation='[(2+3{}]'):
    symbols = {'(': ')',
               '{': '}',
               '[': ']'}

    my_stack = []

    for char in equation:
        if char in symbols.keys():
            my_stack.append(char)
        elif char in symbols.values():
            if (not my_stack) or (symbols[my_stack.pop()] != char):
                return False

    return my_stack == []


if __name__ == '__main__':

    assert main('(3-[3*{4}])')
    assert main('[(2+3{})]')
    assert not main('[(2+3{}]')
    assert not main('([)]')
    assert main('')
    assert not main('))))')
    assert not main('((((')
    assert not main('))((')
