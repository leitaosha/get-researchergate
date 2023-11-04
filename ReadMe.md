# Introduction
[![Using Get Researchgate](https://img.shields.io/badge/Using-Get%20Researchergate-blue?style=flat-round&logo=github)](https://github.com/leitaosha/get-researchergate)
[![GitHub Repo stars](https://img.shields.io/github/stars/leitaosha/get-researchergate?label=⭐get-researchergate)](https://github.com/leitaosha/get-researchergate)
[![License](https://img.shields.io/github/license/leitaosha/get-researchergate)](https://github.com/leitaosha/get-researchergate/LICENSE)

[//]: # (![Downloads latest release]&#40;https://img.shields.io/github/downloads/leitaosha/get-researchergate/total?color=yellow&#41;)

**If you like this project, please give it a ⭐Star.**

This is a python script that gets all the article meta information (include doi, title, publication etc.) of the author from [researchgate](https://www.researchgate.net/).

# How to use?

1. Clone this repository to your computer.
2. Install [Python3.10](https://www.python.org/downloads/windows/). 
3. Install dependencies. ```pip install -r requirements.txt```
4. Configure some information:
   - Download the same version of [chromedriver.exe](https://googlechromelabs.github.io/chrome-for-testing/#stable) and Chrome. 
   - ![](https://s2.loli.net/2023/10/31/Fnw8gtUYmyM9JDv.png)
   - Unzip chrome and chromedriver to the repository root. Make sure the directory format looks like this. Put the chrome.exe and chromedriver.exe in the chrome and chromedriver directory respectively.
   ```text
      |—crawlerutils    # crawler script
      | | Article.py
      | | AuthorArtical.py
      | | ...
      |
      | DATA            # export folder
      | config.py       # config file
      | main.py         # Execute functions
      |
      |─chrome          # chrome folder
      |  | ...
      |  | chrome.exe
      |  | ...
      |
      |─chromedriver    # chromedriver folder
      |  | chromedriver.exe
   ```

5. Open `config.py` and replace the `Url`. Execute python script. `python run main.py`

# TODO

- [x] Export in xlsx format
- [x] More fields
- [x] Clean the useless data
- [ ] Multithreading
