This is the replication package for papaer "Insights into Deep Learning Refactoring: Bridging the Gap Between Practices and Expectations"
# Contents
## Refactoring Commits
commitsX.zip: refactoring commits named by SHA, consists of related python files "before" and "after" change, and "commit.json".

commit_list.csv: information of labeled commits, consists of SHA, commits date, url, label("1"), refactoring operation.

ref_filter.py: filter commit by refactoring operation type.

## Raw Data of Questionnaire Answer
questionnaire.csv

# How to Use the Refactoring Commits Data
1. Unzip the compression bags.
2. Change "target_type" in "ref_filter.py" to the refactoring operation type you want.
