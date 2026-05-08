# sas-client

[![PyPI](https://img.shields.io/pypi/v/sas-client?style=for-the-badge)](https://pypi.org/project/sas-client/)
[![Python](https://img.shields.io/pypi/pyversions/sas-client?style=for-the-badge)](https://pypi.org/project/sas-client/)
[![License](https://img.shields.io/badge/License-GPL--3.0%20%2B%20Durante%20Invariance-purple?style=for-the-badge)](LICENSE)
[![SAS API](https://img.shields.io/badge/SAS%20API-online-brightgreen?style=for-the-badge)](https://sas-api.onrender.com)
[![Zenodo](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.19702379-blue?style=for-the-badge)](https://doi.org/10.5281/zenodo.19702379)

Official Python client and CLI for **SAS - Symbiotic Autoprotection System**.

SAS is a structural coherence audit API for generative AI outputs. It exposes operational endpoints for hallucination / semantic rupture detection using the **κD = 0.56** threshold.

---

## Language / Idioma

- [English](#english)
- [Español](#español)

---

<a id="english"></a>

# English

## Links

- Public API: <https://sas-api.onrender.com>
- API docs: <https://sas-api.onrender.com/docs>
- Main repository: <https://github.com/Leesintheblindmonk1999/SAS>
- Client repository: <https://github.com/Leesintheblindmonk1999/sas-client>
- Landing page: <https://leesintheblindmonk1999.github.io/sas-landing/>
- PyPI package: <https://pypi.org/project/sas-client/>
- Zenodo DOI: <https://doi.org/10.5281/zenodo.19702379>

---

## Install

```bash
pip install sas-client
```

For local development from source:

```bash
pip install -e .[dev]
```

---

## Quick Start

```python
from sas_client import SASClient

client = SASClient(api_key="YOUR_API_KEY")

result = client.diff(
    text_a="Python is a programming language used for data analysis.",
    text_b="A python is a large tropical snake."
)

print(result["isi"])
print(result["verdict"])
print(result.get("evidence", {}).get("fired_modules"))
```

---

## API Key

The hosted SAS API expects an API key for protected endpoints.

Pass the key directly:

```python
client = SASClient(api_key="YOUR_API_KEY")
```

Or use an environment variable:

```bash
export SAS_API_KEY="YOUR_API_KEY"
```

Windows PowerShell:

```powershell
$env:SAS_API_KEY="YOUR_API_KEY"
```

---

## Python Usage

### Health

```python
from sas_client import SASClient

client = SASClient()
print(client.health())
```

### Readiness

```python
from sas_client import SASClient

client = SASClient()
print(client.readyz())
```

### Public stats

```python
from sas_client import SASClient

client = SASClient()
print(client.public_stats())
print(client.public_activity(limit=10))
```

### Audit one text

```python
from sas_client import SASClient

client = SASClient(api_key="YOUR_API_KEY")

result = client.audit(
    "Paris is the capital of France. The Eiffel Tower is located in Berlin."
)

print(result)
```

### Compare two texts

```python
from sas_client import SASClient

client = SASClient(api_key="YOUR_API_KEY")

result = client.diff(
    text_a="Python is a programming language commonly used for automation.",
    text_b="A python is a large tropical snake."
)

print(result["isi"])
print(result["verdict"])
```

### Chat endpoint

```python
from sas_client import SASClient

client = SASClient(api_key="YOUR_API_KEY")

result = client.chat("Explain κD = 0.56 in one paragraph.")
print(result)
```

---

## CLI Usage

After installation, the `sas` command is available.

```bash
sas health
sas readyz
sas public-stats
sas public-activity --limit 10
```

For authenticated endpoints, pass `--api-key` before the subcommand:

```bash
sas --api-key YOUR_API_KEY audit "Paris is the capital of France. The Eiffel Tower is located in Berlin."
sas --api-key YOUR_API_KEY diff "Python is a programming language." "A python is a snake."
```

Or use `SAS_API_KEY`:

```bash
export SAS_API_KEY="YOUR_API_KEY"
sas diff "Python is a programming language." "A python is a snake."
```

Windows PowerShell:

```powershell
$env:SAS_API_KEY="YOUR_API_KEY"
sas diff "Python is a programming language." "A python is a snake."
```

Override the API URL:

```bash
sas --base-url https://your-sas-instance.example.com health
```

---

## Default API

The client defaults to:

```text
https://sas-api.onrender.com
```

Self-hosted deployments can be used by passing a custom `base_url`.

---

## Privacy

This client does not collect telemetry.

Requests are sent only to the configured SAS API base URL.

The client does not store API keys, raw requests, or responses locally.

---

## License

GPL-3.0 + Durante Invariance License.

The SAS framework and **κD = 0.56** require attribution to **Gonzalo Emir Durante** and citation of the public SAS repository / DOI when used for semantic invariance, hallucination detection, or similar structural coherence auditing purposes.

---

<a id="español"></a>

# Español

## Enlaces

- API pública: <https://sas-api.onrender.com>
- Documentación API: <https://sas-api.onrender.com/docs>
- Repositorio principal: <https://github.com/Leesintheblindmonk1999/SAS>
- Repositorio del cliente: <https://github.com/Leesintheblindmonk1999/sas-client>
- Landing page: <https://leesintheblindmonk1999.github.io/sas-landing/>
- Paquete PyPI: <https://pypi.org/project/sas-client/>
- Zenodo DOI: <https://doi.org/10.5281/zenodo.19702379>

---

## Instalación

```bash
pip install sas-client
```

Para desarrollo local desde el código fuente:

```bash
pip install -e .[dev]
```

---

## Inicio rápido

```python
from sas_client import SASClient

client = SASClient(api_key="YOUR_API_KEY")

result = client.diff(
    text_a="Python is a programming language used for data analysis.",
    text_b="A python is a large tropical snake."
)

print(result["isi"])
print(result["verdict"])
print(result.get("evidence", {}).get("fired_modules"))
```

---

## API Key

La API pública alojada de SAS requiere API key para endpoints protegidos.

Podés pasar la key directamente:

```python
client = SASClient(api_key="YOUR_API_KEY")
```

O usar una variable de entorno:

```bash
export SAS_API_KEY="YOUR_API_KEY"
```

Windows PowerShell:

```powershell
$env:SAS_API_KEY="YOUR_API_KEY"
```

---

## Uso desde Python

### Health

```python
from sas_client import SASClient

client = SASClient()
print(client.health())
```

### Readiness

```python
from sas_client import SASClient

client = SASClient()
print(client.readyz())
```

### Estadísticas públicas

```python
from sas_client import SASClient

client = SASClient()
print(client.public_stats())
print(client.public_activity(limit=10))
```

### Auditar un texto

```python
from sas_client import SASClient

client = SASClient(api_key="YOUR_API_KEY")

result = client.audit(
    "Paris is the capital of France. The Eiffel Tower is located in Berlin."
)

print(result)
```

### Comparar dos textos

```python
from sas_client import SASClient

client = SASClient(api_key="YOUR_API_KEY")

result = client.diff(
    text_a="Python is a programming language commonly used for automation.",
    text_b="A python is a large tropical snake."
)

print(result["isi"])
print(result["verdict"])
```

### Chat endpoint

```python
from sas_client import SASClient

client = SASClient(api_key="YOUR_API_KEY")

result = client.chat("Explain κD = 0.56 in one paragraph.")
print(result)
```

---

## Uso CLI

Después de instalar, queda disponible el comando `sas`.

```bash
sas health
sas readyz
sas public-stats
sas public-activity --limit 10
```

Para endpoints autenticados, `--api-key` va antes del subcomando:

```bash
sas --api-key YOUR_API_KEY audit "Paris is the capital of France. The Eiffel Tower is located in Berlin."
sas --api-key YOUR_API_KEY diff "Python is a programming language." "A python is a snake."
```

O usando `SAS_API_KEY`:

```bash
export SAS_API_KEY="YOUR_API_KEY"
sas diff "Python is a programming language." "A python is a snake."
```

Windows PowerShell:

```powershell
$env:SAS_API_KEY="YOUR_API_KEY"
sas diff "Python is a programming language." "A python is a snake."
```

Cambiar la URL de API:

```bash
sas --base-url https://your-sas-instance.example.com health
```

---

## API por defecto

El cliente usa por defecto:

```text
https://sas-api.onrender.com
```

Para instancias autoalojadas, usá `base_url`.

---

## Privacidad

Este cliente no recolecta telemetría.

Las requests se envían únicamente a la URL SAS API configurada.

El cliente no almacena API keys, requests crudas ni respuestas localmente.

---

## Licencia

GPL-3.0 + Durante Invariance License.

El framework SAS y **κD = 0.56** requieren atribución a **Gonzalo Emir Durante** y cita del repositorio / DOI público de SAS cuando se usen para invariancia semántica, detección de alucinaciones o auditoría estructural de coherencia.
