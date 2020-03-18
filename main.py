# TODO: 삶의 목적을 추측하는 알고리즘 만들기.

purposes_of_life = []
habits_of_my_life = []

# SET
def add_a_purpose_of_life(purpose='do nothing', verb_or_adjective = 'v'):
    item_purpose = {}
    if verb_or_adjective == 'v':
        item_purpose['verb_or_adjective'] = 'v'
    elif verb_or_adjective == 'a':
        item_purpose['verb_or_adjective'] = 'a'
    else:
        print('### The purpose is something wrong. ###')
        return
    item_purpose['purpose'] = purpose
    purposes_of_life.append(item_purpose)

def add_habit_of_my_life(habit='do nothing'):
    habits_of_my_life.append(habit)

# GET
def why_do_you_live():
    print('Why do you live?')
    for number in range(len(purposes_of_life)):
        if purposes_of_life[number]['verb_or_adjective'] == 'v':
            print('> I live to %s.' % (purposes_of_life[number]['purpose']))
        elif purposes_of_life[number]['verb_or_adjective'] == 'a':
            print('> I live for %s.' % (purposes_of_life[number]['purpose']))

def what_is_your_name(name):
    print('What is your name?')
    print('> My name is %s.' % (name))

def what_are_your_habits():
    print('What are your habits?')

    print('> My habits are %s.' % (habits_of_my_life))

def main():
    name = 'MS'
    what_is_your_name(name)

    add_a_purpose_of_life()
    add_a_purpose_of_life('play')
    add_a_purpose_of_life('fun')
    add_a_purpose_of_life('work')
    add_a_purpose_of_life('happiness', verb_or_adjective = 'a')

    add_habit_of_my_life('playing piano')
    add_habit_of_my_life('playing tennis')
    add_habit_of_my_life('watching youtube')

    why_do_you_live()
    what_are_your_habits()

if __name__ == "__main__":
    main()
