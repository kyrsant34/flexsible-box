import functools
import json
import yaml

from django.apps import apps
from django.core.management.base import BaseCommand
from path import Path


def load(f, load_f):
    with open(f, 'r') as input_file:
        return load_f(input_file)


def save(f, data, save_f, extra=None):
    if extra is None:
        extra = {}
    with open(f, 'w') as output_file:
        return save_f(data, output_file, **extra)


class Command(BaseCommand):

    initial_data_fixture = 'initial_data'
    fixture_format = 'yaml'

    loaders = {
        '.yaml': functools.partial(load, load_f=yaml.load),
        '.json': functools.partial(load, load_f=json.load),
    }

    savers = {
        'yaml': functools.partial(save, save_f=yaml.dump),
        'json': functools.partial(save, save_f=json.dump)
    }

    def handle(self, *args, **options):

        # Result data
        seen_items = {}

        # Iterate over apps
        configs = apps.get_app_configs()
        for app in configs:

            clean_data = []

            # Skip apps w/o fixture dir
            fixture_path = Path(app.path) / 'fixtures'
            if not fixture_path.exists():
                continue

            # Iterate over fixture files
            for fixture_file in fixture_path.walkfiles():

                # Skip initial data fixtures
                if fixture_file.name.stripext() == self.initial_data_fixture:
                    continue

                # Load data
                fixture_data = self.loaders.get(fixture_file.ext, lambda x: {})(fixture_file)

                for item in fixture_data:

                    # Skip seen ids
                    seen_id = "{}|{}".format(item['model'], item['pk'])
                    if seen_id in seen_items:
                        continue

                    # Add data to result
                    seen_items[seen_id] = True
                    clean_data.append(item)

            result_file = fixture_path / "{}.{}".format(self.initial_data_fixture, self.fixture_format)
            self.savers.get(self.fixture_format)(result_file, clean_data)
