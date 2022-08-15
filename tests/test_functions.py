import modules.module as module
import pandas as pd
import pytest

def test_add():

    # test basic functionality
    assert module.add(1,1) == 2

    # try a border case
    assert module.add(-1,-1) == -2


def test_add_col():

    # creating starting dataframe
    df = pd.DataFrame(
                    [[0, 1], [2, 3]],
                    index=['cat', 'dog'],
                    columns=['weight', 'height'])

    # expected
    df_expected = pd.DataFrame(
                       [[0, 1, 2], [2, 3, 2]],
                       index=['cat', 'dog'],
                       columns=['weight', 'height', 'n_ears'])

    # test the result
    assert module.add_col(df, 'n_ears', 2).equals(df_expected)


# test parameterization
@pytest.mark.parametrize("a, b, expected", [[2, 1, 1], [-1 ,1 ,-2]])

def test_subtract(a, b, expected):

    assert module.subtract(a, b) == expected


# fixture
@pytest.fixture()
def df():

    df = pd.DataFrame([[0, 1], [2, 3]],
                       index=['wallaby', 'kangaroo'],
                       columns=['weight', 'height'])
    return(df)


def test_add_col2(df):
    # expected
    df_expected = pd.DataFrame(
                       [[0, 1, 3], [2, 3, 5]],
                       index=['wallaby', 'kangaroo'],
                       columns=['weight', 'height', 'hop_height'])
    assert module.add_col(df, 
                           'hop_height',
                           [3,5]).equals(df_expected)

