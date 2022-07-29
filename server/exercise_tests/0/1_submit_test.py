from submission import sum


class TestSum:
    def test_positive(self):
        assert sum(1, 1) == 2
        assert sum(100000, 100000) == 200000

    def test_negative(self):
        assert sum(-1, -1) == -2
        assert sum(-100000, -100000) == -200000

    def test_mixed(self):
        assert sum(0, 1) == 1
        assert sum(-1, 1) == 0
        assert sum(0, 0) == 0
