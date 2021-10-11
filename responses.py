import random
import re


def process_message(message, response_array, response):
    # Splits the message and the punctuation into an array
    list_message = re.findall(r"[\w']+|[.,!?;]", message.lower())

    # Scores the amount of words in the message
    score = 0
    for word in list_message:
        if word in response_array:
            score = score + 1

    # Returns the response and the score of the response
    # print(score, response)
    return [score, response]


def get_response(message):
    # Add your custom responses here
    response_list = [
        process_message(message, ['hello', 'hi', 'hey','hai'],    random.choice(['HI!','Hello','Whatsup','Hehe','Hloo'])),
        process_message(message, ['bye', 'goodbye'],        random.choice(['Goodbye!'])),
        process_message(message, ['how', 'are', 'you'],     random.choice(['Sugham ','Fine , ninko?'])),
        process_message(message, ['your', 'name'],          random.choice(['My name is Devu, nice to meet you!'])),
        process_message(message, ['help', 'me'],            random.choice(['I will do my best to assist you!'])),
        process_message(message, ['hmm', 'mm'], random.choice(['pinne','vere entha ppd?'])),
        process_message(message, ['entha'], random.choice(['enth?','entha'])),
        process_message(message, ['enth'], random.choice(['onnula'])),
        #process_message(message, ['bye', 'goodbye'], random.choice(['Goodbye!'])),
        #process_message(message, ['bye', 'goodbye'], random.choice(['Goodbye!'])),
        #process_message(message, ['bye', 'goodbye'], random.choice(['Goodbye!'])),
        #process_message(message, ['bye', 'goodbye'], random.choice(['Goodbye!'])),
        #process_message(message, ['bye', 'goodbye'], random.choice(['Goodbye!'])),
        #process_message(message, ['bye', 'goodbye'], random.choice(['Goodbye!'])),
        #process_message(message, ['bye', 'goodbye'], random.choice(['Goodbye!'])),
        #process_message(message, ['bye', 'goodbye'], random.choice(['Goodbye!'])),
        #process_message(message, ['bye', 'goodbye'], random.choice(['Goodbye!'])),
        #process_message(message, ['bye', 'goodbye'], random.choice(['Goodbye!'])),
        #process_message(message, ['bye', 'goodbye'], random.choice(['Goodbye!'])),
        #
    ]

    # Checks all of the response scores and returns the best matching response
    response_scores = []
    for response in response_list:
        response_scores.append(response[0])

    # Get the max value for the best response and store it into a variable
    winning_response = max(response_scores)
    matching_response = response_list[response_scores.index(winning_response)]

    # Return the matching response to the user
    if winning_response == 0:
        bot_response = 'I didn\'t understand what you wrote.'
        trainingdata = open("training.txt", "a")
        questions = [message,"\n"]
        trainingdata.writelines(questions)
        trainingdata.close()
    else:
        bot_response = matching_response[1]

    print('Bot response:', bot_response)
    return bot_response



