# Calculator App

This is a simple command-line calculator application written in Python. It evaluates arithmetic expressions and outputs the result in JSON format.

## Features

*   Evaluates basic arithmetic expressions.
*   Supports addition (`+`), subtraction (`-`), multiplication (`*`), and division (`/`).
*   Respects operator precedence.
*   Outputs results in a structured JSON format.

## Usage

To use the calculator, run the `main.py` script from your terminal, providing the expression as a command-line argument.

```bash
python main.py "<expression>"
```

### Example

```bash
python main.py "3 + 5 * 2"
```

This will output:

```json
{
    "expression": "3 + 5 * 2",
    "result": 13.0
}
```

## Error Handling

The calculator handles invalid expressions and provides informative error messages.

```bash
python main.py "3 + * 2"
```

This will output:

```
Error: invalid token: *
```
