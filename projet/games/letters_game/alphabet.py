import numpy as np


def random_draft(n):
    alphabet = {'A': .095, 'N': .05,
                'B': .015, 'O': .07,
                'C': .03, 'P': .03,
                'D': .0225, 'Q': .01,
                'E': .18, 'R': .0625,
                'F': .0125, 'S': .075,
                'G': .015, 'T': .05,
                'H': .015, 'U': .06,
                'I': .08525, 'V': .0125,
                'J': .005, 'W': .0025,
                'K': .005, 'X': .0075,
                'L': .045, 'Y': .0030,
                'M': .03, 'Z': .005}

    probabilities = list(alphabet.values())
    # standardisation
    probabilities = np.array(probabilities)
    probabilities /= probabilities.sum()
    keys = list(alphabet.keys())

    vowels = "AEIOUY"
    n_vowels, n_consonant = 0, 0
    draft = []
    while len(draft) < n:
        letter = keys[np.random.choice(26, p=probabilities)]

        if draft.count(letter) >= 2:
            continue
        elif letter in vowels:
            if 1 + n_vowels - n_consonant > 2:
                continue
            else:
                n_vowels += 1
        else:
            if n_consonant - n_vowels - 1 > 2:
                continue
            else:
                n_consonant += 1

        draft.append(letter)

    return ''.join(draft)
