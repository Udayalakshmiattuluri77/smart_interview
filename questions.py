from data import questions


def get_topics():

    return list(questions.keys())


def get_questions(topic):

    return questions.get(topic, [])