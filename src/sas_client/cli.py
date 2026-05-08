"""Command line interface for sas-client."""

from __future__ import annotations

import argparse
import json
import sys
from typing import Any

from .client import DEFAULT_BASE_URL, SASClient
from .exceptions import SASClientError


def _print_json(data: dict[str, Any]) -> None:
    print(json.dumps(data, indent=2, ensure_ascii=False))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="sas", description="CLI for SAS - Symbiotic Autoprotection System.")
    parser.add_argument("--base-url", default=DEFAULT_BASE_URL, help=f"SAS API base URL. Default: {DEFAULT_BASE_URL}")
    parser.add_argument("--api-key", default=None, help="SAS API key. If omitted, reads SAS_API_KEY.")
    parser.add_argument("--timeout", type=float, default=30.0, help="Request timeout in seconds.")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("health", help="Check /health.")
    sub.add_parser("readyz", help="Check /readyz.")
    sub.add_parser("public-stats", help="Fetch /public/stats.")
    p_activity = sub.add_parser("public-activity", help="Fetch /public/activity.")
    p_activity.add_argument("--limit", type=int, default=20, help="Number of events, max 100.")
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
    client = SASClient(base_url=args.base_url, api_key=args.api_key, timeout=args.timeout)
    try:
        if args.command == "health":
            _print_json(client.health())
        elif args.command == "readyz":
            _print_json(client.readyz())
        elif args.command == "public-stats":
            _print_json(client.public_stats())
        elif args.command == "public-activity":
            _print_json(client.public_activity(limit=args.limit))
        elif args.command == "audit":
            _print_json(client.audit(args.text, experimental=not args.no_experimental))
        elif args.command == "diff":
            _print_json(client.diff(text_a=args.text_a, text_b=args.text_b, experimental=not args.no_experimental))
        elif args.command == "chat":
            _print_json(client.chat(args.message, experimental=not args.no_experimental))
        else:
            parser.error(f"Unknown command: {args.command}")
            return 2
        return 0
    except SASClientError as exc:
        print(str(exc), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
