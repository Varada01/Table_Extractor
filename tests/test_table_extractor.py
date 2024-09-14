import unittest
from src.table_parser import TableExtractor

class TestTableExtractor(unittest.TestCase):
    def test_extract_ordered_table(self):
        table_contents = """[
            ["Order", "Name", "Age"],
            [2, "Alice", 30],
            [1, "Bob", 25],
            [3, "Charlie", 35]
        ]"""
        
        extractor = TableExtractor(table_contents)
        result = extractor.extract_ordered_table()
        
        expected = [
            ["Order", "Name", "Age"],
            [1, "Bob", 25],
            [2, "Alice", 30],
            [3, "Charlie", 35]
        ]
        
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()