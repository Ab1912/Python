# Instance attribute

class study():
    subject = "English"

new = study()
print(study.__dict__)
print(study.subject)
print(new.__dict__)
print(new.subject)
new.subject = "Tamil"
print(new.__dict__)
print(new.subject)

new2 = study()
print(new2.subject)