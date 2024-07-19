class SchoolJournal:
    def __init__ (self, subject, student):
        self.subject = subject
        self.student = student
        self.grade_list = []
    def grade(self, n):
        if n>=1 and n<=5:
            self.grade_list.append(n)
        else:
            pass
    def printer(self):
        print(f'Subject: {self.subject}')
        print(f'Name: {self.student}')
        print(f'Grages: {self.grade_list}')
    def  final_grade(self):
        sr = 0
        for i in range(0, len(self.grade_list), 1):
            sr += self.grade_list[i]
        print(f'Final grage: {sr/len(self.grade_list)}')

st =  SchoolJournal('astr', 'ser way')
st.grade(3)
st.grade(3)
st.grade(5)
st.grade(4)
st.grade(7)
st.printer()
st.final_grade()