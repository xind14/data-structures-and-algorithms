import pytest
from code_challenges.hashtable_left_join import left_join


def test_exists():
    assert left_join


def test_example():
    synonyms = {
        "diligent": "employed",
        "fond": "enamored",
        "guide": "usher",
        "outfit": "garb",
        "wrath": "anger",
    }
    antonyms = {
        "diligent": "idle",
        "fond": "averse",
        "guide": "follow",
        "flow": "jam",
        "wrath": "delight",
    }

    expected = [
        ["diligent", "employed", "idle"],
        ["fond", "enamored", "averse"],
        ["guide", "usher", "follow"],
        ["outfit", "garb", "None"],
        ["wrath", "anger", "delight"],
    ]
    
    actual = left_join(synonyms, antonyms)
    
    assert sorted(actual) == sorted(expected)


def test_empty_hashmaps():
    synonyms = {}
    antonyms = {}

    expected = []

    actual = left_join(synonyms, antonyms)

    assert actual == expected


def test_different_keys():
    synonyms = {
        "happy": "joyful",
        "sad": "unhappy",
        "angry": "irate",
    }
    antonyms = {
        "happy": "sad",
        "angry": "calm",
    }

    expected = [
        ["happy", "joyful", "sad"],
        ["sad", "unhappy", "None"],
        ["angry", "irate", "calm"],
    ]

    actual = left_join(synonyms, antonyms)

    assert sorted(actual) == sorted(expected)
