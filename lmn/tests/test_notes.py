
from django.urls import reverse

from django.test import TestCase
from lmn.models import Note




class TestUser(TestCase):

 def delete_own_note(self):
    response = self.client.post(reverse('delete', kwargs={'note_pk': 2}), follow=True)
    note_2 = Note.objects.filter(pk=2)
    assert note_2 is None


 def delete_someone_else_note_not_auth(self):
    response = self.client.post(reverse('delete', kwargs={'note_pk': 6}), follow=True)
    self.assertEqual(401, response.status_code)
    note_5 = Note.objects.filter(pk=5)
    assert note_5 is not None
 def test_add_notes(self):

        response = self.client.post(reverse('note_details', kwargs={'note_pk':4}), {'notes':'yay'}, follow=True)

        updated_note_4 = Note.objects.get(pk=4)

        # db updated?
        self.assertEqual('yay', updated_note_4.notes)

        # Correct object used in response?
        self.assertEqual(response.context['note'], updated_note_4)
        # Check correct template was used
        self.assertTemplateUsed(response, 'lmnop/note_detail.html')

        # and correct data shown on page?
        text_rendered = str(response.content)
        assert 'yay' in text_rendered    # new text added

