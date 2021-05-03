
# Assessment task for Backend Data Engineer Internship

**```Before proceeding with the assignment task please make sure to fill up the given questionnaire form share already and available at```** [Backend Data Engineer Internship Questionnaire Form](https://forms.office.com/r/BPNshF57V0).

**2 identical XLS files are shared which contains data sampled at `1 sample/second`**

These 2 data files are from the same data source and represents same data, due to space restrictions of the file type it is divided into 2 separate files named *'data.xlsx'* and *'data_1.xlsx'* and while saving the data, it is also saved not accordingly, follow the index column named *'Record Index'* to see the parity. 

## Tasks

1. Create 3 separate *'*.csv'* files named `'detail.csv'`, `'detailVol.csv'` and `'detailTemp.csv'`.
	1. Combine all the data in sheets named like "Detail_67_" only, among the two data files provided, and save into `'detail.csv'`
	2. Combine all the data in sheets named like "DetailVol_67_" only, among the two data files provided, and save into `'detailVol.csv'`
	3. Combine all the data in sheets named like "DetailTemp_67_" only, among the two data files provided, and save into `'detailTemp.csv'`
Provide attention to the column `'Record Index'` which provided index values to avoid mismatching the rows while combining multiple files.

2. Apply down-sampling method to reduce the sampling rate  to `1 sample/minute`. Appy the same to `'detail.csv'`, `'detailVol.csv'` and `'detailTemp.csv'` and creating 3 files named  `'detailDownsampled.csv'`, `'detailVolDownsampled.csv'` and `'detailTempDownsampled.csv'`
3. Apply `low pass filter` technique for noise removal on the data set for  `'detailVolDownsampled.csv'` and show  the distribution of the dataset through visualization, also provide explanation of the same.

4. Run profile for all the functions; use `cProfile` for Python for profiling of individual functions.

5. Run unit test on each function,i.e., write test cases for each function. Use `unittest` for the same.
6. Try to maintain Coding Style Guide **PEP-8**, and use `pylint` or `flake8` to check the code for PEP-8 violations.

## Deliverables

1. One *'\*.py'*  file with detailed commented code on the working for *`Task 1`* and its subtasks. The intention is to see how the code is architected rather than simple execution. Try employing functional programming concepts and making the code look clean by following PEP-8 coding style.
	1. The code should be reproducible  on any environment; i.e. system agnostic and the intended data files should be generated running the code.
2. One *'\*.py'*  file with detailed commented code on the working for *`Task 2`* and its subtasks. Try employing functional programming concepts and making the code look clean by following PEP-8 coding style.
	1. The code should be reproducible  on any environment; i.e. system agnostic and the intended data files should be generated running the code
3. One Jupyter NoteBook file for `Task 3` along with visualization.
4. Profile testing result in a *"\*.txt"* file  for all the functions runtime; use `cProfile`
5. Unit testing result in a *"\*.txt"* file  for all the functions ; use `unittest`.

## Deadline

1 day from receiving the assignment.

## Submission

Share  all the deliverable codebase (Only Code *.py* or *.ipynb* files, no Data ) over a public `GitHub` or `GitLab` or `BitBucket` repository with a clean git tree and periodic commits;
include a `Readme.md` describing on how to run the files for each task clearly mentioned. Please make sure that the provided repository is public and can be cloned from anywhere by anyone.
Follow the below mentioned link to share the result of the assignment.

**[Assignment Submission Form](https://forms.office.com/r/Yg6bNrcLKu)**

Do note here, after the deadline is over the assignment submission link will be deactivated. For any further issues reply at [saradindu@nunam.com](mailto:saradindu@nunam.com).
