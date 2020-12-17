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
