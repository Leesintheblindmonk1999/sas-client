"""Command line interface for sas-client."""

from __future__ import annotations

import argparse
import json
import sys
from typing import Any

from .client import DEFAULT_BASE_URL, SASClient
from .exceptions import (
    SASAuthenticationError,
    SASClientError,
    SASRateLimitError,
    SASServerError,
)


def _print_json(data: dict[str, Any]) -> None:
    print(json.dumps(data, indent=2, ensure_ascii=False))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="sas",
        description="CLI for SAS - Symbiotic Autoprotection System.",
    )

    parser.add_argument(
        "--base-url",
        default=DEFAULT_BASE_URL,
        help=f"SAS API base URL. Default: {DEFAULT_BASE_URL}",
    )
    parser.add_argument(
        "--api-key",
        default=None,
        help="SAS API key. If omitted, reads SAS_API_KEY or SAS_KEY.",
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=30.0,
        help="Request timeout in seconds.",
    )

    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("health", help="Check /health.")
    sub.add_parser("readyz", help="Check /readyz.")
    sub.add_parser("public-stats", help="Fetch /public/stats.")
    sub.add_parser("plans", help="Show hosted SAS plan information.")

    p_activity = sub.add_parser("public-activity", help="Fetch /public/activity.")
    p_activity.add_argument("--limit", type=int, default=20, help="Number of events, max 100.")

    p_request_key = sub.add_parser(
        "request-key",
        help="Request a personal Free SAS API key by email.",
    )
    p_request_key.add_argument("--email", required=True, help="Email address to receive the key.")
    p_request_key.add_argument("--name", default=None, help="Optional display name.")

    p_demo = sub.add_parser(
        "demo-audit",
        help="Run the public no-key demo audit endpoint.",
    )
    p_demo.add_argument("source", help="Reference/source text.")
    p_demo.add_argument("response", help="Response/output text to audit.")

    sub.add_parser("whoami", help="Show current API key identity, plan and quota.")

    p_audit = sub.add_parser("audit", help="Audit one text using /v1/audit.")
    p_audit.add_argument("text", help="Text to audit.")
    p_audit.add_argument("--no-experimental", action="store_true", help="Send experimental=false.")

    p_diff = sub.add_parser("diff", help="Compare two texts using /v1/diff.")
    p_diff.add_argument("text_a", help="First text.")
    p_diff.add_argument("text_b", help="Second text.")
    p_diff.add_argument("--no-experimental", action="store_true", help="Send experimental=false.")

    p_chat = sub.add_parser("chat", help="Send one message using /v1/chat.")
    p_chat.add_argument("message", help="Message to send.")
    p_chat.add_argument("--no-experimental", action="store_true", help="Send experimental=false.")

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    client = SASClient(
        base_url=args.base_url,
        api_key=args.api_key,
        timeout=args.timeout,
    )

    try:
        if args.command == "health":
            _print_json(client.health())
        elif args.command == "readyz":
            _print_json(client.readyz())
        elif args.command == "public-stats":
            _print_json(client.public_stats())
        elif args.command == "public-activity":
            _print_json(client.public_activity(limit=args.limit))
        elif args.command == "plans":
            _print_json(client.plans())
        elif args.command == "request-key":
            _print_json(client.request_key(email=args.email, name=args.name))
        elif args.command == "demo-audit":
            _print_json(client.demo_audit(args.source, args.response))
        elif args.command == "whoami":
            _print_json(client.whoami())
        elif args.command == "audit":
            _print_json(
                client.audit(args.text, experimental=not args.no_experimental)
            )
        elif args.command == "diff":
            _print_json(
                client.diff(
                    text_a=args.text_a,
                    text_b=args.text_b,
                    experimental=not args.no_experimental,
                )
            )
        elif args.command == "chat":
            _print_json(
                client.chat(args.message, experimental=not args.no_experimental)
            )
        else:
            parser.error(f"Unknown command: {args.command}")
            return 2

        return 0

    except SASRateLimitError as exc:
        print(str(exc), file=sys.stderr)
        print(
            "Rate limit reached. Request a personal Free key or use your own SAS_API_KEY.",
            file=sys.stderr,
        )
        return 4

    except SASAuthenticationError as exc:
        print(str(exc), file=sys.stderr)
        print(
            "Authentication failed. Set SAS_API_KEY/SAS_KEY or pass --api-key.",
            file=sys.stderr,
        )
        return 3

    except SASServerError as exc:
        print(str(exc), file=sys.stderr)
        return 5

    except SASClientError as exc:
        print(str(exc), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
