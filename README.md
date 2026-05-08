# sas-client

Python client and CLI for **SAS - Symbiotic Autoprotection System**.

SAS is a structural coherence audit API for generative AI outputs. It exposes operational endpoints for hallucination / semantic rupture detection using the κD = 0.56 threshold.

- Public API: <https://sas-api.onrender.com>
- API docs: <https://sas-api.onrender.com/docs>
- Main repository: <https://github.com/Leesintheblindmonk1999/SAS>
- Landing page: <https://leesintheblindmonk1999.github.io/sas-landing/>
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

client = SASClient(api_key="sas_test_key_2026")

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

```python
client = SASClient(api_key="sas_test_key_2026")
```

Or use an environment variable:

```bash
export SAS_API_KEY="sas_test_key_2026"
```

Windows PowerShell:

```powershell
$env:SAS_API_KEY="sas_test_key_2026"
```

---

## Usage

### Health

```python
from sas_client import SASClient

client = SASClient()
print(client.health())
```

### Audit one text

```python
from sas_client import SASClient

client = SASClient(api_key="sas_test_key_2026")

result = client.audit(
    "Paris is the capital of France. The Eiffel Tower is located in Berlin."
)

print(result)
```

### Compare two texts

```python
from sas_client import SASClient

client = SASClient(api_key="sas_test_key_2026")

result = client.diff(
    text_a="Python is a programming language commonly used for automation.",
    text_b="A python is a large tropical snake."
)

print(result["isi"])
print(result["verdict"])
```

### Public stats

```python
from sas_client import SASClient

client = SASClient()
print(client.public_stats())
print(client.public_activity(limit=10))
```

---

## CLI

After installation, the `sas` command is available.

```bash
sas health
sas public-stats
sas public-activity --limit 10
sas audit "Paris is the capital of France. The Eiffel Tower is located in Berlin." --api-key sas_test_key_2026
sas diff "Python is a programming language." "A python is a snake." --api-key sas_test_key_2026
```

Override the API URL:

```bash
sas --base-url https://your-sas-instance.example.com health
```

---

## Privacy

This client does not collect telemetry.

Requests are sent only to the configured SAS API base URL.

---

## License

GPL-3.0 + Durante Invariance License.

The SAS framework and κD = 0.56 require attribution to Gonzalo Emir Durante and citation of the public SAS repository / DOI when used for semantic invariance, hallucination detection, or similar structural coherence auditing purposes.
