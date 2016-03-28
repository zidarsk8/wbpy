import sys
import json
import unittest

import mock

from wbpy import utils


class TestFetchFn(unittest.TestCase):

    def setUp(self):
        # The response contains non-ascii characters, so encoding can be tested
        # against different python versions.
        self.url = "http://api.worldbank.org/topic?format=json&"
        "mrv=1&per_page=10000"

    def tearDown(self):
        mock.patch.stopall()

    def test_caching_response(self):
        cache_fn = mock.patch("wbpy.utils._cache_response").start()
        res = utils.fetch(self.url, check_cache=False, cache_response=True)
        self.assertTrue(cache_fn.called)

        # The response will be json-decoded, so make sure not have
        # str/unicode/byte problems.
        self.assertTrue(json.loads(res))

    def test_fetching_from_cache(self):
        # Make call once so we know it's been cached
        utils.fetch(self.url, check_cache=False, cache_response=True)

        # Make sure reading from file, rather than calling url
        if sys.version_info > (3,):
            urlopen = "urllib.request.urlopen"
        else:
            urlopen = "urllib2.urlopen"

        urlopen_fn = mock.patch(urlopen).start()
        res = utils.fetch(self.url, check_cache=True)
        self.assertFalse(urlopen_fn.called)

        # The response will be json-decoded, so make sure not have
        # str/unicode/byte problems.
        self.assertTrue(json.loads(res))
