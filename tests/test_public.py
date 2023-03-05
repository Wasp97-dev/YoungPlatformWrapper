from public import Public


class TestPing:
    def test_return_type(self):
        public = Public()
        assert isinstance(public.ping(), bool)

    def test_return_value(self):
        public = Public()
        assert public.ping() is True
