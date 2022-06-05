__authors__ = "Sofiane Mahiou"
__copyright__ = "(c) 2022, Hazy Limited"
__license__ = ""
__contact__ = "Sofiane Mahiou <sofiane@hazy.com>"

from datetime import datetime
from Equation.similar import sim, nsim, gsim, lsim
from Equation.util import addOp, addFn, addConst, addUnaryOp
import operator as op
import pandas as pd


def last(x):
    return x.iloc[-1]


def is_last(x):
    x = pd.Series(x)
    il = pd.Series(False, index=x.index)
    il.iloc[-1] = True
    return il


def rank(x):
    x = pd.Series(x)
    return x.rank(method="min", na_option="keep")


def dense_rank(x):
    x = pd.Series(x)
    return x.rank(method="dense", na_option="keep")


def year(x):
    return pd.Series(x, dtype="datetime64[ns]").dt.year


def month(x):
    return pd.Series(x, dtype="datetime64[ns]").dt.month


def day(x):
    return pd.Series(x, dtype="datetime64[ns]").dt.day


def weekday(x):
    return pd.Series(x, dtype="datetime64[ns]").dt.weekday


def dayofyear(x):
    return pd.Series(x, dtype="datetime64[ns]").dt.dayofyear


def hour(x):
    return pd.Series(x, dtype="datetime64[ns]").dt.hour


def minute(x):
    return pd.Series(x, dtype="datetime64[ns]").dt.minute


def second(x):
    return pd.Series(x, dtype="datetime64[ns]").dt.second


def microsecond(x):
    return pd.Series(x, dtype="datetime64[ns]").dt.microsecond


def days_in_month(x):
    return pd.Series(x, dtype="datetime64[ns]").dt.days_in_month


def is_month_end(x):
    return pd.Series(x, dtype="datetime64[ns]").dt.is_month_end


def is_month_start(x):
    return pd.Series(x, dtype="datetime64[ns]").dt.is_month_start


def is_year_start(x):
    return pd.Series(x, dtype="datetime64[ns]").dt.is_year_start


def pandas_if(condition, x, y):
    out = pd.Series(y)
    out.loc[condition] = x.loc[condition]
    return out


def equation_extend():
    addFn('last', "last({0:s})", "\\last\\left({0:s}\\right)", 1, last)
    addFn('is_last', "is_last({0:s})", "\\is_last\\left({0:s}\\right)", 1, is_last)
    addFn('rank', "rank({0:s})", "\\rank\\left({0:s}\\right)", 1, rank)
    addFn('dense_rank', "dense_rank({0:s})", "\\dense_rank\\left({0:s}\\right)", 1, dense_rank)
    addFn('year', "year({0:s})", "\\year\\left({0:s}\\right)", 1, year)
    addFn('month', "month({0:s})", "\\month\\left({0:s}\\right)", 1, month)
    addFn('day', "day({0:s})", "\\day\\left({0:s}\\right)", 1, day)
    addFn('weekday', "weekday({0:s})", "\\weekday\\left({0:s}\\right)", 1, weekday)
    addFn('dayofyear', "dayofyear({0:s})", "\\dayofyear\\left({0:s}\\right)", 1, dayofyear)
    addFn('hour', "hour({0:s})", "\\hour\\left({0:s}\\right)", 1, hour)
    addFn('minute', "minute({0:s})", "\\minute\\left({0:s}\\right)", 1, minute)
    addFn('second', "second({0:s})", "\\second\\left({0:s}\\right)", 1, second)
    addFn('microsecond', "microsecond({0:s})", "\\microsecond\\left({0:s}\\right)", 1, microsecond)
    addFn('days_in_month', "days_in_month({0:s})", "\\days_in_month\\left({0:s}\\right)", 1, days_in_month)
    addFn('is_month_end', "is_month_end({0:s})", "\\is_month_end\\left({0:s}\\right)", 1, is_month_end)
    addFn('is_month_start', "is_month_start({0:s})", "\\is_month_start\\left({0:s}\\right)", 1, is_month_start)
    addFn('is_year_start', "is_year_start({0:s})", "\\is_year_start\\left({0:s}\\right)", 1, is_year_start)
    addFn('last', "last({0:s})", "\\last\\left({0:s}\\right)", 1, last)
    # IF
    addFn('now', "now({0:s})", "\\now\\left({0:s}\\right)", 0, datetime.now)
    addFn('if', "if({0:s})", "\\if\\left({0:s}\\right)", 3, pandas_if)
