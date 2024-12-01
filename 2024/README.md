# Log

## 2024-12-01
- Ljubljana first day of AOC
- Didn't like the `item` requirement for numpy to get values
- `radon cc`, `radon mi`, `radon hal` for quality
- Stubburn to answer without `for` changed to `juxt` and `map_curried`
- `python -c "import ast; print(ast.dump(ast.parse(open('2024/d1/d1.py').read()), indent=4))" | wc -l`
- `python -c "import dis; dis.dis(open('2024/d1/d1.py').read())" | wc -l` 
- `python -c "import dis; print(sum(1 for _ in dis.Bytecode(open(''2024/d1/d1.py'').read())))"`
- `python -m cProfile 2024/d1/d1.py`
- `python -m cProfile -o profile_results.prof 2024/d1/d1.py`
