# Last updated: 8/20/2025, 5:50:22 PM
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # If there's only one row or the string is empty, no zigzag conversion is needed.
        if numRows == 1 or not s:
            return s

        # Create a list of strings, where each string will represent a row in the zigzag pattern.
        # The number of strings in the list will be equal to numRows.
        rows = [''] * numRows

        # Initialize variables to keep track of the current row and the direction of movement.
        # 'current_row' starts at the top row (index 0).
        # 'going_down' is a boolean flag, initially False, indicating we are moving downwards.
        # It's initialized to False because the first character will always go to row 0,
        # and then the direction will immediately switch to True to go down to row 1.
        current_row = 0
        going_down = False

        # Iterate through each character in the input string 's'.
        for char in s:
            # Append the current character to the string corresponding to the 'current_row'.
            rows[current_row] += char

            # Check if we need to change direction.
            # If 'current_row' is the first row (0) or the last row (numRows - 1),
            # we need to reverse the direction.
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down # Toggle the direction

            # Move to the next row based on the current direction.
            if going_down:
                current_row += 1 # Move downwards
            else:
                current_row -= 1 # Move upwards

        # After processing all characters, join all the strings in the 'rows' list
        # to form the final zigzag converted string.
        return "".join(rows)

