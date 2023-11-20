class Solution:
  # FIRST HARD UNDER 30 MINS
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        # Initialize variables to store the result, current line, and total number of letters
        result, cur, num_of_letters = [], [], 0
        
        # Iterate through each word in the input list of words
        for word in words:
            # Check if adding the current word exceeds the maxWidth limit for the current line
            if num_of_letters + len(word) + len(cur) > maxWidth:
                # Distribute extra spaces evenly between words in the current line
                for i in range(maxWidth - num_of_letters):
                    cur[i % (len(cur) - 1 or 1)] += ' '
                # Add the formatted line to the result
                result.append(''.join(cur))
                # Reset current line and total number of letters
                cur, num_of_letters = [], 0
            # Add the current word to the current line and update the total number of letters
            cur += [word]
            num_of_letters += len(word)
        
        # Left-justify the last line and add it to the result
        return result + [' '.join(cur).ljust(maxWidth)]
