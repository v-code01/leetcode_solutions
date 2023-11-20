class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Initialize dictionaries to track character frequencies in t and the current window
        t_freq, window_freq = {}, {}
        
        # Populate t_freq dictionary with character frequencies from t
        for char in t:
            t_freq[char] = t_freq.get(char, 0) + 1
        
        # Initialize pointers and variables to track the minimum window
        left, right, min_len, min_window = 0, 0, float('inf'), ""
        required_chars = len(t)
        
        while right < len(s):
            # Expand the window to the right
            if s[right] in t_freq:
                window_freq[s[right]] = window_freq.get(s[right], 0) + 1
                if window_freq[s[right]] <= t_freq[s[right]]:
                    required_chars -= 1
            
            # Contract the window from the left
            while required_chars == 0:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_window = s[left:right + 1]
                
                if s[left] in t_freq:
                    window_freq[s[left]] -= 1
                    if window_freq[s[left]] < t_freq[s[left]]:
                        required_chars += 1
                
                # Move left pointer to the right
                left += 1
            
            # Move right pointer to the right
            right += 1
        
        return min_window
