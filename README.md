# VCF PARSER AND WRITER LIBRARY IN PYTHON 

* `WARNING` this library is under development for more information check the ROADMAP down bellow.


## ROADMAP

* WRITER:

- [X] Support NAME, FN, ADDRESS, Birthday
- [ ] Support other V-CARD fields.
- [ ] Code Refcatoring if it necessary.

* PARSER:
- [ ] ....


## Usage 

### EXAMPLE
```python
vcf = VcfV3()
vcf.Insert_name("<lastname>","<firstname>")
vcf.Insert_FN("<display name>")
vcf.Write("<filename>")
```
* NOTE: You can Check the source code for more api Library api understading.
