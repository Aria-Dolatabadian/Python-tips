import pkg_resources

required_packages = ['biopython', 'lxml', 'matplotlib-venn',"pyranges","pysam","scipy","seaborn","statsmodels"]

for package in required_packages:
    try:
        dist = pkg_resources.get_distribution(package)
        print(f"{package} is installed (version {dist.version})")
    except pkg_resources.DistributionNotFound:
        print(f"{package} is not installed")
