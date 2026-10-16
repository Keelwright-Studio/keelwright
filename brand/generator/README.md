Python generators for the mark SVGs. `marks3.k_final(size, ground, badge, accent, course)` is the chosen mark
(course defaults to on at 48 px and above); `marks.py` and `marks2.py` hold the explored concepts.
Regenerate the kit with: `python3 -c "from marks3 import k_final; print(k_final(256,'light'))" > ../keelwright-mark.svg`
(then add the xmlns attribute). No dependencies beyond Python 3.
