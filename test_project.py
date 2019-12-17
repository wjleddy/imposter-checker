"""Tests for final project. Many tests adapted from
https://realpython.com/testing-in-django-part-1-best-practices-and-examples/ , 
https://www.vinta.com.br/blog/2017/how-i-test-my-drf-serializers/ and 
https://www.argpar.se/posts/programming/testing-django-admin/"""

from django.test import TestCase as DJTest
from get_handles.models import BaseHandle, SimilarHandles
from datetime import date, timedelta

# Postgres will have to set up correctly to run these tests

class BaseHandleTests(DJTest):

    def create_base_handle(self, date_pulled=date.today(), handle="test_handle"):
        return BaseHandle.objects.create(date_pulled=date_pulled, handle=handle)

    def test_base_handle_creation(self):
        w = self.create_base_handle()
        self.assertTrue(isinstance(w, BaseHandle))
        self.assertEqual(w.__str__(), w.handle)
        
    def test_field_content(self):
        w = self.create_base_handle()
        self.assertEqual(w.handle, "test_handle")
        self.assertEqual(w.date_pulled, date.today())

class SimilarHandleTests(DJTest):

    def create_similar_handles(self, b_handle= "test_handle", date_pulled=date.today(), 
                               handle="tst_handle", suspended=False, display_name="Mr. T Handle", 
                               number_of_tweets=5000, number_of_followers=7, number_following=12, 
                               date_joined = date.today() - timedelta(days=1), bio= "Cool cool cool"):
        BaseHandle.objects.create(handle=b_handle, date_pulled=date_pulled)
        bh_date = BaseHandle.objects.get(handle=b_handle, date_pulled=date_pulled)
        return SimilarHandles.objects.create(base_handle_date=bh_date, handle=handle, suspended=suspended,
                                         display_name=display_name, number_of_tweets=number_of_tweets, number_of_followers=number_of_followers,
                                         number_following=number_following, date_joined=date_joined, bio=bio)

    def test_bh_creation(self):
        w = self.create_similar_handles()
        self.assertTrue(isinstance(w, SimilarHandles))
        self.assertEqual(w.__str__(), w.handle)
    
    def test_field_content(self):
        w = self.create_similar_handles()
        self.assertEqual(w.handle, "tst_handle")
        self.assertEqual(w.suspended, False)
        self.assertEqual(w.display_name, "Mr. T Handle")
        self.assertEqual(w.number_of_tweets, 5000)
        self.assertEqual(w.number_of_followers, 7)
        self.assertEqual(w.number_following, 12)
        self.assertEqual(w.date_joined, date.today() - timedelta(days=1))
        self.assertEqual(w.bio, "Cool cool cool")
        

