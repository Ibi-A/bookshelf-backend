#!/usr/bin/env python3

from aws_cdk import core

from bookshelf_backend.bookshelf_backend_stack import BookshelfBackendStack


app = core.App()
BookshelfBackendStack(app, "bookshelf-backend")

app.synth()
