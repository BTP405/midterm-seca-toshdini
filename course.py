"""This module defines a Course class for managing educational courses."""

class Course:
    """Represents a course offered by an educational institution.

    Attributes:
        course_name (str): The name of the course.
        instructor (str): The name of the instructor teaching the course.
        sections (int): The number of sections available for the course (default is 1).
        prerequisites (list): List of prerequisite courses for the course (default is None).
        enrolled_students (list): List of students enrolled in the course.
        waitlisted_students (list): List of students waitlisted for the course.
        assessments (list): List of assessments (e.g., exams, quizzes) for the course.
    """

    def __init__(self, course_name, instructor, sections=1, prerequisites=None):
        """Initialize a Course object.

        Args:
            course_name (str): The name of the course.
            instructor (str): The name of the instructor teaching the course.
            sections (int, optional): The number of sections available for the course (default is 1).
            prerequisites (list, optional): List of prerequisite courses for the course (default is None).
        """
        self.course_name = course_name
        self.instructor = instructor
        self.sections = sections
        self.prerequisites = prerequisites
        self.enrolled_students = []
        self.waitlisted_students = []
        self.assessments = []


    def add_student(self, student):
        """Enroll a student in the course or add them to the waitlist if all sections are full.

        Args:
            student (Student): The student object to be enrolled or added to the waitlist.
        """
        self.enrolled_students.append(student)


    def remove_student(self, student):
        """Remove a student from the course or the waitlist.

        Args:
            student (Student): The student object to be removed from the course or waitlist.
        """
        if student in self.enrolled_students:
            self.enrolled_students.remove(student)
        elif student in self.waitlisted_students:
            self.waitlisted_students.remove(student)

    def add_instructor(self, instructor):
        """Assign an instructor to the course.

        Args:
            instructor (str): The name of the instructor to be assigned to the course.
        """
        self.instructor = instructor

    def add_assessment(self, assessment):
        """Add an assessment to the course.

        Args:
            assessment (str): The description of the assessment to be added.
        """
        self.assessments.append(assessment)

