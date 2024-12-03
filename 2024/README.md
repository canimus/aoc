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
```bash
(.venv) herminio@LAPTOP-T7U0GVOQ:~/aoc/2024/d1$ hyperfine "python d1.py" "python d1a.py" "python d1b.py" 
Benchmark 1: python d1.py
  Time (mean ± σ):     119.3 ms ±   7.9 ms    [User: 795.3 ms, System: 13.0 ms]
  Range (min … max):   113.5 ms … 147.0 ms    22 runs
 
Benchmark 2: python d1a.py
  Time (mean ± σ):     119.3 ms ±   7.2 ms    [User: 793.9 ms, System: 15.9 ms]
  Range (min … max):   111.6 ms … 140.6 ms    26 runs
 
Benchmark 3: python d1b.py
  Time (mean ± σ):     100.9 ms ±  11.1 ms    [User: 652.1 ms, System: 9.5 ms]
  Range (min … max):    91.7 ms … 138.9 ms    26 runs
 
Summary
  python d1b.py ran
    1.18 ± 0.15 times faster than python d1a.py
    1.18 ± 0.15 times faster than python d1.py
```

## 2024-12-03
- Completed day 3, this one was with `regex` 
- Dinner was __Chilpachole de Robalo__