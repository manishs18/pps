import requests
from tqdm import tqdm

url = "http://127.0.0.1:5000/t1.zip"

with requests.get(url, stream=True) as response:
    response.raise_for_status()
    total_size = int(response.headers.get('content-legth',0))
    with open("largefile.zip", "wb") as file:
        with tqdm(total=total_size, unit='B', unit_scale=True, desc="Downloading") as progress_bar:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
                progress_bar.update(len(chunk))

print("FIle downloaded successfully")
