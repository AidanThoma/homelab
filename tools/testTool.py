"""
title: Testing Tool
description: Testing Purposes.
"""

class tools:
    def __init__(self):
        self.initialValue = 'This test tool is working! Good job :)'

    def testing(self):
        return self.initialValue

tool = tools()
print(tool.testing())