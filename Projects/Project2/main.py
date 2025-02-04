# Define a class named 'students' to represent student records
class students:
    def __init__(self, first, last):
        # Initialize the student's first and last name
        self.first = first
        self.last = last
        # Create an empty list to store the student's grades
        self.grades = []
    
    def gInput(self, ng):
        # Loop 'ng' times to input grades
        for i in range(ng):
            # Prompt the user to enter a grade, ensuring it's stored as a float
            grade = float(input(f"Enter grade {i + 1} for {self.first} {self.last}: "))
            # Append the grade to the student's list of grades
            self.grades.append(grade)
    
    def printGrades(self):
        # Print the student's name followed by their grades
        print(f"{self.first} {self.last}'s Grades are:")
        # Iterate through the list of grades and print each one
        for grade in self.grades:
            print(grade)
    
    def avGrades(self):
        # Check if the student has grades before calculating the average
        if self.grades:
            # Compute the average by summing the grades and dividing by the number of grades
            return sum(self.grades) / len(self.grades)
        # Return 0.0 if no grades are present
        return 0.0
    
    def highLow(self):
        # Check if the student has grades before finding high/low values
        if self.grades:
            # Use max() to get the highest grade and min() to get the lowest grade
            return max(self.grades), min(self.grades)
        # Return None if no grades are present
        return None, None

# Main Program
# Create a student object named 'student1' with first name 'Joe' and last name 'Evans'
student1 = students("Joe", "Evans")

# Input grades for student1 (user enters 4 grades)
student1.gInput(4)

# Print grades for student1
student1.printGrades()

# Calculate and display statistics for student1
average = student1.avGrades()  # Compute average grade
high, low = student1.highLow() # Find highest and lowest grades

# Print the computed statistics
print(f"{student1.first} has an average of {average:.2f}")
print(f"{student1.first} has a high grade of {high}")
print(f"{student1.first} has a low grade of {low}")

# Create a second student object named 'student2' with first name 'Shirley' and last name 'Baker'
student2 = students("Shirley", "Baker")

# Input grades for student2 (user enters 4 grades)
student2.gInput(4)

# Print grades for student2
student2.printGrades()

# Calculate and display statistics for student2
average = student2.avGrades()
high, low = student2.highLow()

# Print the computed statistics for student2
print(f"{student2.first} has an average of {average:.2f}")
print(f"{student2.first} has a high grade of {high}")
print(f"{student2.first} has a low grade of {low}")