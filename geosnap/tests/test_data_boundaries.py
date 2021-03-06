from geosnap import datasets


def test_metros():

    mets = datasets.msas()
    assert mets.shape == (945, 4)


def test_tracts():

    assert datasets.tracts_1990(convert=False).shape[0] == 60658
    assert datasets.tracts_2000(convert=False).shape == (65677, 192)
    assert datasets.tracts_2010(convert=False).shape == (72832, 194)
