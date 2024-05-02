#!/bin/python
from samgob import DiceSetParser
import sys
import os

#for control flow parsing and determining how to parse out our values
from samgob.iterators.file_word_parser import RegexFileIterator
from samgob.iterators.control_flow_iterator import ControlFlowIterator
from samgob.iterators.control_flow_iterator import IgnoreControlIterator
import re

def main():
        if len(sys.argv) == 1:
            print("usage:")
            print("\tinterpret file: pydice -f <fname>")
            print("\tcompile file: pydice -c <fname>")
            print("\tinterpret commands: pydice <dice lang>")
            quit()

        stream = None

        dice_set_parser = DiceSetParser()

        if sys.argv[1] == '-f':
            stream = ControlFlowIterator(
                RegexFileIterator(sys.argv[2],
                                    re.compile("[^\\s]+\\s"))
            )
        elif sys.argv[1] == '-c':
            stream = IgnoreControlIterator(
                        RegexFileIterator(sys.argv[2],
                                            re.compile("[^\\s]+\\s"))
                    )
            dice_set_parser.do_compile = True
        else:
            stream = ControlFlowIterator(iter(sys.argv[1:]))

        print(dice_set_parser.compile_langauge(stream))

if __name__ == '__main__':
    main()
