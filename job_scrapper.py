from extractors.wwr import extract_wwr_jobs
from file import save_to_file
keyword = input("what do you want to search for?")
wwr=extract_wwr_jobs(keyword)
jobs= wwr
save_to_file(keyword,jobs)
