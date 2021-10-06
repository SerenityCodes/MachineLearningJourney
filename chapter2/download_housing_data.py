import os
import tarfile
import urllib.request as request

HOUSING_URL = "https://github.com/ageron/handson-ml2/blob/master/datasets/housing/housing.tgz?raw=true"
HOUSING_PATH = os.path.join("datasets", "housing")


def fetch_housing_data(housing_url=HOUSING_URL, housing_path=HOUSING_PATH):
    os.makedirs(housing_path, exist_ok=True)
    tgz_path = os.path.join(housing_path, "housing.tgz")
    request.urlretrieve(housing_url, tgz_path)
    housing_tgz = tarfile.open(tgz_path)
    housing_tgz.extractall(path=housing_path)
    housing_tgz.close()