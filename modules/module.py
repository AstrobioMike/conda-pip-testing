import textwrap
import sys
import pandas as pd

### variables ###

# version
version = '0.1'

# setting some colors
tty_colors = {
    'green' : '\033[0;32m%s\033[0m',
    'yellow' : '\033[0;33m%s\033[0m',
    'red' : '\033[0;31m%s\033[0m'
}


### functions ###
def color_text(text, color='green'):
    if sys.stdout.isatty():
        return tty_colors[color] % text
    else:
        return text


def wprint(text):
    print(textwrap.fill(text, width = 80, initial_indent = "  ", 
          subsequent_indent="  ", break_on_hyphens = False))


def add(a, b):
    return(a + b)


def add_col(df, colname, coldata):
    
    # add a column to a DataFrame
    df[colname] = coldata
    return(df)


def subtract(a , b):
    return(a - b)

