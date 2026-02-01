# Cryptographic Primitives Implementation

This repository contains educational implementations of fundamental cryptographic algorithms and mathematical structures. 

## ⚠️ SECURITY WARNING (DISCLAIMER)

**THIS CODE IS FOR EDUCATIONAL PURPOSES ONLY.**

* **DO NOT** use this code in production environments or to protect sensitive data.
* These implementations are designed for readability and algorithmic clarity, **NOT** for security.
* They are **vulnerable** to side-channel attacks (timing attacks, power analysis) and do not implement constant-time execution.
* No standard padding or secure memory wiping mechanisms are guaranteed.

Use standard libraries (e.g., OpenSSL, PyCryptodome) for any commercial or industrial application.

## 📂 Repository Contents

### 1. AES-128 (Advanced Encryption Standard)
* **File:** `aes_cbc_implementation.c`
* **Description:** A raw implementation of the AES encryption algorithm in C.
* **Key Features:**
    * Manual implementation of SP-network layers: `SubBytes`, `ShiftRows`, `MixColumns`, `AddRoundKey`.
    * Demonstrates state matrix manipulation using bitwise operations.
    * Includes a basic implementation of **CBC (Cipher Block Chaining)** mode.

### 2. Elliptic Curve Cryptography (ECC) over Finite Fields
* **File:** `ecc_finite_field.py`
* **Description:** A pure Python implementation of Elliptic Curve arithmetic defined over a finite field $F_p$.
* **Key Features:**
    * Implements point addition and point doubling formulas analytically.
    * Calculates modular inverse for finite field division.
    * Demonstrates the "Discrete Logarithm Problem" difficulty basis.
    * Includes group order calculation and point generation logic.

### 3. Cyclic Group Generator Search
* **File:** `cyclic_group_generator.sage`
* **Description:** An algorithmic approach to finding generators of a cyclic group, inspired by SageMath logic.
* **Concepts:** Group Theory, Primitive Roots, Order of an Element, Factorization.
