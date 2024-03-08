import unittest
from assessment import Assessment
from course import Course
from instructor import Instructor
from student import Student

class TestCourseManagementSystem(unittest.TestCase):

    def setUp(self):
        # Create instructors
        self.instructor1 = Instructor("John Doe", "001")
        self.instructor2 = Instructor("Jane Smith", "002")

        # Create courses
        self.course1 = Course("Mathematics", self.instructor1, sections=2, prerequisites=[])
        self.course2 = Course("Physics", self.instructor2, sections=1, prerequisites=[self.course1])

        # Create students
        self.student1 = Student("Alice", "S001")
        self.student2 = Student("Bob", "S002")

        # Enroll students in courses
        self.student1.enroll_course(self.course1)
        self.student2.enroll_course(self.course1)
        self.student2.enroll_course(self.course2)

        # Create assessments
        self.assignment1 = Assessment("Assignment 1")
        self.exam1 = Assessment("Midterm Exam")

        # Add assessments to courses
        self.course1.add_assessment(self.assignment1)
        self.course1.add_assessment(self.exam1)

    def test_enroll_student(self): # 4 marks
        self.assertIn(self.student1, self.course1.enrolled_students)
        self.assertIn(self.student2, self.course1.enrolled_students)
        self.assertIn(self.student2, self.course2.enrolled_students)

    def test_drop_student(self): # 4 marks
        self.student1.drop_course(self.course1)
        self.assertNotIn(self.student1, self.course1.enrolled_students)
        self.student2.drop_course(self.course2)
        self.assertNotIn(self.student2, self.course2.enrolled_students)

    def test_submit_grade(self): # 6 marks
        self.student1.submit_grade(self.course1, self.assignment1, 90)
        self.assertEqual(self.student1.grades[self.course1.course_name][self.assignment1.assessment_type], 90)
        self.student2.submit_grade(self.course1, self.assignment1, 85)
        self.assertEqual(self.student2.grades[self.course1.course_name][self.assignment1.assessment_type], 85)
        self.student2.submit_grade(self.course1, self.exam1, 75)
        self.assertEqual(self.student2.grades[self.course1.course_name][self.exam1.assessment_type], 75)

if __name__ == '__main__':
    unittest.main()
