# Custom Converters

An example showing how custom converters work. You can specify Python module paths to your custom converter definitions with the `-c` or `--converters` flags in the Shellshock CLI.

To run this example:
```bash
shellshock -c examples.coverters.converters examples/converters/script.py
```

## Multiple Custom Converters

Chain together custom converter definitions with multiple `-c`/`--converters` arguments:

```bash
shellshock -c custom.converters1 -c custom.converters2 myscript.py
```
