#!/usr/bin/env python3
# Designed for use with boofuzz v0.2.0

# More advanced request definitions can be found in the request_definitions directory.

from boofuzz import *


def main():
    session = Session(
        target=Target(connection=TCPSocketConnection("dialserver", 56790)),
    )
    req = Request("HTTP-Request", children=(
    Block("Request-Line", children=(
        Group(name="Method", values=["GET", "HEAD", "POST", "PUT", "DELETE", "CONNECT", "OPTIONS", "TRACE"]),
        Delim(name="space-1", default_value=" "),
        String(name="Request-URI", default_value="/index.html"),
        Delim(name="space-2", default_value=" "),
        String(name="HTTP-Version", default_value="HTTP/1.1"),
        Static(name="CRLF", default_value="\r\n"),
        Static(name="Content-Length-Header", default_value="Content-Length:"),
        Delim(name="space-3", default_value=" "),
        )),
        FuzzableBlock("Content-Length-Param", children=(
            QWord(name="Content-Length-Value", fuzzable=True, output_format="ascii", signed=True),
            Static(name="CRLF-end", default_value="\r\n"),
        )),

        Static(name="CRLF", default_value="\r\n"),
    ))

    # fmt: on

    session.connect(req)

    session.fuzz()


if __name__ == "__main__":
    main()
