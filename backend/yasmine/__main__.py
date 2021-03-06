#!/usr/bin/env python
import argparse
import os

from yasmine.app.settings import TORNADO_HOST, TORNADO_PORT, MEDIA_ROOT, LOGGING_ROOT, RUN_ROOT, TMP_ROOT,\
    NRL_ROOT
import sys


def runserver_cmd(values):
    from yasmine.app.run import runserver as yasmine_run
    yasmine_run(values.debug, values.host, values.port)


def create_sys_folder():
    sys_folders = [
        MEDIA_ROOT,
        LOGGING_ROOT,
        RUN_ROOT,
        TMP_ROOT,
        NRL_ROOT
    ]
    for folder in sys_folders:
        if not os.path.exists(folder):
            os.makedirs(folder)


def syncdb(values):
    import alembic.config
    import yasmine 
    os.chdir(yasmine.__path__[0])
    alembic.config.main(argv=values.alembic_args)


def run_test_cmd(*_, **__):
    import unittest

    from yasmine.app.tests.unit.inv_valid import ValidateInventoryTests
    from yasmine.app.tests.integration.imp_exp import ImportExportStationXmlt
    from yasmine.app.tests.gui.home import HomeTest
    from yasmine.app.tests.gui.xml_list import XmlListTest
    from yasmine.app.tests.unit.nrl_io import NrlIoTest
    from yasmine.app.tests.unit.attr_validation import AttrValidationTests
    from yasmine.app.tests.gui.settings import SettingsTest
    loader = unittest.TestLoader()
    alltests = unittest.TestSuite([
        loader.loadTestsFromTestCase(AttrValidationTests),
        loader.loadTestsFromTestCase(ValidateInventoryTests),
        loader.loadTestsFromTestCase(ImportExportStationXmlt),
        loader.loadTestsFromTestCase(NrlIoTest),
        loader.loadTestsFromTestCase(HomeTest),
        loader.loadTestsFromTestCase(XmlListTest),
        loader.loadTestsFromTestCase(SettingsTest)
    ])
    runner = unittest.TextTestRunner(failfast=True)
    result = runner.run(alltests)
    sys.exit(not result.wasSuccessful())

def main():

    # get command line arguments after the command $0
    args = []
    if (len(sys.argv) > 1):
        args = sys.argv[1:]

    create_sys_folder()

    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(help="Sync database/run server commands.")

    parser_syncdb = subparsers.add_parser("syncdb", help="Sync database command parser")
    parser_syncdb.set_defaults(func=syncdb)
    parser_syncdb.add_argument('alembic_args', nargs=argparse.REMAINDER)

    parser_test = subparsers.add_parser("test", help="Run tests")
    parser_test.set_defaults(func=run_test_cmd)

    parser_runserver = subparsers.add_parser("runserver", help="Runserver parser")
    parser_runserver.add_argument("--port", type=int, default=TORNADO_PORT, help="Port to use (%(default)s))")
    parser_runserver.add_argument("--host", type=str, default=TORNADO_HOST, help="Hostname to listen on (%(default)s))")
    parser_runserver.add_argument("--debug", action='store_true', help="Start server in the debug mode.")
    parser_runserver.set_defaults(func=runserver_cmd)
    values = parser.parse_args(args)
    if values.__dict__:
        values.func(values)

if __name__ == "__main__":
    main()