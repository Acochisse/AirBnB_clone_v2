#!/usr/bin/python3
"""UnitTests for the console"""

import os
import sys
import models
import unittest
from io import StringIO
from console import HBNBCommand
from unittest.mock import create_autospec
import os


class test_console(unittest.TestCase):
    """UnitTest for console module"""

    def test_quit(self):
        """Test quit exists"""
        console = self.create()
        self.assertTrue(console.onecmd("quit"))

    def test_EOF(self):
        """"Test EOF exists"""
        console = self.create()
        self.assertTrue(console.onecmd("EOF"))

    def create(self):
        """Tests create an instance of the HBNBCommand"""
        return HBNBCommand()

    def test_show(self):
        """ Test that show exists """
        console = self.create()
        console.onecmd("create User")
        user_id = self.capt_out.getvalue()
        sys.stdout = self.backup
        self.capt_out.close()
        self.capt_out = StringIO()
        sys.stdout = self.capt_out
        console.onecmd("show User " + user_id)
        x = (self.capt_out.getvalue())
        sys.stdout = self.backup
        self.assertTrue(isinstance(x, str))

    def test_destroy(self):
        """tests destroy"""
        console = self.create()
        self.assertTrue(console.onecmd("destroy"))

    def test_update(self):
        """tests update"""
        console = self.create()
        self.assertTrue(console.onecmd("update"))
