from mlproject import distance

def test_distance():
    assert distance.haversine(1,1,1,1) == 0
