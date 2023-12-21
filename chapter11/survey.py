class AnonymousSurvey:
    """collect anonymous answers to a survey question."""
    def __init__(self , question):
        """store a question and prepare to store responses"""
        self.question=question
        self.responses=[]
    def show_question(self):
        print(self.question)
    def store_response(self, new_response):
        self.responses.append(new_response)
    def show_results(self):
        print("survey results:")
        for response in self.responses:
            print(f" - {response}")