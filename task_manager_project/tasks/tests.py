from django.test import TestCase
from django.contrib.auth.models import User

from .models import Category
from .models import Task
from .models import Detail

class TaskManagerTest(TestCase):
    def setUpTestData():
        # create a user
        test_user1 = User.objects.create_user(
            username='testuser1', password='testpassword1'
        )
        test_user1.save()
        # create a category
        test_category1 = Category.objects.create(
            author=test_user1, title='Test Category 1', color='red'
        )
        test_category1.save()
        # create a task
        test_task1 = Task.objects.create(
            category=test_category1, title='Test Task 1', completed=False
        )
        test_task1.save()
        # create task details
        test_task_detail1 = Detail.objects.create(
            task=test_task1, body='Test Task 1, Detail 1 Body', completed=False
        )
        test_task_detail2 = Detail.objects.create(
            task=test_task1, body='Test Task 1, Detail 2 Body', completed=False
        )
        test_task_detail1.save()
        test_task_detail2.save()
     

    def test_task_content(self):
        # test user and category 1
        category1 = Category.objects.get(id=1)
        self.assertEqual(f'{category1.author}', 'testuser1')
        self.assertEqual(category1.title, 'Test Category 1')
        self.assertEqual(category1.color, 'red')

        # test task1
        task1 = Task.objects.get(id=1)
        self.assertEqual(task1.category, category1)
        self.assertEqual(task1.title, 'Test Task 1')
        self.assertEqual(task1.completed, False)

        # test detail 1
        detail1 = Detail.objects.get(id=1)
        self.assertEqual(detail1.task, task1)
        self.assertEqual(detail1.body, 'Test Task 1, Detail 1 Body')
        self.assertEqual(detail1.completed, False)

        # test detail 2
        detail2 = Detail.objects.get(id=2)
        self.assertEqual(detail2.task, task1)
        self.assertEqual(detail2.body, 'Test Task 1, Detail 2 Body')
        self.assertEqual(detail2.completed, False)



