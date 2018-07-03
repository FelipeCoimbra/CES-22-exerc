'''
    Composite: Structural pattern. Keep structures of objects from the same
    type as the self object to naturally create a tree-like chaining of objects
'''
class Job:

    def __init__(self, name, difficulty, subseq=None):
        self.__name = name
        self.__difficulty = difficulty
        self.subseq = subseq
        if self.subseq is None:
            self.subseq = []

    def add_subsequent(self, job):
        self.subseq.append(job)

    def add_subsequents(self,jobs):
        self.subseq.append(jobs)

    def execute(self):
        print("Executing",self.__name)
        for subsequent_job in self.subseq:
            subsequent_job.execute()

start_job = Job("Eat", 6, [Job("Clean table", 4), Job("Wash dishes", 5)])
semifinal_job = Job("Go upstairs", 5)
semifinal_job.add_subsequents([Job("Brush my teeth", 5), Job("Go to bed", 10)])

start_job.execute()
