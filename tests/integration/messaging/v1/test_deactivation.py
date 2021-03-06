# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from tests import IntegrationTestCase
from tests.holodeck import Request
from twilio.base.exceptions import TwilioException
from twilio.http.response import Response


class DeactivationsTestCase(IntegrationTestCase):

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.messaging.v1.deactivations().fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://messaging.twilio.com/v1/Deactivations',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "redirect_to": "https://www.twilio.com"
            }
            '''
        ))

        actual = self.client.messaging.v1.deactivations().fetch()

        self.assertIsNotNone(actual)
