def test_unitSystemOne():
    units = "46"
    assert units == "Imperial" or units == "Metric"
    if units == "Imperial":
        units = "sq ft"
        return units
    if units == "Metric":
        units = "sq meters"
        return units
    else:
        print("Please enter Imperial or Metric")


def test_unitSystemTwo():
    units = "imperial"  # In future make sure code can recognize lower case input
    assert units == "Imperial" or units == "Metric"
    if units == "Imperial":
        units = "sq ft"
        return units
    if units == "Metric":
        units = "sq meters"
        return units
    else:
        print("Please enter Imperial or Metric")

def test_unitSystemThree():
    units = "Imperial"
    assert units == "Imperial" or units == "Metric"
    if units == "Imperial":
        units = "sq ft"
        return units
    if units == "Metric":
        units = "sq meters"
        return units
    else:
        print("Please enter Imperial or Metric")