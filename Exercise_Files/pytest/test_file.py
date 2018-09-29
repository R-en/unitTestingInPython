class TestClass:
    @classmethod
    def setup_class(cls):
        print("\nSetting up class")

    @classmethod
    def teardown_class(cls):
        print("\nTearing down class")

    def setup_method(self, method):
        if method == self.test1:
            print("\nSetting up test 1")
        elif method == self.test2:
            print("\nSetting up test 2")
        else:
            print("\nSetting up unknown test")

    def teardown_method(self, method):
        if method == self.test1:
            print("\nTearing down test 1")
        elif method == self.test2:
            print("\nTearing down test 2")
        else:
            print("\nTearing down unknown test")

    def test1(self):
        print("Executing test 1")
        assert True

    def test2(self):
        print("Executing test 2")
        assert True