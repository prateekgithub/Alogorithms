#!/usr/bin/env python


def search4vowels(word: str) -> set:
    """Return any vowel found in supplied word."""
    vowels = set('aeiou')
    return vowels.intersection(set(word))
