#! /usr/bin/env python
"""
    A simple numerological profile calculator. The calculations and profile
    elements are based on: http://www.dragondance.com/numerology.html
    
    Usage:
        ./numerology.py [or]
        python numerology.py
"""

INTERPRETATIONS = [
    "Zero. The system encountered an error somewhere.",
    # From various sources on the WWW. Change as desired:
    "One. Aggressiveness, courage, leadership, pioneering spirit.",
    "Two. Indecisiveness, adaptability, harmony, inner balance.",
    "Three. Expansiveness, optimism, enjoyment of labour's fruits.",
    "Four. Stability, orderliness, control, practicality, pragmatism.",
    "Five. Freedom, instability, curiosity, innovation, desire for change.",
    "Six. Sensitivity, empathy, social responsibility, desire to help others.",
    "Seven. Seclusion, intellectualism, mysticism, desire for spiritual growth.",
    "Eight. Authority, responsibility, financial sense, ambition, dominance.",
    "Nine. Sacrifice, surrender, catharsis, undoing."
]

PROFILE_KEYS = [
    ("Expression", "one's overall life purpose"),
    ("Heart", "one's desires"),
    ("Personality", "how one is perceived by others"),
    ("Destiny", "one's natural talents/gifts"),
]


class NumerologyCalculator:
    
    letters = "abcdefghijklmnopqrstuvwxyz"
    vowels = "aeiou"
    num_map = dict()
    
    def __init__(self):
        counter = 1
        for l in self.letters:
            self.num_map[l] = counter
            if counter < 9: counter += 1
            else: counter = 1
    
    def _compute_segments(self, segment_list):
        """Helper. Computes and reduces number values of strings in
        segment_list.
        """
        
        subtotals = []
        total = 0
        for substring in segment_list:
            subtotal = 0
            # Get the raw total first.
            for letter in substring:
                if letter.isdigit():
                    subtotal += int(letter)
                if letter in self.num_map:
                    subtotal += self.num_map[letter]
            # Reduce the total if it is not a master number.
            subtotals.append(self._reduce(subtotal))
        for s in subtotals:
            total += s
        return self._reduce(total)
    
    def _get_destiny(self, birthday):
        """Calculates the Destiny number."""
        
        if not birthday.replace("-", "").isdigit():
            return 0
        return self._compute_segments(birthday.split("-"))
    
    def _get_expression(self, full_name):
        """Calculates the Expression number of a given name (full_name)."""
        
        # Break the full name down into name segments.
        name = []
        segment = ""
        for letter in full_name + ".":   # We want to end with a non-alnum.
            if letter.isalnum():
                segment += letter.lower()
            else:
                name.append(segment)
                segment = ""
        return self._compute_segments(name)
    
    def _get_heart_personality(self, full_name):
        """Calculates the Heart and Personality numbers."""
        
        total_v = 0  # Vowels are for Heart.
        total_c = 0  # Consonants are for Personality.
        for letter in [x for x in full_name if x.isalpha()]:
            if letter in self.vowels:
                total_v += self.num_map[letter]
            else:
                total_c += self.num_map[letter]
        return self._reduce(total_v), self._reduce(total_c)
    
    def _reduce(self, segment):
        """Reduces a number to a single digit."""
        
        segment = str(segment)
        while len(segment) > 1:
            total = 0
            nums = list(segment)
            for n in nums:
                total += int(n)
            segment = str(total)
        return int(segment)
    
    def get_profile(self, full_name, birthday):
        """Generates the profile based on the name and birthday. @birthday must
        be in the following format: yyyy-mm-dd; otherwise, it reduces to zero.
        """
        
        full_name = full_name.lower()
        h, p = self._get_heart_personality(full_name)
        profile = {
            "expression": self._get_expression(full_name),
            "heart": h,
            "personality": p,
            "destiny": self._get_destiny(birthday),
        }
        return profile


if __name__ == "__main__":
    import sys
    
    nc = NumerologyCalculator()
    n = raw_input("Enter your name: ")
    b = raw_input("Enter your birthday (yyyy-mm-dd): ")
    profile = nc.get_profile(n, b)
    sys.stdout.write("\nYour numerological profile:\n\n")
    for i in PROFILE_KEYS:
        sys.stdout.write("%s - %s:\n    %s\n" % \
            (i[0], i[1], INTERPRETATIONS[profile[i[0].lower()]]))
    sys.exit("\nGoodbye.")

