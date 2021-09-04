from vcfunded.lib import get_recent_funded

def test_recent_funded_length():
    recent = get_recent_funded()
    assert len(recent) != 0

