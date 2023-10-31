# Introduction

This is a python script to get researcher's all DOI of articles (include book etc.) from [researchgate](https://www.researchgate.net/)

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
- [ ] Export based on customized conditions
- [ ] Multithreading
