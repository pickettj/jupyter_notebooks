# Python Lab

Testing out various Python routines.

Useful links:

- [Guide to Pandas for Humanists](https://pandas.pythonhumanities.com/intro.html).
- [Binder](https://mybinder.org/): Free site for using Git to host Jupyter notebooks for outside users (i.e. great for demoing).
- Web scraping:
  - Mat Lavin [slides](https://docs.google.com/presentation/d/1JnMZbl7434RrzAHluKOT4OyUxCpln3B_7QYoSa01X0M/edit#slide=id.p) & [repo](https://github.com/mjlavin80/advanced-webscraping-pitt-february-2020)
  - [Method for mapping website lacking an index](https://www.freecodecamp.org/news/how-to-build-a-url-crawler-to-map-a-website-using-python-6a287be1da11/)
- [Online Jupyter Notebooks for teaching purposes](https://github.com/iamlemec/data_science)

Python3.8 is necessary for a number of new functions (notably the walrus operator), but it's a bit of a challenge to get it working with Jupyter:

- First [create a new conda environment](https://stackoverflow.com/questions/58568175/upgrade-to-python-3-8-using-conda): `conda create -n python38 python=3.8`
- Then install the new Python into the kernel: `python3.8 -m ipykernel install --user --name python38 --display-name "Python 3.8"`
- It will be necessary to reinstall packages for the new environment.
