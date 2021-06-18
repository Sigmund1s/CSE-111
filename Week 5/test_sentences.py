from sentences import get_determiner, get_noun, get_preposition, get_prepositional_phrase, get_verb
import pytest


# GET HELP TO UNDERSTAND THESE LINES OF CODE

def test_get_determiner():
    # Test the singular determiners.
    
    singular_determiner = ["the", "one", "a"]
    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):
        word = get_determiner(1)

        # Verify that the word returned from get_determiner is
        # one of the words in the singular_determiners list.
        assert word in singular_determiner
        

    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.

    # Test the plural determiners.
    plural_determiners = ["some", "many", "two"]
    for _ in range(4):
        word = get_determiner(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners

def test_get_noun():
    singular_noun = ["adult", "bird", "boy", "car", "cat",
        "child", "dog", "girl", "man", "woman"]
    
    for _ in range(10):
        noun = get_noun(1)

        assert noun in singular_noun
    
    plural_noun = ["adults", "birds", "boys", "cars", "cats",
        "children", "dogs", "girls", "men", "women"]
    
    for _ in range(10):
        noun = get_noun(2)

        assert noun in plural_noun

def test_get_verb():
    tense_past = ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]
    for _ in range(10):
        verb = get_verb(2, "past")
    assert verb in tense_past

    tense_present_q_1 = ["drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]
    for _ in range(10):
        verb = get_verb(1, "present")
    assert verb in tense_present_q_1

    tense_present_q_2 = ["drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]
    for _ in range(10):
        verb = get_verb(2, "present")
    assert verb in tense_present_q_2

    tense_future = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]
    for _ in range(10):
        verb = get_verb(1,"future")
    assert verb in tense_future


# NEWLY ADDED
def test_get_preposition():
    prep = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    for _ in range(4):
        preps = get_preposition()
    assert preps in prep


def test_get_prepositional_phrase():
    phrase = get_prepositional_phrase(1)
    
    list_of_words = phrase.split() # ["above", "one", "cat"]

    prep = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    determiners = ["the", "a", "one", "two", "some", "many"]
    nouns = ["adult", "bird", "boy", "car", "cat",
        "child", "dog", "girl", "man", "woman", "adults", "birds", "boys", "cars", "cats",
        "children", "dogs", "girls", "men", "women"]

    assert list_of_words[0] in prep and list_of_words[1] in determiners and list_of_words[2] in nouns


    # for _ in range(4):
    #     preps = get_prepositional_phrase()
    

# Call the main function that is part of pytest so that
# the test functions in this file will start executing.
pytest.main(["-v", "--tb=line", "-rN", "test_sentences.py"])
