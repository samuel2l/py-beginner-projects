import html
class QuizBrain:

    def __init__(self,qu_list):
        self.qu_number=0
        self.qu_list=qu_list

    def next_qu(self):
        sum = 0
        attempts = 0
        while self.qu_number<len(self.qu_list):

            x=input(f"Q{self.qu_number +1}: {html.unescape(self.qu_list[self.qu_number].qu)}(True/False)").capitalize()

            if x=='True':
                sum+=1
                print("You are right")
            else:
                print("wrong choice")
            attempts += 1
            print(f"Score: {sum}/{attempts}")


            self.qu_number+=1
