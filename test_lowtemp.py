import lowtemp

from colorama import Fore


def test_get_color():
    assert lowtemp.get_color(32) == Fore.RED
    assert lowtemp.get_color(-1) == Fore.RED
    assert lowtemp.get_color(0) == Fore.RED
    assert lowtemp.get_color(1) == Fore.RED
    assert lowtemp.get_color(33) == Fore.YELLOW
    assert lowtemp.get_color(40) == Fore.YELLOW
    assert lowtemp.get_color(41) == Fore.GREEN
    assert lowtemp.get_color(100) == Fore.GREEN
    assert lowtemp.get_color(999) == Fore.GREEN


def test_get_meridiem():
    assert lowtemp.get_meridiem(0) == (12, 'am')
    assert lowtemp.get_meridiem(1) == (1, 'am')
    assert lowtemp.get_meridiem(10) == (10, 'am')
    assert lowtemp.get_meridiem(12) == (12, 'pm')
    assert lowtemp.get_meridiem(20) == (8, 'pm')
    assert lowtemp.get_meridiem(23) == (11, 'pm')


def test_pull_time():
    assert lowtemp.pull_time('2023-12-22T00:00:00-06:00') == 0
    assert lowtemp.pull_time('2023-12-22T01:00:00-06:00') == 1
    assert lowtemp.pull_time('2023-12-22T06:00:00-06:00') == 6
    assert lowtemp.pull_time('2023-12-22T11:00:00-06:00') == 11
    assert lowtemp.pull_time('2023-12-22T12:00:00-06:00') == 12
    assert lowtemp.pull_time('2023-12-22T15:00:00-06:00') == 15
    assert lowtemp.pull_time('2023-12-22T18:00:00-06:00') == 18
    assert lowtemp.pull_time('2023-12-22T23:00:00-06:00') == 23


def test_graph():
    assert lowtemp.graph(32) == "\u2588" * 16
    assert lowtemp.graph(2) == "\u2588" * 1
    assert lowtemp.graph(33) == "\u2588" * 16
    assert lowtemp.graph(40) == "\u2588" * 20
    assert lowtemp.graph(85) == "\u2588" * 42
    assert lowtemp.graph(-1) == "\u2588" * 0


