"""Typing test implementation"""

from utils import lower, split, remove_punctuation, lines_from_file
from ucb import main, interact, trace
from datetime import datetime


###########
# Phase 1 #
###########


def choose(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns True. If there are fewer than K such paragraphs, return
    the empty string.

    Arguments:
        paragraphs: a list of strings
        select: a function that returns True for paragraphs that can be selected
        k: an integer

    >>> ps = ['hi', 'how are you', 'fine']
    >>> s = lambda p: len(p) <= 4
    >>> choose(ps, s, 0)
    'hi'
    >>> choose(ps, s, 1)
    'fine'
    >>> choose(ps, s, 2)
    ''
    """
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"

    valid_paragraphs = [] ##有效的段落

    for paragraph in paragraphs : ##从paragraphs中选择有效段落
        if select(paragraph):
            valid_paragraphs.append(paragraph)
    
    if k > len(valid_paragraphs) - 1:
        return str('') ##如果k大于有效段落的长度返回空字符串
    else:
        return valid_paragraphs[k] ##返回所选的段落

    # END PROBLEM 1


def about(topic):
    """Return a select function that returns whether
    a paragraph contains one of the words in TOPIC.

    Arguments:
        topic: a list of words related to a subject

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([lower(x) == x for x in topic]), 'topics should be lowercase.'
    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"
    def about_what(s):
        count = 0
        save_topic = topic
        remove_punctuation_string = remove_punctuation(s)
        lower_string = lower(remove_punctuation_string)
        split_string = split(lower_string)
        for x in split_string:
            count = count + save_topic.count(x)
        return bool(count)
    return about_what
    # END PROBLEM 2


def accuracy(typed, reference):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of REFERENCE that was typed.

    Arguments:
        typed: a string that may contain typos
        reference: a string without errors

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    >>> accuracy('', '')
    100.0
    """
    typed_words = split(typed)
    reference_words = split(reference)
    # BEGIN PROBLEM 3
    "*** YOUR CODE HERE ***"

    reference_lenth = len(reference_words)
    typed_lenth = len(typed_words)
    typed_extra = 0
    reference_extra =0
    correct = 0
    if (typed_lenth == 0) and (reference_lenth == 0):
        return 100.0
    elif (typed_lenth == 0) and (reference_lenth != 0):
        return 0.0
    elif (typed_lenth != 0) and (reference_lenth == 0):
        return 0.0

    if typed_lenth > reference_lenth:
        typed_extra = typed_lenth - reference_lenth
        del typed_words[reference_lenth:]
    elif reference_lenth > typed_lenth:
        reference_extra = reference_lenth - typed_lenth
        del reference_words[typed_lenth]

    for i in range(typed_lenth if(reference_lenth>=typed_lenth) else reference_lenth):
        if typed_words[i] == reference_words[i]:
            correct = correct + 1
    if bool(typed_extra):
        percentage = ( (correct) / (reference_lenth + typed_extra) ) * 100
    else:
        percentage = ( correct / typed_lenth ) * 100
    return percentage
    # END PROBLEM 3


def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string.

    Arguments:
        typed: an entered string
        elapsed: an amount of time in seconds

    >>> wpm('hello friend hello buddy hello', 15)
    24.0
    >>> wpm('0123456789',60)
    2.0
    """
    assert elapsed > 0, 'Elapsed time must be positive'
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    characters_lenth = len(typed)
    if characters_lenth == 0:
        return 0.0
    words_per_minute = characters_lenth / 5
    return words_per_minute * (60/elapsed)
    # END PROBLEM 4


###########
# Phase 2 #
###########

def autocorrect(typed_word, valid_words, diff_function, limit):
    """Returns the element of VALID_WORDS that has the smallest difference
    from TYPED_WORD. Instead returns TYPED_WORD if that difference is greater
    than LIMIT.

    Arguments:
        typed_word: a string representing a word that may contain typos
        valid_words: a list of strings representing valid words
        diff_function: a function quantifying the difference between two words
        limit: a number

    >>> ten_diff = lambda w1, w2, limit: 10 # Always returns 10
    >>> autocorrect("hwllo", ["butter", "hello", "potato"], ten_diff, 20)
    'butter'
    >>> first_diff = lambda w1, w2, limit: (1 if w1[0] != w2[0] else 0) # Checks for matching first char
    >>> autocorrect("tosting", ["testing", "asking", "fasting"], first_diff, 10)
    'testing'
    """
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"
    lowest_diff_index = 0
    lowest_diff = 30 
    if bool(valid_words.count(typed_word)):
        return typed_word
    for i in range(len(valid_words)):
        if diff_function(typed_word,valid_words[i],limit) < lowest_diff:
            lowest_diff = diff_function(typed_word,valid_words[i],limit)
            lowest_diff_index = i
    if lowest_diff > limit:
        return typed_word
    else:
        return valid_words[lowest_diff_index]

    # END PROBLEM 5


def sphinx_switches(start, goal, limit):
    """A diff function for autocorrect that determines how many letters
    in START need to be substituted to create GOAL, then adds the difference in
    their lengths and returns the result.

    Arguments:
        start: a starting word
        goal: a string representing a desired goal word
        limit: a number representing an upper bound on the number of chars that must change

    >>> big_limit = 10
    >>> sphinx_switches("nice", "rice", big_limit)    # Substitute: n -> r
    1
    >>> sphinx_switches("range", "rungs", big_limit)  # Substitute: a -> u, e -> s
    2
    >>> sphinx_switches("pill", "pillage", big_limit) # Don't substitute anything, length difference of 3.
    3
    >>> sphinx_switches("roses", "arose", big_limit)  # Substitute: r -> a, o -> r, s -> o, e -> s, s -> e
    5
    >>> sphinx_switches("rose", "hello", big_limit)   # Substitute: r->h, o->e, s->l, e->l, length difference of 1.
    5
    """
    # BEGIN PROBLEM 6
    '''
    if len(start) == 0 and len(goal) > 0:
        return len(goal)
    elif len(start) == 0 and len(goal) == 0:
        return 0
    elif len(start) > 0 and len(goal) ==0:
        return len(start) 
    if start[0] == goal[0]:
        diff = 0
    else:
        diff = 1
     
    total_diff = sphinx_switches(start[1:],goal[1:],limit) + diff
    if total_diff > limit:
        return 100 

    return total_diff
    '''

    '''
    def counts(cstart, cgoal, count):
        if count > limit:
            return limit + 1
        if not cstart and not cgoal:
            return count
        elif not cstart or not cgoal:
            return counts(cstart[1:], cgoal[1:], count + 1)
        elif cstart[0] == cgoal[0]:
            return counts(cstart[1:], cgoal[1:], count)
        else:
            return counts(cstart[1:], cgoal[1:], count + 1)
    return counts(start, goal, 0)
    '''
    def counts(cstart,cgoal,count): #尾递归？
        #base case
        if count > limit:
            return limit+1
        if not cstart and not cgoal:
            return count
        #cursion
        elif not cstart or not cgoal:
            return counts(cstart[1:],cgoal[1:],count+1)
        elif cstart[0] == cgoal[0]:
            return counts(cstart[1:],cgoal[1:],count)
        else:
            return counts(cstart[1:],cgoal[1:],count+1)
    return counts(start,goal,0)
    # END PROBLEM 6


def pawssible_patches(start, goal, limit):
    """A diff function that computes the edit distance from START to GOAL.
    This function takes in a string START, a string GOAL, and a number LIMIT.

    Arguments:
        start: a starting word
        goal: a goal word
        limit: a number representing an upper bound on the number of edits

    >>> big_limit = 10
    >>> pawssible_patches("cats", "scat", big_limit)       # cats -> scats -> scat
    2
    >>> pawssible_patches("purng", "purring", big_limit)   # purng -> purrng -> purring
    2
    >>> pawssible_patches("ckiteus", "kittens", big_limit) # ckiteus -> kiteus -> kitteus -> kittens
    3
    """
    #assert False, 'Remove this line'
    if limit < 0:  # Fill in the condition
        # BEGIN
        "*** YOUR CODE HERE ***"
        return 0
        # END

    if not start and not goal:
        return 0

    elif not start or not goal:
        return abs(len(start) - len(goal))

    elif start[0] == goal[0]:  # Feel free to remove or add additional cases
        # BEGIN
        "*** YOUR CODE HERE ***"
        return pawssible_patches(start[1:], goal[1:], limit)
        # END

    else:
        add = pawssible_patches(start, goal[1:], limit - 1)  # Fill in these lines
        remove = pawssible_patches(start[1:], goal, limit - 1)
        substitute = pawssible_patches(start[1:], goal[1:], limit - 1)
        # BEGIN
        "*** YOUR CODE HERE ***"
        return min(add, remove, substitute) + 1

        # END


def final_diff(start, goal, limit):
    """A diff function that takes in a string START, a string GOAL, and a number LIMIT.
    If you implement this function, it will be used."""
    assert False, 'Remove this line to use your final_diff function.'


FINAL_DIFF_LIMIT = 6  # REPLACE THIS WITH YOUR LIMIT


###########
# Phase 3 #
###########


def report_progress(typed, prompt, user_id, send):
    """Send a report of your id and progress so far to the multiplayer server.
    Returns the progress so far.

    Arguments:
        typed: a list of the words typed so far
        prompt: a list of the words in the typing prompt
        user_id: a number representing the id of the current user
        send: a function used to send progress to the multiplayer server

    >>> print_progress = lambda d: print('ID:', d['id'], 'Progress:', d['progress'])
    >>> # The above function displays progress in the format ID: __, Progress: __
    >>> print_progress({'id': 1, 'progress': 0.6})
    ID: 1 Progress: 0.6
    >>> typed = ['how', 'are', 'you']
    >>> prompt = ['how', 'are', 'you', 'doing', 'today']
    >>> report_progress(typed, prompt, 2, print_progress)
    ID: 2 Progress: 0.6
    0.6
    >>> report_progress(['how', 'aree'], prompt, 3, print_progress)
    ID: 3 Progress: 0.2
    0.2
    """
    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"
    prompt_lenth = len(prompt)
    typed_lenth = len(typed)
    correct = 0
    for i in range(min(prompt_lenth,typed_lenth)):
        if typed[i] == prompt[i]:
            correct = correct + 1
        else:
            break
    progress = correct / prompt_lenth 
    dic = {'id': user_id, 'progress': progress}
    send(dic)
    return progress
    # END PROBLEM 8


def fastest_words_report(times_per_player, words):
    """Return a text description of the fastest words typed by each player."""
    game = time_per_word(times_per_player, words)
    fastest = fastest_words(game)
    report = ''
    for i in range(len(fastest)):
        words = ','.join(fastest[i])
        report += 'Player {} typed these fastest: {}\n'.format(i + 1, words)
    return report


def time_per_word(times_per_player, words):
    """Given timing data, return a game data abstraction, which contains a list
    of words and the amount of time each player took to type each word.

    Arguments:
        times_per_player: A list of lists of timestamps including the time
                          the player started typing, followed by the time
                          the player finished typing each word.
        words: a list of words, in the order they are typed.

    >>> p = [[75, 81, 84, 90, 92], [19, 29, 35, 36, 38]]
    >>> game = time_per_word(p, ['collar', 'plush', 'blush', 'repute'])
    >>> all_words(game)
    ['collar', 'plush', 'blush', 'repute']
    >>> all_times(game)
    [[6, 3, 6, 2], [10, 6, 1, 2]]
    """
    # BEGIN PROBLEM 9
    "*** YOUR CODE HERE ***"
    timestamps = []
    for i in times_per_player:
        timestamps.append([abs(i[n]-i[n+1])for n in range(len(i)-1)])
        #print(timestamps)
    return game(words,timestamps)

    # END PROBLEM 9


def fastest_words(game):
    """Return a list of lists of which words each player typed fastest.

    Arguments:
        game: a game data abstraction as returned by time_per_word.

    >>> p0 = [5, 1, 3]
    >>> p1 = [4, 1, 6]
    >>> fastest_words(game(['Just', 'have', 'fun'], [p0, p1]))
    [['have', 'fun'], ['Just']]
    """
    player_indices = range(len(all_times(game)))  # contains an *index* for each player
    word_indices = range(len(all_words(game)))    # contains an *index* for each word
    # BEGIN PROBLEM 10
    "*** YOUR CODE HERE ***"
    fastest = [[] for _ in player_indices]
    for word_index in word_indices:
        min_time = float('inf')
        player = 0
        for player_index in player_indices:
            if time(game, player_index, word_index) < min_time:
                min_time = time(game, player_index, word_index)
                player = player_index
        fastest[player].append(word_at(game, word_index))
    return fastest
    # END PROBLEM 10


def game(words, times):
    """A data abstraction containing all words typed and their times."""
    assert all([type(w) == str for w in words]), 'words should be a list of strings'
    assert all([type(t) == list for t in times]), 'times should be a list of lists'
    assert all([isinstance(i, (int, float)) for t in times for i in t]), 'times lists should contain numbers'
    assert all([len(t) == len(words) for t in times]), 'There should be one word per time.'
    return [words, times]


def word_at(game, word_index):
    """A selector function that gets the word with index word_index"""
    assert 0 <= word_index < len(game[0]), "word_index out of range of words"
    return game[0][word_index]


def all_words(game):
    """A selector function for all the words in the game"""
    return game[0]


def all_times(game):
    """A selector function for all typing times for all players"""
    return game[1]


def time(game, player_num, word_index):
    """A selector function for the time it took player_num to type the word at word_index"""
    assert word_index < len(game[0]), "word_index out of range of words"
    assert player_num < len(game[1]), "player_num out of range of players"
    return game[1][player_num][word_index]


def game_string(game):
    """A helper function that takes in a game object and returns a string representation of it"""
    return "game(%s, %s)" % (game[0], game[1])


enable_multiplayer = False  # Change to True when you're ready to race.

##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file('data/sample_paragraphs.txt')
    select = lambda p: True
    if topics:
        select = about(topics)
    i = 0
    while True:
        reference = choose(paragraphs, select, i)
        if not reference:
            print('No more paragraphs about', topics, 'are available.')
            return
        print('Type the following paragraph and then press enter/return.')
        print('If you only type part of it, you will be scored only on that part.\n')
        print(reference)
        print()

        start = datetime.now()
        typed = input()
        if not typed:
            print('Goodbye.')
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print('Words per minute:', wpm(typed, elapsed))
        print('Accuracy:        ', accuracy(typed, reference))

        print('\nPress enter/return for the next paragraph or type q to quit.')
        if input().strip() == 'q':
            return
        i += 1


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument('topic', help="Topic word", nargs='*')
    parser.add_argument('-t', help="Run typing test", action='store_true')

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)
