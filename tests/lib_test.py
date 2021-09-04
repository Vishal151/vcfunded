from vcfunded.lib import get_recent_funded, get_by_category

def test_recent_funded_length():
    recent = get_recent_funded()
    assert len(recent) != 0

def test_rand_by_category_length():
    recent = get_by_category()
    assert len(recent) != 0
