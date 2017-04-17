import sys, unittest
from StringIO import StringIO
from App import main

class my_tests(unittest.TestCase):
    """Lets test!"""

    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()
        self.message = 'YOU DONT KNOW HOW TO PLAY :-)'

    def test_no_parameters(self):
        sys.argv = ["App.py"]
        main()
        self.assertIn(self.message, sys.stdout.getvalue())

    def test_parameters_json1(self):
        sys.argv = ["App.py", "",]
        main()
        self.assertIn(self.message, sys.stdout.getvalue())

    def test_parameters_json2(self):
        sys.argv = ["App.py", "data"]
        main()
        self.assertIn(self.message, sys.stdout.getvalue())

    def test_parameters_start_node1(self):
        sys.argv = ["App.py", "data.json", "-1", "knife", "Potted Plan"]
        main()
        self.assertIn(self.message, sys.stdout.getvalue())

    def test_parameters_start_node2(self):
        sys.argv = ["App.py", "data.json", "0", "knife", "Potted Plan"]
        main()
        self.assertIn(self.message, sys.stdout.getvalue())

    def test_parameters_start_node3(self):
        sys.argv = ["App.py", "data.json", "", "knife", "Potted Plan"]
        main()
        self.assertIn(self.message, sys.stdout.getvalue())

    def test_parameters_needles1(self):
        sys.argv = ["App.py", "data.json", "2"]
        main()
        self.assertIn(self.message, sys.stdout.getvalue())

    def test_parameters_needles2(self):
        sys.argv = ["App.py", "data.json", "2", ""]
        main()
        self.assertIn(self.message, sys.stdout.getvalue())

    def test_parameters_needles3(self):
        sys.argv = ["App.py", "data.json", "2", "knife", "Potted Plan", "Other1", "Other2", "Other3"]
        main()
        self.assertIn('STARTING AT ID', sys.stdout.getvalue())

    def test_parameters_start_node4(self):
        sys.argv = ["App.py", "data.json", "2", "", ""]
        main()
        self.assertIn(self.message, sys.stdout.getvalue())



if __name__ == '__main__':
    unittest.main()