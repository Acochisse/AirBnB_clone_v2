#!/usr/bin/python3
"""
UnitTest Module for the console
"""

import os
import sys
import models
import unittest
from io import StringIO
from console import HBNBCommand
from unittest.mock import create_autospec
import os

    def test_do_quit(self):
    	"""Test quit exists"""
    	console = self.create()
        self.assertTrue(console.onecmd("quit"))

        def test_do_EOF(self):
        """Test EOF exists"""
    	console = self.create()
        self.assertTrue(console.onecmd("EOF"))

    def do_create(self):
    	"""Test do_create"""
    	return HBNBCommand()

    def test_do_show(self):
    	"""Testing that show exists"""
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
    @unittest.skipIf(
        os.getenv('HBNB_TYPE_STORAGE') == 'db',
    	"won't work in db")

    def test_do_destroy(self):
        """Test do_destroy"""
    	console = self.create()
        self.assertTrue(console.onecmd("destroy"))

    def test_do_all(self):
    	"""Test all exists"""
    	console = self.create()
        console.onecmd("all")
        self.assertTrue(isinstance(self.capt_out.getvalue(), str))

    def test_do_update(self):
        """Test do_update"""
    	console = self.create()
        self.assertTrue(console.onecmd("update"))
