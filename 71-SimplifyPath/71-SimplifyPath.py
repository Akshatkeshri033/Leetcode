# Last updated: 8/20/2025, 5:49:35 PM
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        parts = path.split("/")

        for part in parts:
            if part == "" or part == ".":
                # Ignore empty parts (caused by //) and current directory
                continue
            elif part == "..":
                # Go up to the parent directory if possible
                if stack:
                    stack.pop()
            else:
                # Valid directory/file name
                stack.append(part)

        # Join stack into canonical path
        return "/" + "/".join(stack)