class PaperBoy:
    """ This class defines a PaperBoy """

    def __init__(self, name):
        self.name = name
        self.experience = 0
        self.earnings = 0
    
    def __str__(self):
        return f"Paperboy: {self.name}\nPapers Delivered: {self.experience}\nMoney earned: {self.earnings}\n"

    def quota(self):
        return 50 + int((self.experience / 2))
    
    def deliver(self, start_address, end_address):
        papers_delivered = end_address - start_address
        quota_num = self.quota()
        over_quota = papers_delivered - quota_num

        self.experience += papers_delivered

        if over_quota > 0:
            self.earnings += over_quota * 0.50 + quota_num * 0.25
        else:
            self.earnings += papers_delivered * 0.25

        if papers_delivered < quota_num:
            self.earnings -= 2

        self.quota()
    
    def report(self):
        return f"I'm {self.name}! I've delivered {self.experience} papers and I've earned ${self.earnings} so far!"


tommy = PaperBoy("Tommy")

tommy.deliver(1, 51)

print(tommy.report())

tommy.deliver(3, 43)

print(tommy.report())

tommy.deliver(1, 58)

print(tommy.report())

tommy.deliver(1, 4000)

print(tommy.report())