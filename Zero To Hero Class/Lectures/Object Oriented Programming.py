#Question: There are 5 people in a room. 4 people leave, and 4 come in. Half of the people who left come back. If a woman comes into the room, then one person will be asked to leave. 
# If a man comes into the room, no one will leave. How many people will be in the room if: a: a woman comes b. a man comes in

#Solution
class room:
    def __init__(self,people,people_left,people_came_in,gender):
        self.people = people
        self.people_left = people_left
        self.people_came_in = people_came_in
        self.gender = gender

    def logic_people(self):
       # self.people = 5
        self.people_left = 0.5 * self.people_left #Halve the people who left

        if self.people <= 5:
            people_left_remain = self.people - self.people_left  #Remaining people who stayed after some left
            
            if people_left_remain <= 5:
                people_came_in = self.people_came_in + people_left_remain  #More people came in
                return people_came_in

class gender(room):
    def gender_logic(self):
        if self.gender == "woman":  #Check if the gender is woman or not
            woman_came_in_people_left = super().logic_people()
            woman_came_in_people_left_remaining = round((woman_came_in_people_left + 1) - 1)
            return f"a woman comes in, people remaining are: {woman_came_in_people_left_remaining}"

        if self.gender == "man":   #Check if the gender is man or not
            man_came_in_people_left = super().logic_people()
            people_remaining = round(man_came_in_people_left + 1)
            return f"a man comes in, people remaining are: {people_remaining}"

woman_checker = room(5,4,4,"woman")
man_checker = room(5,4,4,"man")

gender_checker_woman = gender(5,4,4,"woman")
gender_checker_man = gender(5,4,4,"man")

print(gender_checker_woman.gender_logic())
print(gender_checker_man.gender_logic())