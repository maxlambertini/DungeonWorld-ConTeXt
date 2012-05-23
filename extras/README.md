## Extra Utilities

`dwjoiner.py` is a simple tool for preparing original XML DungeonWorld file for XHTML2CTX, a tool
that performs a preliminary conversion from XHTML (sort of) to TeX, ConTeXt flavor that can be found
here: https://github.com/maxlambertini/xhtml2ctx

### usage

* Copy `dwjoiner.py` and `filelist.txt` where the original DungeonWorld XML are.
* Launch `dwjoiner.py`
* You'll get a big file named `dw_big.xml`. Feed this file to XHTML2CTX to get ConTeXt files. 
