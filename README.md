# CWAPI3D Fake Implementation

[![Run Tests](https://github.com/Brunner246/cwapi3d_fake/actions/workflows/test.yml/badge.svg)](https://github.com/Brunner246/cwapi3d_fake/actions/workflows/test.yml)

This project is a partial fake implementation of the `cwapi3d` package. It provides a set of utilities and controllers
to simulate the behavior of the `cwapi3d` package for testing and development purposes.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/Brunner246/cwapi3d_fake.git
   cd cwapi3d_fake
   ```

2. Install the required packages:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

### Running Tests

To run the tests, use the following command:

```sh
pytest
```

### Modifying Data

The `data_modifier.py` script provides functions to modify the `data.json` file. You can run this script to update the
data as needed:

```sh
python cwapi3d_fake/tests/data_modifier.py
```
