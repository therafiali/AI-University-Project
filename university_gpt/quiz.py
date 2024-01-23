from abc import ABC, abstractmethod
from university_gpt.user import Student
from university_gpt.topic import Question, Option, SingleSelectMCQ, MultipleSelectMCQ, CaseStudy


class Quiz:
    def __init__(self, quizID:str, student: Student, subpath: str, quizTitle:str) -> None:
        self.quizID:str = quizID
        self.student: Student = student
        self.subpath: str = subpath
        self.quizTitle : str = quizTitle
        self.quizTopics: list[QuizTopic]= []


class QuizTopic:
    def __init__(self, quizID: str, topicID:str) -> None:
        self.quizID = quizID
        self.topicID: str = topicID
        self.subtopics : list[QuizTopic] = []
        self.questions : list[Question] = []

class QuizAnswerSheet:
    def __init__(self, answerSheetID: str, quiz: Quiz) -> None:
       self.answerSheetID = answerSheetID 
       self.quiz = quiz
       self.answer : list[Answer] = []



class Answer(ABC):
    def __init__(self,answerSheetID: str, answerID: str, pointsReceived: float = 0) -> None:
        self.answerSheetID = answerSheetID
        self.answerID = answerID
        self.pointsReceived: float = pointsReceived

    @abstractmethod
    def checkAnswer(self):
        pass

    @abstractmethod
    def getQuestion(self)-> Question:
        pass

class SingleSelectAnswer(Answer):
    def __init__(self,answerSheetID: str, answerID: str, question: SingleSelectMCQ, selectedOption: Option) -> None:
        super().__init__(answerSheetID, answerID)
        self.question: SingleSelectMCQ = question
        self.selectedOption: Option = selectedOption

    def getQuestion(self):
        return self.question

    def checkAnswer(self):
        for option in self.question.getOptions(): 
            if self.selectedOption.optionID == option.optionID:
                self.pointsReceived = self.question.getPoints()
                break


class CaseStudyAnswer(Answer):
    def __init__(self,answerSheetID: str, answerID: str, question: CaseStudy) -> None:
        super().__init__(answerSheetID, answerID)
        self.question: CaseStudy = question

    def getQuestion(self):
        return self.question

    def checkAnswer(self):
        pass
            
class FreeTextAnswer(Answer):
    pass

class CodeAnswer(Answer):
    pass