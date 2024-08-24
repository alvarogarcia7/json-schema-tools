import unittest
from typing import Any

from approvaltests import verify
from approvaltests.namer import NamerFactory

from test.approval_tests.command_helper import CommandHelper


class TestGenerateCli(unittest.TestCase):
    command_helper: CommandHelper

    @classmethod
    def setUpClass(cls: Any) -> None:
        cls.command_helper = CommandHelper()
        # approvaltests.set_default_reporter(PythonNativeReporter())

    def test_make_custom_private_key_1(self) -> None:
        verify(options=NamerFactory.with_parameters("modify"), data=self.command_helper.invoke_command(
            self.command_helper.to_list(f"""\
genson data/sample1.json
""")))


if __name__ == '__main__':
    unittest.main()
