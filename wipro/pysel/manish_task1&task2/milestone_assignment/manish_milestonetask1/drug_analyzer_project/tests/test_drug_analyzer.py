import pytest
from unittest.mock import patch
from drug_analyzer_project.drug_analyzer import DrugAnalyzer

@pytest.fixture
def mock_api_response():
    return [
        {'pill_id': 'L01-10', 'pill_weight': 1000, 'active_substance': 102.88, 'impurities': 1.001},
        {'pill_id': 'L01-06', 'pill_weight': 996.42, 'active_substance': 99.68, 'impurities': 2.00087}
    ]

def test_initialization():
    # Test initialization with data
    my_drug_data = [
        ['L01-10', 1000.02, 102.88, 1.001],
        ['L01-06', 999.90, 96.00, 2.001]
    ]
    analyzer = DrugAnalyzer(my_drug_data)
    assert len(analyzer.data) == 2

    # Test initialization without data
    analyzer = DrugAnalyzer()
    assert analyzer.data == []

def test_add_data():
    analyzer = DrugAnalyzer()
    new_data = ['L01-20', 1000.00, 105.00, 1.002]
    analyzer.add_data(new_data)
    assert len(analyzer.data) == 1
    assert analyzer.data[0] == new_data

    with pytest.raises(ValueError):
        analyzer.add_data(['invalid', 1000])  # Improper length

def test_verify_series(mock_api_response):
    with patch('requests.get') as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_api_response

        analyzer = DrugAnalyzer()
        result = analyzer.verify_series('L01', 100, 0.05, 0.001)
        assert result == False  # Based on mock_api_response data

def test_verify_series_invalid_series_id():
    analyzer = DrugAnalyzer()
    with pytest.raises(ValueError):
        analyzer.verify_series(123, 100, 0.05, 0.001)  # Non-string ID
