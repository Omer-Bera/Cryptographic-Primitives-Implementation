# Cryptographic Primitives Implementation

This repository contains raw implementations of fundamental cryptographic algorithms written to understand their underlying mathematical logic.

**⚠️ Disclaimer:** This code is for educational purposes only. It is not secure and should not be used in production.

## Files

* **`aes_cbc_implementation.c`**: A manual C implementation of the AES-128 encryption standard (CBC mode).
* **`ecc_finite_field.py`**: Python script demonstrating elliptic curve arithmetic and point operations over finite fields.
* **`cyclic_group_generator.sage`**: A SageMath script to find generators of a cyclic group.

## Usage

**AES (C):**

```bash
gcc aes_cbc_implementation.c -o aes
./aes
```

**ECC (Python):**

```bash
python3 ecc_finite_field.py
```

**Cyclic Group (SageMath):**

```bash
sage cyclic_group_generator.sage
```

---
*Written for academic study.*
