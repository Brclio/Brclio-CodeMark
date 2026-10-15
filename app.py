#!/usr/bin/env python
import os
import sys


def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "codemark_project.settings")
    from django.core.management import execute_from_command_line

    if len(sys.argv) == 1:
        sys.argv.extend(["runserver", "0.0.0.0:8991"])
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
