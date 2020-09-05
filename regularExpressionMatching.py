def is_match_helper(text, pattern, start_text, start_pattern):
    if start_text == len(text) and start_pattern == len(pattern):
        return True
    if start_pattern >= len(pattern):
        return False
    if start_pattern + 1 < len(pattern) and pattern[start_pattern + 1] == '*':
        any_true = False
        any_true = any_true or is_match_helper(text, pattern, start_text, start_pattern +2)
        text_char = pattern[start_pattern]
        while start_text < len(text) and (text_char == '.' or text_char == text[start_text]):
            if any_true:
                return True
            start_text += 1
            any_true = any_true or is_match_helper(text, pattern, start_text, start_pattern+2)
        return any_true
    elif pattern[start_pattern] == '.':
        if start_text >= len(text):
            return False
        return is_match_helper(text, pattern, start_text +1, start_pattern+1)
    else:
        if start_text < len(text) and pattern[start_pattern] == text[start_text]:
            return is_match_helper(text, pattern, start_text+1, start_pattern+1)
        else:
            return False

class Solution:


    def isMatch(self, s: str, p: str) -> bool:
        return is_match_helper(s, p, 0, 0)
