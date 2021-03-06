from py_pkg_jraza19 import __version__
from py_pkg_jraza19 import py_pkg_jraza19
import pandas as pd


def test_version():
    assert __version__ == "0.1.0"


def test_catbind():
    a = pd.Categorical(["character", "hits", "your", "eyeballs"])
    b = pd.Categorical(["but", "integer", "where it", "counts"])
    assert ((py_pkg_jraza19.catbind(a, b)).codes == [1, 4, 7, 3, 0, 5, 6, 2]).all()
    assert (
        (py_pkg_jraza19.catbind(a, b)).categories
        == [
            "but",
            "character",
            "counts",
            "eyeballs",
            "hits",
            "integer",
            "where it",
            "your",
        ]
    ).all()
