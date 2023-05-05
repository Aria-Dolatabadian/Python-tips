import urllib.request

url = "ftp://ftp.sanger.ac.uk/pub/cancer/AlexandrovEtAl/somatic_mutation_data/Pancreas/Pancreas_raw_mutations_data.txt"
filename = "file.txt"  # The name to save the downloaded file as

try:
    urllib.request.urlretrieve(url, filename)
    print("File downloaded successfully!")
except urllib.error.URLError as e:
    print("Error occurred while downloading the file:", e)
