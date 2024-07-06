import os
import requests
import gdown
from urllib.parse import urlparse, unquote

def create_folders():
    base_dir = "assets"
    folders = ["Pictures", "Certificates", "Projects"]
    for folder in folders:
        os.makedirs(os.path.join(base_dir, folder), exist_ok=True)

def download_file(url, folder):
    base_dir = "assets"
    parsed_url = urlparse(url)
    filename = unquote(os.path.basename(parsed_url.path))
    
    if 'drive.google.com' in url:
        file_id = url.split('/')[5]
        output = os.path.join(base_dir, folder, filename)
        gdown.download(f"https://drive.google.com/uc?id={file_id}", output, quiet=False)
    elif 'github.com' in url:
        print(f"GitHub repository link: {url}")
        print("Please clone this repository manually.")
    else:
        response = requests.get(url)
        if response.status_code == 200:
            filepath = os.path.join(base_dir, folder, filename)
            with open(filepath, 'wb') as f:
                f.write(response.content)
            print(f"Downloaded: {filename}")
        else:
            print(f"Failed to download: {url}")

def main():
    create_folders()

    certificates = [
        "https://drive.google.com/file/d/120cr9mQZsdUdpwv5e-MiHl5t6Ytrz7Po/view",
        "https://drive.google.com/file/d/19ufFwPTlODNjmy9RNBiUXOU3InUeco_T/view",
        "https://drive.google.com/file/d/1Rk4R9aT6JoDELKPNC7Y9_yg50HxCLS2l/view?usp=sharing",
        "https://drive.google.com/file/d/1odWia_koD6BwbK-4pWsmMNh3sRGTaDOX/view?usp=drivesdk",
        "https://forage-uploads-prod.s3.amazonaws.com/completion-certificates/PwC%20US/4KqDALSkyRNPXjQGa_PwC%20US_6GD79jbdfB7tFeFTj_1700853864130_completion_certificate.pdf",
        "https://drive.google.com/file/d/1AQI6nZfMkiA1fdyYaR3Bvpui3FFsBL4L/view?usp=sharing"
    ]

    pictures = [
        "https://media.licdn.com/dms/image/D562DAQGBb4i6NLUoXQ/profile-treasury-image-shrink_800_800/0/1719364265776?e=1720544400&v=beta&t=7LlY-nXp8JtX2iFS9Qi3-I7rbtklVg3Fi7Y4YY2ciA0",
        "https://drive.google.com/file/d/1ZBK8hMiHFhwJkymQEZ9aPhJxzbJBeGL4/view?usp=sharing"
    ]

    projects = [
        "https://docs.google.com/file/d/12kjSZp_8XxADhW4a_mzaIUkBWWJd2q95/edit?filetype=mspresentation",
        "https://github.com/KanishkThamman/intel-project-air_polution_predictor-/tree/main"
    ]

    for url in certificates:
        download_file(url, "Certificates")

    for url in pictures:
        download_file(url, "Pictures")

    for url in projects:
        download_file(url, "Projects")

if __name__ == "__main__":
    main()
