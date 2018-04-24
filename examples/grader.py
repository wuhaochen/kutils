import kutils
import random


# Implement your own question class following instructions in
# each function.
class SumQuestion(kutils.KQuestion):

    # Used to identify your class.
    # DO NOT CHANGE
    _name = 'Sum Question'


    # Initializer. The specification of the problem should
    # be initilized here.
    def __init__(self, data=None):
        self.first, self.second = data
        self.parser = kutils.IntegerParser()


    # Factory static method.
    # Generate a random object of this class with the parameters.
    @staticmethod
    def generate_question(**gen_args):
        first = random.randrange(10)
        second = random.randrange(10)
        return SumQuestion((first, second))


    # Specify how to format your question in Kodethon.
    # Return a string that will be used to show your question.
    @property
    def description(self):
        return ('What is the anwser of %d + %d ?' %
                (self.first, self.second))


    # Solve the question of this object.
    @property
    def solution(self):
        return self.first + self.second


    # Grade student's submission.
    # The submission is a raw string if your class doesn't have
    # a parser or the format from the parser's output.
    # It should return a kutils.score_map including score,
    # maximum score and comments for the submission.
    def score_submission(self, submission, max_score=10):
        if submission == self.solution:
            return kutils.score_map(10, comment='Correct!')
        else:
            return kutils.score_map(0, comment='Wrong!')


    ### ADDITIONAL EXTRA CHOICE. ###
    
    # Parse the raw submission from student submission to data
    # format match the solution.
    # kutils provides a few common ones that can be chosen from.
    # if you want to use those, set self.parser = KParser()
    # in the __init__ function.
    # of you can define your own parser below.

    # @staticmethod
    # def parser(raw_submission):
    

    # The dumps and loads are a pair of function to serialize
    # your object.
    # The Default option implemented in the base class uses pickle,
    # but it may not work with complicated class.

    # dumps function should return a portable string that can
    # be safely stored in json.

    # def dumps(self):
    #     return pickle.loads(codecs.decode(data.encode(), "base64"))


    # loads function should reconstrct the object from a string
    # generated by dumps function.

    # @staticmethod
    # def loads(data):
    #     return FunctionQuestion(mapping)
