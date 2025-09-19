from django.test import TestCase
from .models import Question


class QuestionModelTest(TestCase):
	def test_create_question(self):
		q = Question.objects.create(
			category="HTML",
			text="What does HTML stand for?",
			option1="Hyper Text Markup Language",
			option2="High Text Markup Language",
			option3="Hyperlinks and Text Markup Language",
			option4="",
			answer="Hyper Text Markup Language",
		)
		self.assertIsNotNone(q.id)
		self.assertEqual(q.category, "HTML")
		self.assertIn("HTML", str(q))
