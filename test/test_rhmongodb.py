import unittest
from bson.objectid import ObjectId
from rh_mongodb import RHMongoDB  # le fichier où tu as mis la classe

class TestRHMongoDB(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rh = RHMongoDB()
        # Préparer un employé test
        cls.test_employee = {
            "first_name": "Test",
            "last_name": "User",
            "email": "test.user@example.com",
            "salary": 3000,
            "department_id": ObjectId(),
            "position": "Testeur",
            "on_leave": False
        }
        # Insert employee test (avant tests)
        cls.inserted_id = cls.rh.insert_new_employee(cls.test_employee)

    @classmethod
    def tearDownClass(cls):
        # Supprimer l'employé test (après tests)
        cls.rh.delete_employee(cls.test_employee["email"])

    def test_find_all_employees_contains_test_user(self):
        emps = self.rh.find_all_employees()
        emails = [emp["email"] for emp in emps]
        self.assertIn(self.test_employee["email"], emails)

    def test_update_employee_salary(self):
        new_salary = 3500
        modified_count = self.rh.update_employee_salary(self.test_employee["email"], new_salary)
        self.assertEqual(modified_count, 1)

        # Vérifier mise à jour effective
        emp = self.rh.employees.find_one({"email": self.test_employee["email"]})
        self.assertEqual(emp["salary"], new_salary)

    def test_find_employee_by_name(self):
        results = self.rh.find_employee_by_name("Test")
        self.assertTrue(any(emp["email"] == self.test_employee["email"] for emp in results))

    def test_delete_employee(self):
        # Création temporaire
        email = "temp.user@example.com"
        emp = self.test_employee.copy()
        emp["email"] = email
        emp_id = self.rh.insert_new_employee(emp)

        deleted_count = self.rh.delete_employee(email)
        self.assertEqual(deleted_count, 1)

        # Vérifier suppression
        emp_after = self.rh.employees.find_one({"email": email})
        self.assertIsNone(emp_after)

if __name__ == "__main__":
    unittest.main()
