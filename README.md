# sas-client

<div align="center">

**Official Python client and CLI for SAS — Symbiotic Autoprotection System**  
**κD = 0.56 · Durante Constant · Structural Coherence Auditing for Generative AI**

[![PyPI](https://img.shields.io/pypi/v/sas-client?style=for-the-badge)](https://pypi.org/project/sas-client/)
[![Python](https://img.shields.io/pypi/pyversions/sas-client?style=for-the-badge)](https://pypi.org/project/sas-client/)
[![License](https://img.shields.io/badge/License-GPL--3.0%20%2B%20Durante%20Invariance-purple?style=for-the-badge)](LICENSE.md)
[![SAS API](https://img.shields.io/badge/SAS%20API-online-brightgreen?style=for-the-badge)](https://sas-api.onrender.com)
[![Landing](https://img.shields.io/badge/Landing-sas--landing-00ffd0?style=for-the-badge)](https://leesintheblindmonk1999.github.io/sas-landing/)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.19702379-blue?style=for-the-badge)](https://doi.org/10.5281/zenodo.19702379)

</div>

---

## Language / Idioma

- [English](#english)
- [Español](#español)

---

<a id="english"></a>

# English

## Overview

` sas-client ` is the official Python SDK and command-line client for **SAS — Symbiotic Autoprotection System**.

SAS is a structural coherence audit API for generative AI outputs. It evaluates whether a generated response preserves semantic, logical, numerical, and reference-related coherence relative to a source text using the **κD = 0.56** operational threshold and the **Invariant Similarity Index (ISI)**.

The client is designed for:

- developers integrating SAS into Python applications;
- RAG / LLM pipelines;
- hallucination and semantic rupture auditing;
- CLI-based testing and debugging;
- self-hosted SAS deployments;
- public hosted API usage.

---

## Ecosystem Links

| Resource | URL |
|---|---|
| Hosted SAS API | <https://sas-api.onrender.com> |
| API docs | <https://sas-api.onrender.com/docs> |
| Main SAS repository | <https://github.com/Leesintheblindmonk1999/SAS> |
| Client repository | <https://github.com/Leesintheblindmonk1999/sas-client> |
| Landing page | <https://leesintheblindmonk1999.github.io/sas-landing/> |
| PyPI package | <https://pypi.org/project/sas-client/> |
| Zenodo DOI | <https://doi.org/10.5281/zenodo.19702379> |

---

## Installation

```bash
pip install sas-client
```

For local development from source:

```bash
git clone https://github.com/Leesintheblindmonk1999/sas-client.git
cd sas-client
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

Typical output fields include:

```json
{
  "isi": 0.0,
  "kappa_d": 0.56,
  "verdict": "MANIFOLD_RUPTURE",
  "detected_hallucination": true,
  "fired_modules": []
}
```

---

## API Keys

Protected endpoints require an API key.

### Option 1 — Use an existing key

Pass the key directly:

```python
client = SASClient(api_key="YOUR_API_KEY")
```

Or use the environment variable:

```bash
export SAS_API_KEY="YOUR_API_KEY"
```

Windows PowerShell:

```powershell
$env:SAS_API_KEY="YOUR_API_KEY"
```

Then instantiate the client without passing the key explicitly:

```python
from sas_client import SASClient

client = SASClient()
```

---

### Option 2 — Request a Free hosted API key

The hosted SAS API supports automatic Free key generation:

```bash
curl -X POST https://sas-api.onrender.com/public/request-key \
  -H "Content-Type: application/json" \
  -d '{"email": "your@email.com", "name": "Your Name"}'
```

The API key is generated and delivered by email automatically.

Free tier default:

```text
50 requests/day
```

Limit:

```text
1 Free key per email per day
```

---

### Option 3 — Pro key through payment automation

Hosted Pro access is connected to payment automation through:

- **Polar** for international card payments;
- **Mercado Pago** for LATAM payment flows.

After payment confirmation, the hosted service can generate and send the Pro API key automatically by email.

> Payment, key issuance, and plan automation are hosted-service features.  
> They do not change the open-source license of the client or the self-hosted SAS engine.

---

## Default API

The client defaults to:

```text
https://sas-api.onrender.com
```

Self-hosted deployments can be used by passing a custom `base_url`:

```python
from sas_client import SASClient

client = SASClient(
    api_key="YOUR_API_KEY",
    base_url="https://your-sas-instance.example.com"
)
```

CLI override:

```bash
sas --base-url https://your-sas-instance.example.com health
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

### Public stats and activity

```python
from sas_client import SASClient

client = SASClient()

print(client.public_stats())
print(client.public_activity(limit=10))
```

These public endpoints do not require an API key.

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
    text_a="The Eiffel Tower is located in Paris, France.",
    text_b="The Eiffel Tower is located in Berlin, Germany."
)

print(result["isi"])
print(result["kappa_d"])
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

### Public commands

```bash
sas health
sas readyz
sas public-stats
sas public-activity --limit 10
```

### Authenticated commands

For authenticated endpoints, pass `--api-key` before the subcommand:

```bash
sas --api-key YOUR_API_KEY audit "Paris is the capital of France. The Eiffel Tower is located in Berlin."
sas --api-key YOUR_API_KEY diff "Python is a programming language." "A python is a snake."
sas --api-key YOUR_API_KEY chat "Explain κD = 0.56 in one paragraph."
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

### Custom API URL

```bash
sas --base-url https://your-sas-instance.example.com health
sas --base-url http://localhost:8000 readyz
```

---

## Current Endpoint Coverage

| Capability | API endpoint | Python client | CLI |
|---|---|---:|---:|
| Health check | `GET /health` | `client.health()` | `sas health` |
| Readiness check | `GET /readyz` | `client.readyz()` | `sas readyz` |
| Public stats | `GET /public/stats` | `client.public_stats()` | `sas public-stats` |
| Public activity | `GET /public/activity` | `client.public_activity(limit=10)` | `sas public-activity --limit 10` |
| Single-text audit | `POST /v1/audit` | `client.audit(text)` | `sas audit "text"` |
| Source-vs-response diff | `POST /v1/diff` | `client.diff(text_a, text_b)` | `sas diff "A" "B"` |
| Chat endpoint | `POST /v1/chat` | `client.chat(message)` | `sas chat "message"` |

---

## Hosted API Features Not Yet Wrapped as First-Class Client Commands

The hosted SAS API may expose additional public or billing-related endpoints such as:

| Hosted capability | Endpoint | Current recommendation |
|---|---|---|
| Public demo audit | `POST /public/demo/audit` | Use `curl` or direct HTTP until wrapped |
| Free key request | `POST /public/request-key` | Use `curl` until wrapped |
| Current account / plan | `GET /v1/whoami` | Use `curl` until wrapped |
| Polar payment webhook | hosted billing endpoint | Server-side only |
| Mercado Pago webhook | hosted billing endpoint | Server-side only |

Example:

```bash
curl -X POST https://sas-api.onrender.com/public/demo/audit \
  -H "Content-Type: application/json" \
  -d '{
    "source": "The Eiffel Tower is located in Paris, France.",
    "response": "The Eiffel Tower is located in Berlin, Germany."
  }'
```

Example:

```bash
curl https://sas-api.onrender.com/v1/whoami \
  -H "X-API-Key: sas_xxxxxxxxxxxxxxxxxxxxx"
```

---

## Recommended Next Client Commands

These are recommended improvements for the next `sas-client` release.

### Proposed Python methods

```python
client.demo_audit(source, response)
client.request_key(email, name=None)
client.whoami()
client.plans()
```

### Proposed CLI commands

```bash
sas demo-audit "source text" "response text"
sas request-key --email your@email.com --name "Your Name"
sas whoami
sas plans
```

### Proposed convenience modules

```text
sas_client.auth       # API key helpers, env loading, whoami
sas_client.public     # public demo, stats, activity, readiness
sas_client.billing    # hosted-plan helpers, Polar/Mercado Pago docs wrappers
sas_client.models     # typed response models / dataclasses
sas_client.errors     # typed exceptions for API errors
```

Suggested behavior:

- `demo-audit` should not require API key.
- `request-key` should not require API key.
- `whoami` should require API key.
- Billing webhooks should remain server-side and should not be exposed as client-side payment verification commands.
- The client should avoid storing keys locally by default.
- Optional local config should be explicit and documented.

---

## Error Handling

Recommended client behavior:

```python
from sas_client import SASClient, SASClientError

client = SASClient(api_key="YOUR_API_KEY")

try:
    result = client.diff("source", "response")
except SASClientError as exc:
    print(exc)
```

Recommended CLI behavior:

```bash
sas diff "source" "response"
echo $?
```

Exit code guidance for future CLI hardening:

| Exit code | Meaning |
|---:|---|
| `0` | Success |
| `1` | Generic client error |
| `2` | Invalid arguments |
| `3` | Authentication or plan error |
| `4` | Rate limit exceeded |
| `5` | Server unavailable |
| `6` | Network error |

---

## Privacy

This client does not collect telemetry.

Requests are sent only to the configured SAS API base URL.

The client does not store API keys, raw requests, or responses locally.

For hosted endpoints:

- API keys should be kept private.
- Do not paste API keys into public logs, screenshots, GitHub issues, or shell history.
- Public stats and public activity are designed to expose aggregated or anonymized operational metadata only.
- Payment automation through Polar or Mercado Pago is part of the hosted SAS service, not the local client package.

---

## Development

Install in editable mode:

```bash
pip install -e .[dev]
```

Run tests:

```bash
pytest
```

Run the CLI locally:

```bash
python -m sas_client --help
```

Build package:

```bash
python -m build
```

Check package metadata:

```bash
twine check dist/*
```

---

## Packaging Checklist

Before publishing a new PyPI release:

- [ ] Update `pyproject.toml` version.
- [ ] Update `CHANGELOG.md`.
- [ ] Update this README.
- [ ] Run tests.
- [ ] Test Python examples.
- [ ] Test CLI examples.
- [ ] Verify package build.
- [ ] Verify no API keys or secrets are committed.
- [ ] Publish to TestPyPI first if possible.
- [ ] Publish to PyPI.
- [ ] Tag the release on GitHub.

---

## License

This client is published under:

```text
GPL-3.0 + Durante Invariance License
```

The SAS framework and **κD = 0.56** require attribution to **Gonzalo Emir Durante** and citation of the public SAS repository / DOI when used for semantic invariance, hallucination detection, or structural coherence auditing.

Main SAS DOI:

```text
https://doi.org/10.5281/zenodo.19702379
```

---

<a id="español"></a>

# Español

## Descripción general

` sas-client ` es el SDK oficial de Python y cliente de línea de comandos para **SAS — Symbiotic Autoprotection System**.

SAS es una API de auditoría de coherencia estructural para salidas de IA generativa. Evalúa si una respuesta generada preserva coherencia semántica, lógica, numérica y referencial respecto de un texto fuente usando el umbral operacional **κD = 0.56** y el **Invariant Similarity Index (ISI)**.

El cliente está diseñado para:

- desarrolladores que integran SAS en aplicaciones Python;
- pipelines RAG / LLM;
- auditoría de alucinaciones y ruptura semántica;
- pruebas y debugging desde CLI;
- despliegues SAS autoalojados;
- uso de la API pública alojada.

---

## Enlaces del ecosistema

| Recurso | URL |
|---|---|
| API SAS alojada | <https://sas-api.onrender.com> |
| Documentación API | <https://sas-api.onrender.com/docs> |
| Repositorio principal SAS | <https://github.com/Leesintheblindmonk1999/SAS> |
| Repositorio del cliente | <https://github.com/Leesintheblindmonk1999/sas-client> |
| Landing page | <https://leesintheblindmonk1999.github.io/sas-landing/> |
| Paquete PyPI | <https://pypi.org/project/sas-client/> |
| Zenodo DOI | <https://doi.org/10.5281/zenodo.19702379> |

---

## Instalación

```bash
pip install sas-client
```

Para desarrollo local desde el código fuente:

```bash
git clone https://github.com/Leesintheblindmonk1999/sas-client.git
cd sas-client
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

Campos típicos de salida:

```json
{
  "isi": 0.0,
  "kappa_d": 0.56,
  "verdict": "MANIFOLD_RUPTURE",
  "detected_hallucination": true,
  "fired_modules": []
}
```

---

## API Keys

Los endpoints protegidos requieren API key.

### Opción 1 — Usar una key existente

Pasá la key directamente:

```python
client = SASClient(api_key="YOUR_API_KEY")
```

O usá la variable de entorno:

```bash
export SAS_API_KEY="YOUR_API_KEY"
```

Windows PowerShell:

```powershell
$env:SAS_API_KEY="YOUR_API_KEY"
```

Después podés instanciar el cliente sin pasar la key explícitamente:

```python
from sas_client import SASClient

client = SASClient()
```

---

### Opción 2 — Solicitar una Free key alojada

La API SAS alojada permite generación automática de Free keys:

```bash
curl -X POST https://sas-api.onrender.com/public/request-key \
  -H "Content-Type: application/json" \
  -d '{"email": "your@email.com", "name": "Tu Nombre"}'
```

La API key se genera y se envía automáticamente por email.

Free tier por defecto:

```text
50 requests/día
```

Límite:

```text
1 Free key por email por día
```

---

### Opción 3 — Pro key mediante pago automático

El acceso Pro alojado está conectado a automatización de pagos mediante:

- **Polar** para pagos internacionales con tarjeta;
- **Mercado Pago** para flujos de pago LATAM.

Después de confirmarse el pago, el servicio alojado puede generar y enviar automáticamente la API key Pro por email.

> Pagos, emisión de keys y automatización de planes son funciones del servicio alojado.  
> No modifican la licencia open source del cliente ni del motor SAS autoalojado.

---

## API por defecto

El cliente usa por defecto:

```text
https://sas-api.onrender.com
```

Los despliegues autoalojados pueden usarse pasando `base_url`:

```python
from sas_client import SASClient

client = SASClient(
    api_key="YOUR_API_KEY",
    base_url="https://your-sas-instance.example.com"
)
```

Override desde CLI:

```bash
sas --base-url https://your-sas-instance.example.com health
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

### Estadísticas públicas y actividad

```python
from sas_client import SASClient

client = SASClient()

print(client.public_stats())
print(client.public_activity(limit=10))
```

Estos endpoints públicos no requieren API key.

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
    text_a="The Eiffel Tower is located in Paris, France.",
    text_b="The Eiffel Tower is located in Berlin, Germany."
)

print(result["isi"])
print(result["kappa_d"])
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

### Comandos públicos

```bash
sas health
sas readyz
sas public-stats
sas public-activity --limit 10
```

### Comandos autenticados

Para endpoints autenticados, pasá `--api-key` antes del subcomando:

```bash
sas --api-key YOUR_API_KEY audit "Paris is the capital of France. The Eiffel Tower is located in Berlin."
sas --api-key YOUR_API_KEY diff "Python is a programming language." "A python is a snake."
sas --api-key YOUR_API_KEY chat "Explain κD = 0.56 in one paragraph."
```

O usá `SAS_API_KEY`:

```bash
export SAS_API_KEY="YOUR_API_KEY"

sas diff "Python is a programming language." "A python is a snake."
```

Windows PowerShell:

```powershell
$env:SAS_API_KEY="YOUR_API_KEY"

sas diff "Python is a programming language." "A python is a snake."
```

### URL de API personalizada

```bash
sas --base-url https://your-sas-instance.example.com health
sas --base-url http://localhost:8000 readyz
```

---

## Cobertura actual de endpoints

| Capacidad | Endpoint API | Cliente Python | CLI |
|---|---|---:|---:|
| Health check | `GET /health` | `client.health()` | `sas health` |
| Readiness check | `GET /readyz` | `client.readyz()` | `sas readyz` |
| Estadísticas públicas | `GET /public/stats` | `client.public_stats()` | `sas public-stats` |
| Actividad pública | `GET /public/activity` | `client.public_activity(limit=10)` | `sas public-activity --limit 10` |
| Auditoría de un texto | `POST /v1/audit` | `client.audit(text)` | `sas audit "text"` |
| Diff fuente-respuesta | `POST /v1/diff` | `client.diff(text_a, text_b)` | `sas diff "A" "B"` |
| Chat endpoint | `POST /v1/chat` | `client.chat(message)` | `sas chat "message"` |

---

## Funciones de la API alojada todavía no envueltas como comandos first-class

La API SAS alojada puede exponer endpoints públicos o de billing adicionales como:

| Capacidad alojada | Endpoint | Recomendación actual |
|---|---|---|
| Demo pública de auditoría | `POST /public/demo/audit` | Usar `curl` o HTTP directo hasta envolverlo |
| Solicitud de Free key | `POST /public/request-key` | Usar `curl` hasta envolverlo |
| Cuenta / plan actual | `GET /v1/whoami` | Usar `curl` hasta envolverlo |
| Webhook Polar | endpoint alojado de billing | Solo server-side |
| Webhook Mercado Pago | endpoint alojado de billing | Solo server-side |

Ejemplo:

```bash
curl -X POST https://sas-api.onrender.com/public/demo/audit \
  -H "Content-Type: application/json" \
  -d '{
    "source": "The Eiffel Tower is located in Paris, France.",
    "response": "The Eiffel Tower is located in Berlin, Germany."
  }'
```

Ejemplo:

```bash
curl https://sas-api.onrender.com/v1/whoami \
  -H "X-API-Key: sas_xxxxxxxxxxxxxxxxxxxxx"
```

---

## Próximos comandos recomendados para el cliente

Estas son mejoras recomendadas para la próxima release de `sas-client`.

### Métodos Python propuestos

```python
client.demo_audit(source, response)
client.request_key(email, name=None)
client.whoami()
client.plans()
```

### Comandos CLI propuestos

```bash
sas demo-audit "source text" "response text"
sas request-key --email your@email.com --name "Your Name"
sas whoami
sas plans
```

### Módulos de conveniencia propuestos

```text
sas_client.auth       # Helpers de API key, carga de env, whoami
sas_client.public     # Demo pública, stats, activity, readiness
sas_client.billing    # Helpers/documentación para hosted plans, Polar/Mercado Pago
sas_client.models     # Modelos tipados / dataclasses
sas_client.errors     # Excepciones tipadas para errores API
```

Comportamiento sugerido:

- `demo-audit` no debería requerir API key.
- `request-key` no debería requerir API key.
- `whoami` debería requerir API key.
- Los webhooks de billing deberían permanecer server-side y no exponerse como comandos de verificación de pago del cliente.
- El cliente no debería almacenar keys localmente por defecto.
- Toda configuración local opcional debería ser explícita y documentada.

---

## Manejo de errores

Comportamiento recomendado del cliente:

```python
from sas_client import SASClient, SASClientError

client = SASClient(api_key="YOUR_API_KEY")

try:
    result = client.diff("source", "response")
except SASClientError as exc:
    print(exc)
```

Comportamiento recomendado de CLI:

```bash
sas diff "source" "response"
echo $?
```

Guía de exit codes para endurecimiento futuro del CLI:

| Exit code | Significado |
|---:|---|
| `0` | Éxito |
| `1` | Error genérico del cliente |
| `2` | Argumentos inválidos |
| `3` | Error de autenticación o plan |
| `4` | Rate limit excedido |
| `5` | Servidor no disponible |
| `6` | Error de red |

---

## Privacidad

Este cliente no recolecta telemetría.

Las requests se envían únicamente a la URL SAS API configurada.

El cliente no almacena API keys, requests crudas ni respuestas localmente.

Para endpoints alojados:

- mantené privadas las API keys;
- no pegues API keys en logs públicos, capturas, issues de GitHub ni historial de shell;
- las stats públicas y la actividad pública están diseñadas para exponer solo metadata operacional agregada o anonimizada;
- la automatización de pagos mediante Polar o Mercado Pago forma parte del servicio SAS alojado, no del paquete cliente local.

---

## Desarrollo

Instalar en modo editable:

```bash
pip install -e .[dev]
```

Ejecutar tests:

```bash
pytest
```

Ejecutar CLI localmente:

```bash
python -m sas_client --help
```

Build del paquete:

```bash
python -m build
```

Verificar metadata del paquete:

```bash
twine check dist/*
```

---

## Checklist de publicación

Antes de publicar una nueva release en PyPI:

- [ ] Actualizar versión en `pyproject.toml`.
- [ ] Actualizar `CHANGELOG.md`.
- [ ] Actualizar este README.
- [ ] Ejecutar tests.
- [ ] Probar ejemplos Python.
- [ ] Probar ejemplos CLI.
- [ ] Verificar build del paquete.
- [ ] Confirmar que no haya API keys ni secretos commiteados.
- [ ] Publicar primero en TestPyPI si es posible.
- [ ] Publicar en PyPI.
- [ ] Crear tag de release en GitHub.

---

## Licencia

Este cliente se publica bajo:

```text
GPL-3.0 + Durante Invariance License
```

El framework SAS y **κD = 0.56** requieren atribución a **Gonzalo Emir Durante** y cita del repositorio / DOI público de SAS cuando se usen para invariancia semántica, detección de alucinaciones o auditoría estructural de coherencia.

DOI principal de SAS:

```text
https://doi.org/10.5281/zenodo.19702379
```
