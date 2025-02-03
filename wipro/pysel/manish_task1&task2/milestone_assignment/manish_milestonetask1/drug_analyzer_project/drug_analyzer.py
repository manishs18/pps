import requests

class DrugAnalyzer:
    def __init__(self, data=None):
        self.data = data if data else []

    def add_data(self, new_data):
        if len(new_data) != 4 or not isinstance(new_data, list):
            raise ValueError("Improper length or type of the added list.")
        self.data.append(new_data)
        return self

    def verify_series(self, series_id, act_subst_wgt, act_subst_rate, allowed_imp):
        if not isinstance(series_id, str) or len(series_id) != 3:
            raise ValueError("Invalid series_id format")

        # Request data from the API for the series
        response = requests.get(f"http://api.example.com/pills?series={series_id}")
        if response.status_code != 200:
            raise ValueError(f"Error fetching data for series {series_id}")

        pills = response.json()

        total_weight = 0
        total_substance = 0
        total_impurities = 0

        for pill in pills:
            total_weight += pill['pill_weight']
            total_substance += pill['active_substance']
            total_impurities += pill['impurities']

        # Verify active substance and impurities conditions
        if not (act_subst_wgt * (1 - act_subst_rate) <= total_substance <= act_subst_wgt * (1 + act_subst_rate)):
            return False
        if total_impurities > allowed_imp * total_weight:
            return False
        return True
