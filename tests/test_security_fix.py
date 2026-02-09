
import unittest
from unittest.mock import patch, MagicMock
import asyncio
import html
import sys
import os

# Add the root directory to sys.path to allow importing src
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Mock dependencies before importing src.utils.helper
sys.modules['requests'] = MagicMock()
mock_config = MagicMock()
sys.modules['config'] = mock_config
mock_config.TELEGRAM_TOKEN = "test_token"
mock_config.TELEGRAM_CHAT_ID = "test_chat_id"
mock_config.TELEGRAM_TOKEN_SENTIMENT = "sent_token"
mock_config.TELEGRAM_CHAT_ID_SENTIMENT = "sent_chat_id"
mock_config.TELEGRAM_MESSAGE_THREAD_ID = None
mock_config.TELEGRAM_MESSAGE_THREAD_ID_SENTIMENT = None
mock_config.LOG_FILENAME = "test.log"
mock_config.DAFTAR_KOIN = []

import requests # This will now be the mock

from src.utils.helper import kirim_tele, kirim_tele_sync

class TestSecurityFix(unittest.IsolatedAsyncioTestCase):

    async def test_kirim_tele_escapes_by_default(self):
        requests.post.return_value.status_code = 200
        requests.post.return_value.text = "OK"

        test_pesan = "Hello <script>alert('xss')</script> & world"
        expected_escaped = html.escape(test_pesan)

        await kirim_tele(test_pesan)

        # Verify requests.post was called with escaped text
        self.assertTrue(requests.post.called)
        args, kwargs = requests.post.call_args
        sent_text = kwargs['data']['text']
        self.assertIn(expected_escaped, sent_text)
        self.assertNotIn("<script>", sent_text)
        requests.post.reset_mock()

    async def test_kirim_tele_respects_is_html(self):
        requests.post.return_value.status_code = 200
        requests.post.return_value.text = "OK"

        test_pesan = "<b>Bold Text</b>"

        await kirim_tele(test_pesan, is_html=True)

        self.assertTrue(requests.post.called)
        args, kwargs = requests.post.call_args
        sent_text = kwargs['data']['text']
        self.assertIn(test_pesan, sent_text)
        requests.post.reset_mock()

    async def test_kirim_tele_alert_prefix_not_escaped(self):
        requests.post.return_value.status_code = 200
        requests.post.return_value.text = "OK"

        test_pesan = "Safe message"

        await kirim_tele(test_pesan, alert=True)

        self.assertTrue(requests.post.called)
        args, kwargs = requests.post.call_args
        sent_text = kwargs['data']['text']
        self.assertIn("⚠️ <b>SYSTEM ALERT</b>\n", sent_text)
        self.assertIn("Safe message", sent_text)
        requests.post.reset_mock()

    def test_kirim_tele_sync_escapes_by_default(self):
        requests.post.return_value.status_code = 200
        requests.post.return_value.text = "OK"

        test_pesan = "Hello <script>alert('xss')</script>"
        expected_escaped = html.escape(test_pesan)

        kirim_tele_sync(test_pesan)

        self.assertTrue(requests.post.called)
        args, kwargs = requests.post.call_args
        sent_text = kwargs['data']['text']
        self.assertEqual(expected_escaped, sent_text)
        requests.post.reset_mock()

    def test_kirim_tele_sync_respects_is_html(self):
        requests.post.return_value.status_code = 200
        requests.post.return_value.text = "OK"

        test_pesan = "<i>Italic</i>"

        kirim_tele_sync(test_pesan, is_html=True)

        self.assertTrue(requests.post.called)
        args, kwargs = requests.post.call_args
        sent_text = kwargs['data']['text']
        self.assertEqual(test_pesan, sent_text)
        requests.post.reset_mock()

if __name__ == '__main__':
    unittest.main()
