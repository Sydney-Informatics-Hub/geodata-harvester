# Welcome to Geodata-Harvester Contributing Guide 

Thank you for investing your time in contributing to our project! 

Contributions to the geodata-harvester can be made in many ways, such as:

- Feedback and bug reports via Github Issue
- Use-case examples via notebook contributions
- Code-base contributions
- New data-source contributions
- Updating existing data source modules
- Improving documentation


## Create a new issue

If you spot a problem or have a suggestion for improvement, [search if an issue already exists](https://github.com/Sydney-Informatics-Hub/geodata-harvester/issues). If a related issue doesn't exist, please open a new issue. The issue should address what is the current problem, where it occurs, and, if possible, at least one suggestion how this problem can be addressed. If this is a bug report, please add the error statement including file name and code line, and your installation details, so that the error can be reproduced.

## Solve an issue

Scan through our [existing issues](https://github.com/Sydney-Informatics-Hub/geodata-harvester/issues) to find one that interests you. As a general rule, we don’t assign issues to anyone. If you find an issue to work on, you are welcome to open a pull request with a fix.

## Make Changes

### Make documentation changes

For small documentation changes, please open a new Issue. If you would like to add/edit some more documentation, please fork the repo, edit the corresponding .md file, commit the change, and create a pull request for a review.


### Add or edit Notebooks

A great start to add and test new functionalities and use-cases is via Jupyter notebooks. Currently we maintain a few basic example notebooks that demonstrate some use-cases of the GeoData-Harvester. If you make use of this package, you are welcome to improve existing notebooks or add new notebooks that provide helpful workflows to the community. 

Please fork the geodata-harvester repo and add your notebook, including your name as author, and settings file to the folder `notebooks`. For reproducible research we encourage the use of settings YAML files (see notebooks/settings). Please give the settings file a name that corresponds to the notebook name. Then commit your changes and create a pull request for a review and to add your notebook to the geodata-harvester repo. 

### Make code changes

We welcome contributions to improve the Python code and keep the data-sources up-tp-date. We encourage to submit an Issue request first. To add your code edits to the geodata-harvester, please fork the repo, commit your changes and create a pull request for a review. 

### Add new data source modules

To add a new data source, please visit the [geodata-harvester contribution guidelines](Contributing.md). Please also submit an Issue request about the data source that you would like to add. Please fork the repo and test your new new data source locally (test scripts and example notebook for the new data source are welcome!). After successful testing, please create a pull request for a review and add details as comment to the Issue. 