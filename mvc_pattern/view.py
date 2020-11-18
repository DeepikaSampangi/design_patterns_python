from .controller import personController

class personView:
    def start_view(self):
        user_response:str = input("Hello there, Do you want to view all the names in DB (y/n)?")
        if user_response == "y":
            print(personController().getAllNames())
        else:
            self.end_view()

    def end_view(self):
        print("Thank you !")

if __name__ == '__main__':
    personView().start_view()
    