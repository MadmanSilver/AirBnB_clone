#!/usr/bin/python3
""" slkjohfgosh """
import os
import time as t
import unittest
import datetime
from models.review import Review
from models import storage


class TestReview(unittest.TestCase):
    """  lkjsdfhalskhf """
    def test_attributes(self):
        """ ksajhfdg """
        subject = Review()
        self.assertTrue(hasattr(subject, "place_id"))
        if hasattr(subject, "place_id"):
            self.assertIsInstance(subject.place_id, str)
        self.assertTrue(hasattr(subject, "user_id"))
        if hasattr(subject, "user_id"):
            self.assertIsInstance(subject.user_id, str)
        self.assertTrue(hasattr(subject, "text"))
        if hasattr(subject, "text"):
            self.assertIsInstance(subject.text, str)

    def test_init_blank(self):
        """  sakujjhdfkasjdhf """
        # test blank
        time1 = datetime.datetime.now()
        subject = Review()
        time2 = datetime.datetime.now()

        # test blank id
        self.assertIsInstance(subject.id, str)
        self.assertTrue(len(subject.id) > 0)

        # test blank created_at
        self.assertIsInstance(subject.created_at, datetime.datetime)
        self.assertLessEqual(subject.created_at, time2)
        self.assertGreaterEqual(subject.created_at, time1)

        # test blank updated_at
        self.assertIsInstance(subject.updated_at, datetime.datetime)
        self.assertLessEqual(subject.updated_at, time2)
        self.assertGreaterEqual(subject.updated_at, time1)

        # check added to storage
        self.assertTrue('Review.' + subject.id in storage.all().keys())
        del subject

    def test_init_dict(self):
        """ wlkfhf """
        # test dict
        diction = {'updated_at\
': datetime.datetime(2020, 6, 27, 22, 9, 38, 171921).isoformat('T'), 'id\
': 'b3857b62-93fa-4bbe-97de-660506f7313b', 'created_at\
': datetime.datetime(2020, 6, 27, 22, 9, 38, 171827).isoformat('T')}
        subject = Review(**diction)

        # test dict id
        self.assertIsInstance(subject.id, str)
        self.assertTrue(len(subject.id) > 0)
        self.assertTrue(subject.id == diction['id'])

        # test dict created_at
        self.assertIsInstance(subject.created_at, datetime.datetime)
        self.assertEqual(subject.created_at.isoformat('T'), diction['\
created_at'])

        # test dict updated_at
        self.assertIsInstance(subject.updated_at, datetime.datetime)
        self.assertEqual(subject.updated_at.isoformat('T'), diction['\
updated_at'])
        del subject

    def test_init_break(self):
        """ skjdfh """
        # test dict empty
        diction = {}
        subject = Review(**diction)
        self.assertTrue('Review.' + subject.id in storage.all().keys())

        # test args
        arr = ['kasjfgklsd', 'ikaugsfkj']
        subject = Review(*arr)
        self.assertTrue('Review.' + subject.id in storage.all().keys())

        # test invalid time
        diction = {'updated_at\
': datetime.datetime(2020, 6, 27, 22, 9, 38, 171921), 'id\
': 'b3857b62-93fa-4bbe-97de-660506f7313b', 'created_at\
': datetime.datetime(2020, 6, 27, 22, 9, 38, 171827)}
        self.assertRaises(Exception, Review, **diction)
        del subject

    def test_str(self):
        """ ksajdfhb """
        # test output
        diction = {'updated_at\
': datetime.datetime(2020, 6, 27, 22, 9, 38, 171921).isoformat('T'), 'id\
': 'b3857b62-93fa-4bbe-97de-660506f7313b', 'created_at\
': datetime.datetime(2020, 6, 27, 22, 9, 38, 171827).isoformat('T')}
        subject = Review(**diction)
        self.assertEqual(str(subject)[:50], "[Review] \
(b3857b62-93fa-4bbe-97de-660506f7313b) {'")
        del subject

    def test_save(self):
        """ s,jdfb """
        # test save
        time4 = datetime.datetime.now()
        subject = Review()
        time3 = datetime.datetime.now()
        json = ""
        if os.path.exists("file.json"):
            with open("file.json") as f:
                json = f.read()
        t.sleep(2)
        time1 = datetime.datetime.now()
        subject.save()
        time2 = datetime.datetime.now()

        # check created_at
        self.assertLess(subject.created_at, time3)
        self.assertGreater(subject.created_at, time4)

        # check updated_at
        self.assertLess(subject.updated_at, time2)
        self.assertGreater(subject.updated_at, time1)

        # check if json updated
        if os.path.exists("file.json"):
            with open("file.json") as f:
                self.assertNotEqual(json, f.read())
        del subject

    def test_to_dict(self):
        """ alksfh """
        # test to_dict
        diction = {'__class__\
': 'Review', 'updated_at\
': datetime.datetime(2020, 6, 27, 22, 9, 38, 171921).isoformat('T'), 'id\
': 'b3857b62-93fa-4bbe-97de-660506f7313b', 'created_at\
': datetime.datetime(2020, 6, 27, 22, 9, 38, 171827).isoformat('T')}
        subject = Review(**diction)

        # check return
        self.assertIsNot(subject.to_dict(), subject.__dict__)
        self.assertEqual(subject.to_dict(), diction)
        del subject
