# ScriptCollection ![PyPI](https://img.shields.io/pypi/v/ScriptCollection)

This repository is the place for little scripts which are also useful in future so that someone does not have remember them and write them new froms sratch. You can simply use the scripts.

## Functions

TODO

## Hints

Most of the scripts are written in [python](https://www.python.org) 3.

Caution: Before executing **any** script of this repository read the sourcecode of the script (and the sourcecode of all functions called by this function directly or transitively) carefully and verify that the script does exactly what you want to do and nothing else.

## Get ScriptCollection

### Installation via pip

```
pip install ScriptCollection
```

pip requires [Python](https://www.python.org) 3. See the [pypi-site of ScriptCollection](https://pypi.org/project/ScriptCollection) for more information.

### Download sourcecode using git

You can simply git-clone the ScriptCollection and then use the scripts under the provided license.

```
git clone https://github.com/anionDev/ScriptCollection
```

It may be more easy to pip-install the ScriptCollection but technically pip is not required. Actually you need to git-clone (or download as zip-file from [Github](https://github.com/anionDev/ScriptCollection) the ScriptCollection to use the scripts in this repository which are not written in python.

## Troubleshooting

It is recommended to always use only the newest version of the ScriptCollection. If you have an older version: Update it (e. g. using `pip install ScriptCollection --upgrade` if you installed the ScriptCollection via pip). If you still have problems, then feel free to create an [issue](https://github.com/anionDev/ScriptCollection/issues).

If you have installed the ScriptCollection as pip-package you can simply check the version using Python with the following command:

```
from ScriptCollection.core import get_ScriptCollection_version
get_ScriptCollection_version()
```

## License

ScriptCollection itself is licensed under the terms of MIT. See the [license](https://raw.githubusercontent.com/anionDev/ScriptCollection/master/License.txt) for more details.
