# -*- coding: utf-8 -*-
"""check_compatibility must accept the version strings that ActiveState's
urllib3 builds report: plain, PEP 440 local (+security.N) and post-release
(.postN)."""

import pytest

from requests import check_compatibility


@pytest.mark.parametrize('urllib3_version', (
    '1.26.20',
    '1.26',
    '1.26.20+security.2',
    '1.26.20.post3',
    '1.26.20.post4',
    '1.21.1',
))
def test_supported_urllib3_versions(urllib3_version):
    check_compatibility(urllib3_version, '3.0.4', None)


@pytest.mark.parametrize('urllib3_version', ('2.0.7', '1.20.0', '1.27.0.post1'))
def test_unsupported_urllib3_versions(urllib3_version):
    with pytest.raises(AssertionError):
        check_compatibility(urllib3_version, '3.0.4', None)
