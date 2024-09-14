import ast

class TableExtractor:
    def __init__(self, table_contents):
        self.table_contents = table_contents

    def extract_ordered_table(self):
        # Convert the string representation of the list to an actual list
        table = ast.literal_eval(self.table_contents)

        # Assume the first row is the header
        header = table[0]

        # Sort the remaining rows based on the first column (assuming it's the order column)
        sorted_rows = sorted(table[1:], key=lambda x: x[0])

        # Combine header and sorted rows
        ordered_table = [header] + sorted_rows

        return ordered_table