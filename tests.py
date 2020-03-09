"""Testsq for Balloonicorn's Flask app."""

import unittest
import party


class PartyTests(unittest.TestCase):
    """Tests for my party site."""

    def setUp(self):
        """Code to run before every test."""

        self.client = party.app.test_client()
        party.app.config['TESTING'] = True

    def test_homepage(self):
        """Can we reach the homepage?"""

        result = self.client.get("/")
        self.assertIn(b"having a party", result.data)

    def test_no_rsvp_yet(self):
        """Do users who haven't RSVPed see the correct view?"""

        result = self.client.get("/")
        self.assertIn(b"<h2>Please RSVP</h2>", result.data)

    def test_rsvp(self):
        """Do RSVPed users see the correct view?"""

        rsvp_info = {'name': "Jane", 'email': "jane@jane.com"}

        result = self.client.post("/rsvp", data=rsvp_info,
                                  follow_redirects=True)

        # FIXME: check that once we log in we see party details--but not the form!
        self.assertIn(b"<h2>Welcome</h2>", result.data)

    def test_rsvp_mel(self):
        """Can we keep Mel out?"""

        # FIXME: write a test that mel can't invite himself
        mel_rsvp = {'name': "Mel Melitpolski", 'email': "mel@ubermelon.com"}
        
        result = self.client.post("/rsvp", data=mel_rsvp, follow_redirects=True)

        self.assertIn(b'<div class="alert alert-info"> Sorry, Mel. This is kind of awkward.</div>', result.data)


if __name__ == "__main__":
    unittest.main()
